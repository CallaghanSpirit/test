import wx
app = wx.App()

frame = wx.Frame(None, title = 'Hello World')
frame.Show()
frame.Move(-1,-1)

app.MainLoop()