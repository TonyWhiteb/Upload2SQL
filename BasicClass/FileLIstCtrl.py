import wx

class FileCtrl(wx.ListCtrl):
    
    def __init__(self, *args, **kwargs):
    
        super(FileCtrl, self).__init__(*args, **kwargs)

        self.currRow = None
        
        self.Bind(wx.EVT_LEFT_DOWN, self.OnFindCurrentRow)
        self.Bind(wx.EVT_RIGHT_DOWN, self.OnRightDown)

        self.numCols = 4
        self.haveEntries = False
        self.numEntries = 0
        

    
    def OnFindCurrentRow(self,event):
        if (self.currRow is not None):
            self.Select(self.currRow, False)

        row,_ignoredFlags = self.HitTest(event.GetPosition())

        self.currRow = row
        self.Select(row)
    def OnRightDown(self,event):

        menu = wx.Menu()
        menuItem = menu.Append(-1, 'Delet This File')

        self.Bind(wx.EVT_MENU, self.OnDeleteRow, menuItem)
        
        self.OnFindCurrentRow(event)

        self.PopupMenu(menu,event.GetPosition())
    def OnDeleteRow(self, event):

        if(self.currRow >= 0):

            assert(self.numEntries == len(self.entriesList))

            allSelectedRowData = self.GetAllSelectedRowData()

    def GetCurrRow(self):
        return self.currRow

    def WriteTextTuple(self, rowDataTuple):

        assert(len(rowDataTuple) >= self.numCols), 'Given data must have at least %d items.' %(self.numCols)

        for idx in range(self.numCols):
            assert(isinstance(rowDataTuple[idex],(bytes,str,int))), 'One or both data elements are not strings or numbers.'

        self.rowDataTupleTruncated = tuple(rowDataTuple[:self.numCols])

        if (self.rowDataTupleTruncated not in self.entriesList):

            if (not self.haveEntries):

                self.DeleteAllItems()

            self.Append(self.rowDataTupleTruncated)

            self.entriesList.append(self.rowDataTupleTruncated)

            self.numEntries +=1

            self.haveEntries = True

            self.Autosize()

    def Autosize(self):

        for colIndex in [1,2,3]:

            col_width = self.GetColumnWidth(colIndex)

            self.SetColumnWidth( colIndex, wx.LIST_AUTOSIZE)

            ColMaxWid = self.GetClientSize()[0]/2

            input_width = self.GetColumnWidth( colIndex)
            reasonableWid = max( col_width, input_width)
            finalWid = min(reasonableWid, ColMaxWid)
            self.SetColumnWidth( colIndex, reasonableWid)



class FilePanel(wx.Panel):

    def __init__(self, parent, label = 'default title'):

        super(FilePanel, self).__init__(parent = parent, style = wx.SIMPLE_BORDER)

        self.listctrl = FileCtrl(self, -1,style = wx.LC_REPORT|wx.BORDER_SUNKEN)
        self.SetBackgroundColour(wx.RED)

        #####Column################
        self.listctrl.InsertColumn(0,'File Path')
        self.listctrl.InsertColumn(1, 'File Name')
        self.listctrl.InsertColumn(2,'File Type')
        self.listctrl.InsertColumn(3, 'Number of Columns')
        # self.listctrl.InsertColumn(4, 'Record Number')
    

        #####Default Message#######
        helpTextTuple = (' '*40, 'Drop Files and Folders Here',' '*len('File Type')*2
                        ,' '*len('Number of Columns  ')*2)
        self.listctrl.Append(helpTextTuple)
        self.listctrl.SetColumnWidth(0, wx.LIST_AUTOSIZE)
        self.listctrl.SetColumnWidth(1, wx.LIST_AUTOSIZE)
        self.listctrl.SetColumnWidth(2, wx.LIST_AUTOSIZE)
        self.listctrl.SetColumnWidth(3, wx.LIST_AUTOSIZE)
        #####Layout################

        layout_vert = wx.BoxSizer(wx.VERTICAL)
        layout_horz = wx.BoxSizer(wx.HORIZONTAL)

        layout_vert.AddSpacer(10)
        layout_vert.Add(self.listctrl,flag = wx.EXPAND, proportion = 1)
        layout_vert.AddSpacer(10)

        layout_horz.AddSpacer(10)
        layout_horz.Add(layout_vert, flag = wx.EXPAND, proportion = 1)
        layout_horz.AddSpacer(10)

        self.SetSizer(layout_horz)


    