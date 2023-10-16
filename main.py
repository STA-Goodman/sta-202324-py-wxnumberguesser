# Thomas Kahler, Andy Kang
# 2023-10-16
# Number guesser in wxPython

import wx

# Declaring and setting up the window
class MainWindow(wx.Frame):
    def __init__(self, parent=None, title="Number Guessing Game"):
        wx.Frame.__init__(self, parent, title=title, size=(240, 144))

        # Create a panel and sizer so we can put widgets in places
        panel = wx.Panel(self)
        sizer = wx.GridSizer(2, 2, 10, 10)
        
        # Create widgets
        guessPanel = wx.Panel(panel, size=(240, 40))
        guessSizer = wx.GridSizer(2, 2, 10, 10)
        guessLabel = wx.StaticText(parent=guessPanel, label="Your guess: ")
        guessEntry = wx.TextCtrl(parent=guessPanel, size=(100,20))
        guessSizer.Add(guessPanel, 0, wx.CENTER)
        guessButton = wx.Button(panel, label="Guess", pos=(0, 90))

        # Show widget
        sizer.Add(guessSizer)
        sizer.Add(panel, wx.CENTER)

        self.Show(True)
    
app = wx.App(False)
frame = MainWindow()

frame.Show(True)
app.MainLoop()