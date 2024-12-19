#wxpython
import wx
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
    
class TestFrame5(wx.Frame):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw,)
        
        toolbar = self.CreateToolBar()
        br_quit = toolbar.AddTool(wx.ID_ANY, "Выход", wx.Bitmap('op-project/exit.png'))
        toolbar.Realize()

        self.Bind(wx.EVT_TOOL, self.onQuit, br_quit)


    def onQuit(self, event):
        dlg = wx.TextEntryDialog(self, 'Введите имя:', "Ввод данных...", "noname")
        res = dlg.ShowModal()
        if res == wx.ID_OK:
            print(dlg.GetValue())  


class MyDlg(wx.Dialog):
    def __init__(self,parent,  *args, **kw):
        super().__init__(parent, *args, **kw)

        self.parent = parent

class TestFrame6(wx.Frame):
    def __init__(self, *args, **kw):
          super().__init__(*args, **kw, size=(731,385))

          toolbar = self.CreateToolBar()
          br_quit = toolbar.AddTool(wx.ID_ANY, 'Выход', wx.Bitmap("op-project/exit.png"))
          dialog = toolbar.AddTool(wx.ID_ANY, 'Диалог', wx.Bitmap("op-project/sound.png"))
          toolbar.Realize()

          self.Bind(wx.EVT_TOOL, self.OnQuit, br_quit)
          self.Bind(wx.EVT_TOOL, self.onDialog, dialog)
    
    def onDialog(self, event):
        with MyDlg(self, title='Мой диалог...') as dlg:
           res = dlg.ShowModal()




    def OnQuit(self, event):
        self.Close() 
      
class Witgets(wx.Frame):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw, size=(731,500))
        self.B_RED = 1
        self.B_GREEN = 2
        self.B_BLUE = 3
        self.sb = self.CreateStatusBar()
        self.sb.SetStatusText("Текст в статусной скроке")

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        panel.SetSizer(vbox)

        st = wx.StaticText(panel, label='Адрес: ')
        vbox.Add(st, flag=wx.ALL, border=10)

        inp = wx.TextCtrl(panel, value="г. Москва")
        vbox.Add(inp, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, border=10)

        vbox.Add(wx.StaticLine(panel), flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)

        rtb = wx.ToggleButton(panel, id=self.B_RED, label='red')
        gtb = wx.ToggleButton(panel, id=self.B_GREEN, label='green')
        btb = wx.ToggleButton(panel, id=self.B_BLUE, label='blue')

        self.col = wx.Colour(0, 0, 0)
        self.pn = wx.Panel(panel)
        self.pn.SetBackgroundColour(self.col.GetAsString())

        vb1 = wx.GridBagSizer(10, 10)
        vb1.Add(rtb, (0,0))
        vb1.Add(gtb, (1,0))
        vb1.Add(btb, (2,0))
        vb1.Add(self.pn, (0,1), (3,1), flag=wx.EXPAND)
        vb1.AddGrowableCol(1)

        vbox.Add(vb1, flag=wx.EXPAND | wx.ALL, border=10)

        rtb.Bind(wx.EVT_TOGGLEBUTTON, self.onToggle)
        gtb.Bind(wx.EVT_TOGGLEBUTTON, self.onToggle)
        btb.Bind(wx.EVT_TOGGLEBUTTON, self.onToggle)

        vbox.Add(wx.StaticLine(panel), flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)

        pn2=wx.Panel(panel)
        wx.StaticBox(pn2, label="Ваш пол", size=(150, 50))
        rd1 = wx.RadioButton(pn2, label='Муж', pos=(10, 20), style=wx.RB_GROUP)
        rd2 = wx.RadioButton(pn2, label='Жен', pos=(100, 20))

        vbox2=wx.BoxSizer(wx.HORIZONTAL)
        vbox2.Add(pn2)

        agree = wx.CheckBox(panel, label='Согласен на обработку')
        agree.SetValue(True)

        vbox2.Add(agree, flag=wx.LEFT | wx.TOP, border=20)

        links = ['телефон', 'e-mail', 'skype']
        cb = wx.ComboBox(panel, choices=links, style=wx.CB_READONLY)
        cb.SetSelection(0)

        vbox2.Add(cb, flag=wx.LEFT | wx.TOP, border=15)
        
        sc = wx.SpinCtrl(panel, value='0', min=-100, max=100)
        vbox2.Add(sc, flag=wx.LEFT | wx.TOP, border=15)

        vbox.Add(vbox2, flag=wx.EXPAND | wx.ALL, border=10)

        self.gauge = wx.Gauge(panel, range=100)
        vbox.Add(self.gauge, flag=wx.EXPAND | wx.ALL, border=10)

        bStart = wx.Button(panel, label='Cтарт')
        bStop  = wx.Button(panel, label='Cтоп')

        hbox3 = wx.BoxSizer()
        hbox3.AddMany([(bStart, 0, wx.LEFT | wx.RIGHT, 10), (bStop, 0, wx.LEFT |wx.RIGHT | wx.BOTTOM, 10)])

        vbox.Add(hbox3, flag=wx.ALIGN_CENTER)

        bStart.Bind(wx.EVT_BUTTON, self.onStart)
        bStop.Bind(wx.EVT_BUTTON, self.onStop)

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)

        self.count = 0

        sld = wx.Slider(panel, value=200, minValue=150, maxValue=500, style=wx.SL_HORIZONTAL)
        vbox.Add(sld, flag = wx.EXPAND| wx.ALL, border=10)

        sld.Bind(wx.EVT_SCROLL, self.OnSliderScroll)

    def OnSliderScroll(self, e):
        val = e.GetEventObject().GetValue()
        self.sb.SetStatusText('Slider: '+ str(val))    
        

    def OnTimer(self, e):
        self.count = self.count + 1 
        self.gauge.SetValue(self.count)

        if self.count >= 100:
            self.timer.Stop()

    
    def onStart(self, e):
        if self.count > 100:
            return 
        
        self.timer.Start(100)

    def onStop(self, e):
       self.timer.Stop()
       self.count = 0
 
    def onToggle(self, event):
        btn = event.GetEventObject()
        val = 255 if btn.GetValue() else 0
        id = btn.GetId()

        r = self.col.Red()
        g = self.col.Green()
        b = self.col.Blue()

        match id:
            case self.B_RED:
                self.col.Set(val, g, b)
            case self.B_BLUE:
                self.col.Set(r, g, val)
            case self.B_GREEN:
                self.col.Set(r, val, b)

        self.pn.SetBackgroundColour(self.col)
        self.pn.Refresh()

