import wx
import pyodbc
from wx.lib.pubsub import pub

class ConnectFrame(wx.Frame):
    '''Connection Frame
    
    '''
    def __init__(self, title = 'Connection', size = (300,350)):
        '''__init__ method
        
        Keyword Arguments:
            title {str} -- title name
        '''
        super(ConnectFrame,self).__init__( parent = None, size = size, title = title)
        self.Default_Driver = 'SQL Server Native Client 11.0'
        self.Default_Type = 'yes'

        panel = wx.Panel(self,style = wx.ALIGN_CENTER)
        Driver_Label = wx.StaticText(panel, label = 'Driver :')
        self.Driver_Box = MyChoice(panel,self.Default_Driver,size = (150,25))
        Server_Label = wx.StaticText(panel, label = 'Server :')
        self.Server_Box = wx.TextCtrl(panel,size =(150,25))
        Database_Label = wx.StaticText(panel, label = 'Database :')
        self.Database_Box= wx.TextCtrl(panel, size = (150,25))
        ConnectType_Label = wx.StaticText(panel, label = 'ConnectType :')
        self.ConnectType_Box = MyChoice(panel,self.Default_Type,['yes','no'],size = (150,25))

        Connect_btn = wx.Button(panel,  label = 'Connect')
        Connect_btn.Bind(wx.EVT_LEFT_DOWN, self.onConnect)

        ######Layout###########

        layout_horz = wx.BoxSizer(wx.HORIZONTAL)
        layout_vert = wx.BoxSizer(wx.VERTICAL)
        
        layout_vert.AddSpacer(10)
        layout_vert.Add(Driver_Label)
        layout_vert.AddSpacer(10)
        layout_vert.Add(self.Driver_Box)
        layout_vert.AddSpacer(10)
        layout_vert.Add(Server_Label)
        layout_vert.AddSpacer(10)
        layout_vert.Add(self.Server_Box)
        layout_vert.AddSpacer(10)
        layout_vert.Add(Database_Label)
        layout_vert.AddSpacer(10)
        layout_vert.Add(self.Database_Box)
        layout_vert.AddSpacer(10)
        layout_vert.Add(ConnectType_Label)
        layout_vert.AddSpacer(10)
        layout_vert.Add(self.ConnectType_Box)
        
        layout_vert.AddSpacer(20)
        layout_vert.Add(Connect_btn,0,wx.CENTER)
        layout_vert.AddSpacer(10)
        
        layout_horz.AddStretchSpacer(prop=1)
        layout_horz.Add(layout_vert, 0, wx.CENTER)
        layout_horz.AddStretchSpacer(prop=1)

        panel.SetSizerAndFit(layout_horz)

        self.Show()
    # def GetDriver(self):
    #     return self.Driver_Box.GetCurrentSelection()
    # def GetServer(self):
    #     return self.Server_Box.GetValue()

    # def GetConnectType(self):
    #     return self.ConnectType_Box.GetString(self.ConnectType_Box.GetCurrentSelection())
    def onConnect(self,event):
        '''Connect Button
        
        '''
        ConnectFlag = False
        Driver = self.Driver_Box.GetDriver()
        Server = self.Server_Box.GetValue()
        Database = self.Database_Box.GetValue()
        ConnectType = self.ConnectType_Box.GetConnectType()
        
        try:
            cnxn = pyodbc.connect("Driver={%s};"
                                  "Server=%s;"
                                  "Database=%s;"
                                  "Trusted_Connection=%s;" % (Driver, Server, Database, ConnectType))
        except pyodbc.Error as ex:

            error_msg = ex.args[1]
            self.Warn(message = error_msg)
        ConnectFlag = True
        pub.sendMessage('GetServerInfo',Driver = Driver, Server = Server, Database = Database, ConnectType = ConnectType, ConnectFlag = ConnectFlag)
        self.Close()


    
    def Warn(self, message, caption = 'Warning!'):

        dlg = wx.MessageDialog(self, message, caption, wx.OK | wx.ICON_WARNING)

        dlg.ShowModal()

        dlg.Destroy() 

class MyChoice(wx.ComboBox):
    def __init__(self, parent,value,choices = [],size = (100,20)):
    
        super().__init__(parent = parent, value = value ,choices = choices,size = size )

        super().SetEditable(False)

    def GetDriver(self):
        if self.GetCurrentSelection() == -1:
            GetDriver = 'SQL Server Native Client 11.0'
        else:
            GetDriver = self.GetString(self.GetCurrentSelection())
        return GetDriver
    
    def GetConnectType(self):
        if self.GetCurrentSelection() == -1:
            GetConnectType = 'yes'
        else:
            GetConnectType = self.GetString(self.GetCurrentSelection())
        return GetConnectType


        


        



         


if __name__ == '__main__':

    app = wx.App(False)

    frame = ConnectFrame()

    app.MainLoop()