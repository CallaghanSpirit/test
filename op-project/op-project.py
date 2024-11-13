import wx
APP_EXIT = 1
VIEW_STATUS = 2
VIEW_RGB = 3
VIEW_SRGB = 4
IT_MAX = 5

class MyFrame(wx.Frame):
    def  __init__(self, parent, title):
        super().__init__(parent, title = title)

        menubar = wx.MenuBar()
        filemenu = wx.Menu()

        expmenu = wx.Menu()
        expmenu.Append(wx.ID_ANY,"Экспорт изображения")
        expmenu.Append(wx.ID_ANY,"Экспорт видео")
        expmenu.Append(wx.ID_ANY,"Экспорт даннных")

        filemenu.Append(wx.ID_EXIT, 'Новый\tCtrl+N', )
        filemenu.Append(wx.ID_EXIT, 'Открыть\tCtrl+O', )
        filemenu.Append(wx.ID_EXIT, 'Сохранить\tCtrl+S',)
        filemenu.AppendSubMenu(expmenu, "&Экспорт")
        filemenu.AppendSeparator()
        
        item = wx.MenuItem(filemenu, APP_EXIT, 'Выход\tCtrl+Q', 'Выход из приложения')
        item.SetBitmap(wx.Bitmap('op-project/exit.png'))
        filemenu.Append(item)
        # item = filemenu.Append(wx.ID_EXIT, 'Выход\tCtrl+Q', 'Выход из приложения')


        menubar.Append(filemenu,'File')

        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_RIGHT_DOWN, self.on_right_click)
        self.Bind(wx.EVT_MENU, self.onQuit, id=APP_EXIT)

    
        self.ctx = wx.Menu()
        it_min = self.ctx.Append(wx.ID_ANY, 'Минизировать')
        it_max = self.ctx.Append(wx.ID_ANY, 'Распахнуть')


    def onStatus(self, event):
         if self.vStatus.IsChecked():
            print('Показать статусную строку')
         else:
            print("Скрыть статусную строку ")
    
    def on_right_click(self, event):
        # Показываем контекстное меню
        self.PopupMenu(self.ctx, event.GetPosition())


    def onQuit(self, event):
        self.Close()



app = wx.App()

frame = MyFrame(None, title = 'Hello World')
frame.Show()
frame.Move(-1,-1)

app.MainLoop()