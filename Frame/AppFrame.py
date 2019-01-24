import wx

from BasicClass import FileLIstCtrl


class AppFrame(wx.Frame):

    def __init__(self, title = 'Demo'):
    
        super(AppFrame, self).__init__(parent = None, title = title, size = (800,600))

        panel = wx.Panel(self)
        panel.SetBackgroundColour(wx.WHITE)

        self.filectrl = FileLIstCtrl.FilePanel(panel, label= 'test')

        self.btn_pnl = BtnPnl(panel)

        #######Layout#######

        layout_horz = wx.BoxSizer(wx.HORIZONTAL)
        layout_vert = wx.BoxSizer(wx.VERTICAL)

        layout_horz.AddSpacer(10)
        layout_horz.Add(self.filectrl)
        layout_horz.AddSpacer(10)
        layout_horz.Add(self.btn_pnl)
        layout_horz.AddSpacer(10)

        layout_vert.AddSpacer(10)
        layout_vert.Add(layout_horz)
        layout_vert.AddSpacer(10)

        panel.SetSizerAndFit(layout_vert)
        self.Show()



class BtnPnl(wx.Panel):

    def __init__(self, *args, **kwargs):
    
        super(BtnPnl, self).__init__(*args, **kwargs)

        ConnectBtn = wx.Button(self, label= 'Connect SQL')


#################Layout#######################
        VertSizer= wx.BoxSizer(wx.VERTICAL)
        HorzSizer= wx.BoxSizer(wx.HORIZONTAL)

        VertSizer.AddSpacer(10)
        VertSizer.Add(ConnectBtn)
        VertSizer.AddSpacer(10)

        HorzSizer.AddSpacer(5)
        HorzSizer.Add(VertSizer)
        HorzSizer.AddSpacer(5)

        self.SetSizer(HorzSizer)

        self.Layout()


