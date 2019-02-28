import wx

class FileCtrl(wx.ListCtrl):
    
    def __init__(self, *args, **kwargs):
    
        super(FileCtrl, self).__init__(*args, **kwargs)



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


    