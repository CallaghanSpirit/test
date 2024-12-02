import wx
from exsel_test import column_data
APP_EXIT = 1
VIEW_STATUS = 2
VIEW_RGB = 3
VIEW_SRGB = 4
IT_MAX = 5

class AppContextMenu(wx.Menu):
    def __init__(self, parent):
        self.parent = parent
        super().__init__()


        it_min = self.Append(wx.ID_ANY, 'Минизировать')
        it_max = self.Append(wx.ID_ANY, 'Распахнуть')
        self.Bind(wx.EVT_MENU,self.onMinimize, it_min)
        self.Bind(wx.EVT_MENU,self.onMaximaze, it_max)
    
    def onMinimize(self,event):
        self.parent.Iconize()

    def onMaximaze(self,event):
        self.parent.Maximize() 

class MainFrame(wx.Frame):
    def  __init__(self, parent, style, title):
        super().__init__(parent, title = title, style = style, size=(731,385))
        
        panel = wx.Panel(self)
        vbox = wx.BoxSizer()

        text_box = wx.BoxSizer()

        tx1 = wx.StaticText(panel,label=column_data())
        text_box.Add(tx1)
         
        img1 = wx.StaticBitmap(panel, wx.ID_ANY, wx.Bitmap("op-project/Рисунок1.jpg")) 
        vbox.Add(text_box)

        
        vbox.Add(img1,wx.ID_ANY)
        panel.SetSizer(vbox)

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


        # menubar.Append(filemenu,'File')

        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_RIGHT_DOWN, self.on_right_click)
        self.Bind(wx.EVT_MENU, self.onQuit, id=APP_EXIT)

    
        self.ctx = AppContextMenu(self)

        # toolbar = self.CreateToolBar()
        # br_quit = toolbar.AddTool(APP_EXIT,"Выход", wx.Bitmap("op-project/exit.png"))
        # toolbar.Realize()
        
       

   
    def onStatus(self, event):
         if self.vStatus.IsChecked():
            print('Показать статусную строку')
         else:
            print("Скрыть статусную строку ")
    
    def on_right_click(self, event):
        # Показываем контекстное меню
        self.PopupMenu(self.ctx, event.GetPosition()) #Mouse ivent


    def onQuit(self, event):
        self.Close()


class TestFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw, size=(731,385))

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        font = wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT)
        font.SetPointSize(12)
        panel.SetFont(font)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(panel, label='Путь к файлу:')
        tc = wx.TextCtrl(panel)

        hbox.Add(st1, flag=wx.RIGHT , border=8)
        hbox.Add(tc, proportion=1)

        vbox.Add(hbox, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP , border=10)
        
        st2 = wx.StaticText(panel, label='Содержимое файла')
        vbox.Add(st2, flag=wx.EXPAND | wx.ALL, border=10)

        tc2 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        vbox.Add(tc2, proportion=1, flag=wx.LEFT | wx.RIGHT | wx.BOTTOM | wx.EXPAND, border=10)
        
        btnOK = wx.Button(panel, label='Да', size=(70,30))
        btnCN = wx.Button(panel, label='Отмена', size=(70,30))
        
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2.Add(btnOK, flag=wx.LEFT, border=10)
        hbox2.Add(btnCN, flag=wx.LEFT, border=10)

        vbox.Add(hbox2, flag=wx.ALIGN_RIGHT | wx.BOTTOM | wx.RIGHT, border=10)

        panel.SetSizer(vbox)

app = wx.App()


frame2=TestFrame(None, title = 'Test', style = wx.DEFAULT_FRAME_STYLE)
frame2.Show()

frame = MainFrame(None, title = 'Мотивация', style = wx.DEFAULT_FRAME_STYLE )
frame.Show()
frame.Move(-1,-1)

app.MainLoop()