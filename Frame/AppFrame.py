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

        self.ConnectFlag = False
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
        # print(self.ConnectFlag)
        if self.ConnectFlag == True:
            self.btn_pnl.myButton.SetLabel(self.Database)
        print('done')
        # self.RunTime = RuntimeV
        # print(self.RunTime)


                        
        






