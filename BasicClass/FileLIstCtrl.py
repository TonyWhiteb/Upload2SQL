import wx

class FileCtrl(wx.ListCtrl):
    
    def __init__(self, *args, **kwargs):
    
        super(FileCtrl, self).__init__(*args, **kwargs)

        self.currRow = None
        
        self.Bind(wx.EVT_LEFT_DOWN, self.OnFindCurrentRow)
        

    
    def OnFindCurrentRow(self,event):
        if (self.currRow is not None):
            self.Select(self.currRow, False)

        row,_ignoredFlags = self.HitTest(event.GetPosition())

        self.currRow = row
        self.Select(row)
    def OnRightDown(self,event):

        menu = wx.Menu()
        menuItem = menu.Append(-1, 'Delet This File')

        self.Bind(wx.EVT_MENU, self.OnDeleteRow, memuItem)
    def OnDeleteRow(self, event):

        if(self.currRow >= 0):

            assert(self.numEntries == len(self.entriesList))

            allSelectedRowData = self.GetAllSelectedRowData()

    def GetCurrRow(self):
        return self.currRow




class FilePanel(wx.Panel):

    def __init__(self, parent, label = 'default title'):

        super(FilePanel, self).__init__(parent = parent, style = wx.SIMPLE_BORDER)

        self.listctrl = FileCtrl(self, -1,style = wx.LC_REPORT)
        self.SetBackgroundColour(wx.RED)

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


    