class Widgets2(wx.Frame):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw, size=(1000,600))

        tabs = wx.Notebook(self, id=wx.ID_ANY)
        splitter = wx.SplitterWindow(tabs, wx.ID_ANY, style=wx.SP_LIVE_UPDATE)

        self.urls = ['op-project/htm/1_1.html']
        listbox = wx.ListBox(splitter, choices=self.urls)

        self.htmlwin = wx.html.HtmlWindow(splitter, wx.ID_ANY, style=wx.NO_BORDER)
        self.htmlwin.SetStandardFonts(12)
        self.htmlwin.LoadPage(self.urls[0])

        splitter.SplitVertically(listbox, listbox)
        splitter.SetMinimumPaneSize(200)

        tabs.InsertPage(0,splitter, "Главная", select=True)
        
        
class Graphics(wx.Frame):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw, size=(600, 600))

        self.btm = wx.Bitmap(wx.GetDisplaySize())
        self.btmDC = wx.MemoryDC()
        self.btmDC.SelectObject(self.btm)

        self.Bind(wx.EVT_PAINT, self.onDraw)

    def onDraw(self, e):
        dc = wx.PaintDC(self)
        dc.DrawBitmap(wx.Bitmap('op-project/Рисунок1.jpg'), (0, 0))



app = wx.App()


test_frame=TestFrame(None, title='Test', style=wx.DEFAULT_FRAME_STYLE)
# test_frame2.Show()

test_frame2=TestFrame2(None, title='Test2', style=wx.DEFAULT_FRAME_STYLE)
# test_frame2.Show()

test_frame3=TestFrame3(None, title='Test3', style=wx.DEFAULT_FRAME_STYLE)
# test_frame3.Show()

test_frame4=TestFrame4(None, title='Test4', style=wx.DEFAULT_FRAME_STYLE)
# test_frame4.Show()

test_frame5=TestFrame5(None, title='Test5', style=wx.DEFAULT_FRAME_STYLE)
# test_frame5.Show()

test_frame6=TestFrame6(None, title='Test6', style=wx.DEFAULT_FRAME_STYLE)
# test_frame6.Show()

widgets=Witgets(None, title='widgets', style=wx.DEFAULT_FRAME_STYLE)
# widgets.Show()

widgets2=Widgets2(None, title='widgets', style=wx.DEFAULT_FRAME_STYLE)
# widgets2.Show()

graphics=Graphics(None, title='graphics', style=wx.DEFAULT_FRAME_STYLE)
graphics.Show()