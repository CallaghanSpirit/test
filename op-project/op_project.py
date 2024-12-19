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
        
        res = column_data()
        self.panel = wx.Panel(self)
        vbox = wx.BoxSizer()

        gbbox = wx.GridBagSizer(6,8)

       
        tx1 = wx.StaticText(self.panel,label=f"{res[0]}")
        tx2 = wx.StaticText(self.panel,label=f"{res[1]}")
        tx3 = wx.StaticText(self.panel,label=f"{res[2]}")
        tx4 = wx.StaticText(self.panel,label=f"{res[3]}")



        gbbox.Add(tx1, pos=(8,17), flag=wx.LEFT|wx.EXPAND, border=7)
        gbbox.Add(tx2, pos=(8,21), flag=wx.LEFT|wx.EXPAND, border=3)
        gbbox.Add(tx3, pos=(8,25), flag=wx.LEFT|wx.EXPAND, border=7)
        gbbox.Add(tx4, pos=(8,29), flag=wx.RIGHT|wx.EXPAND, border=7)


         
        self.img = wx.Bitmap("op-project/Рисунок1.jpg")
        
        
        vbox.Add(gbbox)
        self.panel.SetSizer(vbox)
        self.panel.Bind(wx.EVT_PAINT, self.OnPaint)
       

   
    def OnPaint(self, event):
        dc = wx.PaintDC(self.panel)
        dc.DrawBitmap(self.img, (0,0))


    def onQuit(self, event):
        self.Close()    
        
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

frame = MainFrame(None, title = 'Мотивация', style = wx.DEFAULT_FRAME_STYLE )
frame.Show()
frame.Move(-1,-1)

app.MainLoop()