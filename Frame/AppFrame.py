import wx
import pyodbc
from BasicClass import FileLIstCtrl
from BasicClass import Button as BT
from Frame import Connect
from wx.lib.pubsub import pub


class AppFrame(wx.Frame):
    '''
    Main Frame

    '''


    def __init__(self, title = 'Demo'):
    
        super(AppFrame, self).__init__(parent = None, title = title, size = (800,600))

        panel = wx.Panel(self)
        panel.SetBackgroundColour(wx.WHITE)
        pub.subscribe(self.OnListen, 'GetServerInfo')

        self.filectrl = FileLIstCtrl.FilePanel(panel, label= 'test')

        # self.btn_pnl = BtnPnl(panel,connect = self.onConnect)
        self.btn_pnl = BT.ButtonPanel(panel, ButtonName= 'Connect SQL', onButtonHandlers=self.onConnect)
        # self.btn_pnl.Bind(wx.EVT_LEFT_DOWN, )
        
        #######Layout#######

        layout_horz = wx.BoxSizer(wx.HORIZONTAL)
        layout_vert = wx.BoxSizer(wx.VERTICAL)

        layout_horz.Add(self.filectrl,flag = wx.EXPAND, proportion = 1, border=10)
        layout_horz.AddSpacer(10)
        layout_horz.Add(self.btn_pnl, flag=wx.RIGHT| wx.EXPAND, border=8)


        layout_vert.AddSpacer(10)
        layout_vert.Add(layout_horz, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, proportion = 1,border=10)
        layout_vert.AddSpacer(10)

        panel.SetSizerAndFit(layout_vert)
        self.Show()
    
    def onConnect(self,event):

        Connect_frame = Connect.ConnectFrame()
        Connect_frame.Show()
        

    def OnListen(self,Driver,Server,Database,ConnectType,ConnectFlag):
    
        self.Driver = Driver
        self.Server = Server
        self.Database = Database
        self.ConnectType = ConnectType
        self.ConnectFlag = ConnectFlag


                        
        



class BtnPnl(wx.Panel):

    def __init__(self,parent = None, connect = None):
    
        super(BtnPnl, self).__init__(parent = parent, connect = connect)

        ConnectBtn = wx.Button(self, label= 'Connect SQL')
        ConnectBtn.Bind(wx.EVT_LEFT_DOWN, connect)


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


