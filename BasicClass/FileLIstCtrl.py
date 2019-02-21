import wx

class FileCtrl(wx.ListCtrl):
    
    def __init__(self, *args, **kwargs):
    
        super(FileCtrl, self).__init__(*args, **kwargs)



class FilePanel(wx.Panel):

    def __init__(self, parent, label = 'default title', size= (100,200)):

        super(FilePanel, self).__init__(parent = parent, style = wx.SIMPLE_BORDER)

        self.listctrl = FileCtrl(self,size = size, style = wx.LC_REPORT)
        self.SetBackgroundColour(wx.RED)

        #####Layout################

        layout_vert = wx.BoxSizer(wx.VERTICAL)
        layout_horz = wx.BoxSizer(wx.HORIZONTAL)

        layout_vert.AddSpacer(10)
        layout_vert.Add(self.listctrl)
        layout_vert.AddSpacer(10)

        layout_horz.AddSpacer(10)
        layout_horz.Add(layout_vert)
        layout_horz.AddSpacer(10)

        self.SetSizer(layout_horz)


    