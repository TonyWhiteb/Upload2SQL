import wx

# from wx.lib.pubsub import pub





class ButtonPanel(wx.Panel):



    def __init__(self,parent = None, id = -1,ButtonName = None, onButtonHandlers = None):



        super(ButtonPanel, self).__init__(parent = parent , id = id)
        self.SetBackgroundColour(wx.BLUE)
        

        # pub.subscribe(self.OnListen, 'GetSelectCol')


        self.myButton = wx.Button(self,-1,label = ButtonName)



        self.myButton.Bind(wx.EVT_LEFT_DOWN, onButtonHandlers)

#################Layout#######################
        VertSizer= wx.BoxSizer(wx.VERTICAL)
        HorzSizer= wx.BoxSizer(wx.HORIZONTAL)

        VertSizer.AddSpacer(10)
        VertSizer.Add(self.myButton)
        VertSizer.AddSpacer(10)

        HorzSizer.AddSpacer(5)
        HorzSizer.Add(VertSizer)
        HorzSizer.AddSpacer(5)

        self.SetSizer(HorzSizer)

        self.Layout()

        # def SetLabel(self, NewLabel):
        #     self.myButton.SetLabel(NewLabel)