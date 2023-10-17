# Thomas Kahler, Andy Kang
# 2023-10-16
# Number guesser in wxPython

import wx

# Declaring and setting up the window
class MainWindow(wx.Frame):
    def __init__(self, parent=None, title="Number Guessing Game"):
        # "super" calling the creation of a frame
        super(MainWindow, self).__init__(parent, title=title, size=(240, 144))
        self.InitUI()
        self.Center()
        self.Show()
        self.Fit()
        
    def InitUI(self):
        # Window and widget placement objects
        mainPanel = wx.Panel(self)
        mainSizer = wx.FlexGridSizer(rows=2, cols=1, hgap=10, vgap=10)
        guessPanel = wx.Panel(mainPanel)
        guessSizer = wx.GridSizer(rows=1, cols=2, vgap=10, hgap=10)
        
        mainPanel.SetSizer(mainSizer)
        guessPanel.SetSizer(guessSizer)

        # Widget objects
        guessLabel = wx.StaticText(parent=mainPanel, label="Your guess: ")
        guessEntry = wx.TextCtrl(mainPanel, -1)

        # Add widgets to 
        mainSizer.Add(guessSizer)
        guessSizer.Add(guessLabel, 0, wx.ALIGN_CENTER, 0)
        guessSizer.Add(guessEntry, 0, wx.ALIGN_CENTER, 0)
    
app = wx.App(False)
frame = MainWindow()

frame.Show(True)
app.MainLoop()