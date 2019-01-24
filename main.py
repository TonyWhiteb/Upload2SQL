from Frame import AppFrame
import wx
#from frame_test import AppFrame





if __name__ == '__main__':

    app = wx.App(False)

    frame = AppFrame.AppFrame()

    app.MainLoop()