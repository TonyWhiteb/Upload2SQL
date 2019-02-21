import wx

variables = [i for i in dir(wx.ComboBox) if not callable(i)]
print(variables)

# help(wx.ComboBox)