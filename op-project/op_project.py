import wx
from exsel_test import column_data
BUTTON1 = wx.NewIdRef()
BUTTON2 = wx.NewIdRef()

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
        
        self.panel = wx.Panel(self)
        vbox = wx.BoxSizer()

      

        tx1 = wx.StaticText(self.panel,label=column_data())
        
         
        img1 = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap("op-project/Рисунок1.jpg")) 
    

        
        vbox.Add(img1)
        vbox.Add(tx1)
        self.panel.SetSizer(vbox)

     


        # menubar.Append(filemenu,'File')



    
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
        
        tc = wx.TextCtrl(panel)
        vbox.Add(tc, flag=wx.EXPAND | wx.LEFT | wx.TOP | wx.RIGHT, border=10 )

        gbox = wx.GridSizer(5,4,5,5)
        
        gbox.AddMany([(wx.Button(panel,label='Cls'),wx.ID_ANY,wx.EXPAND,),
              (wx.Button(panel,label='Bck'),wx.ID_ANY,wx.EXPAND,),
              (wx.StaticText(panel ,wx.EXPAND,)),
              (wx.Button(panel,label='Close'),wx.ID_ANY,wx.EXPAND,),
              (wx.Button(panel,label='7'),wx.ID_ANY,wx.EXPAND,),
              (wx.Button(panel,label='8'),wx.ID_ANY,wx.EXPAND,),
              (wx.Button(panel,label='9'),wx.ID_ANY,wx.EXPAND,),
              (wx.Button(panel,label='/'),wx.ID_ANY,wx.EXPAND,),
              (wx.Button(panel,label='4'),wx.ID_ANY,wx.EXPAND,),
              (wx.Button(panel,label='5'),wx.ID_ANY,wx.EXPAND,),
              (wx.Button(panel,label='6'),wx.ID_ANY,wx.EXPAND,),
              (wx.Button(panel,label='*'),wx.ID_ANY,wx.EXPAND,),
              (wx.Button(panel,label='1'),wx.ID_ANY,wx.EXPAND,),
              (wx.Button(panel,label='2'),wx.ID_ANY,wx.EXPAND,),
              (wx.Button(panel,label='3'),wx.ID_ANY,wx.EXPAND,),
              (wx.Button(panel,label='-'),wx.ID_ANY,wx.EXPAND,),
              (wx.Button(panel,label='0'),wx.ID_ANY,wx.EXPAND,),
              (wx.Button(panel,label='.'),wx.ID_ANY,wx.EXPAND,),
              (wx.Button(panel,label='='),wx.ID_ANY,wx.EXPAND,),
              (wx.Button(panel,label='+'),wx.ID_ANY,wx.EXPAND,),])

        vbox.Add(gbox, proportion=1, flag=wx.EXPAND | wx.ALL , border=10)

        panel.SetSizer(vbox) 

class TestFrame2(wx.Frame):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw, size=(731,385))

        self.panel = wx.Panel(self)
        vbox = wx.BoxSizer()
        
        gr = wx.GridBagSizer(5, 5)
        text = wx.StaticText(self.panel, label='Email:')
        gr.Add(text, pos=(0,0), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=5 )

        tc = wx.TextCtrl(self.panel)
        gr.Add(tc, pos=(1, 0), span=(1,5), flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=5)
        
        buttom1 = wx.Button(self.panel, label='Восстановить', size=(120,28))
        buttom2 = wx.Button(self.panel, label='Отмена',size=(90,28))

        gr.Add(buttom1, pos=(3,3))
        gr.Add(buttom2, pos=(3,4), flag=wx.RIGHT | wx.BOTTOM, border=10)
        
        gr.AddGrowableCol(1)
        gr.AddGrowableRow(2)


        self.panel.SetSizer(gr)

        # fb.AddGrowableCol(1,1)
        # fb.AddGrowableRow(3,1)
        # vbox.Add(fb,proportion=1, flag=wx.EXPAND | wx.ALL, border=10)

class TestFrame3(wx.Frame):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw, size=(731,385))

        self.panel = wx.Panel(self)
        vbox = wx.BoxSizer()
        
        fr = wx.FlexGridSizer(5,5,10,10)

        btn1 = wx.Button(self.panel ,id=BUTTON1.GetId(), label='Кнопка 1', size=(50,50) )

        btn1.Bind(wx.EVT_BUTTON, self.onButton)
        self.panel.Bind(wx.EVT_BUTTON, self.onButtonPanel)
        self.Bind(wx.EVT_BUTTON, self.onButtonFrame)

        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

        self.panel.Unbind(wx.EVT_BUTTON)
        
        

        fr.AddMany([(btn1,wx.ID_ANY,wx.EXPAND),
                    
        ])

        vbox.Add(fr)
        self.panel.SetSizer(vbox)
        print(btn1.GetId())

    
    def onButton(self, event):
        print("Уровень кнопки")
        event.Skip()

    def onButtonPanel(self, event):
        print("Уровень панели")
        event.Skip()

    def onButtonFrame(self, event):
        print("Уровень окна")

    def OnCloseWindow(self, event):
        dial = wx.MessageDialog(None, 'Вы точно хотите выйти?', 'Вопрос', wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        
        ret = dial.ShowModal()
        if ret == wx.ID_YES:
            self.Destroy()
        else:
            event.Veto()

class TestFrame4(wx.Frame):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw, size=(731,385))

        self.panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        self.panel.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        self.panel.Bind(wx.EVT_KEY_UP, self.OnKeyUp)
   
        self.panel.SetSizer(vbox)
    
    def OnKeyDown(self, event):
        key = event.GetKeyCode()
        if key == wx.WXK_ESCAPE:
            ret = wx.MessageBox('Выйти надо?', 'Вопрос', wx.YES_NO | wx.NO_DEFAULT, self)

            if ret == wx.YES:
                self.Close()

    def OnKeyUp(self, event):
        print('ОтпустилиКнопку')
    

app = wx.App()


test_frame=TestFrame(None, title='Test', style=wx.DEFAULT_FRAME_STYLE)
# test_frame2.Show()

test_frame2=TestFrame2(None, title='Test2', style=wx.DEFAULT_FRAME_STYLE)
# test_frame2.Show()

test_frame3=TestFrame3(None, title='Test3', style=wx.DEFAULT_FRAME_STYLE)
# test_frame3.Show()

test_frame4=TestFrame4(None, title='Test3', style=wx.DEFAULT_FRAME_STYLE)
test_frame4.Show()


frame = MainFrame(None, title = 'Мотивация', style = wx.DEFAULT_FRAME_STYLE )
# frame.Show()
frame.Move(-1,-1)

app.MainLoop()