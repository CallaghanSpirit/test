import wx
APP_EXIT = 1

class MyFrame(wx.MDIParentFrame):
    def  __init__(self, parent, title):
        super().__init__(parent, title = title)

        menubar = wx.MenuBar()
        filemenu = wx.Menu()

        filemenu.Append(wx.ID_EXIT, 'Новый\tCtrl+N', )
        filemenu.Append(wx.ID_EXIT, 'Открыть\tCtrl+O', )
        filemenu.Append(wx.ID_EXIT, 'Сохранить\tCtrl+S',)
        
        item = wx.MenuItem(filemenu, APP_EXIT, 'Выход\tCtrl+Q', 'Выход из приложения')
        item.SetBitmap(wx.Bitmap('op-project/exit.png'))
        filemenu.Append(item)
        # item = filemenu.Append(wx.ID_EXIT, 'Выход\tCtrl+Q', 'Выход из приложения')


        menubar.Append(filemenu,'File')

        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.onQuit, id=APP_EXIT)

    def onQuit(self, event):
        self.Close()


app = wx.App()

frame = MyFrame(None, title = 'Hello World')
frame.Show()
frame.Move(-1,-1)

app.MainLoop()