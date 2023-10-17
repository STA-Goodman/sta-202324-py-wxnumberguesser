# Thomas Kahler, Andy Kang
# 2023-10-16
# Number guesser in wxPython

import wx

from random import randint

# Declaring and setting up the window
class MainWindow(wx.Frame):
    def __init__(self, parent=None, title="Number Guessing Game"):
        # "super" calling the creation of a frame
        super(MainWindow, self).__init__(parent, title=title, size=(240, 160))

        # Create values for game
        self.__randomNumber = self.setRandomNumber(100)
        self.__attempts = 10
        self.__guessing = True

        # Show window
        self.initUI()
        self.Center()
        self.Show()
        self.Fit()

        
    def initUI(self):
        # Window and widget placement objects
        self.mainPanel = wx.Panel(self)
        self.mainSizer = wx.FlexGridSizer(rows=4, cols=1, hgap=10, vgap=10)
        self.guessPanel = wx.Panel(self.mainPanel)
        self.guessSizer = wx.GridSizer(rows=1, cols=2, vgap=10, hgap=10)

        self.mainPanel.SetSizer(self.mainSizer)
        self.guessPanel.SetSizer(self.guessSizer)

        # Widget objects
        self.guessLabel = wx.StaticText(parent=self.mainPanel, label="Your guess: ")
        self.guessEntry = wx.TextCtrl(self.mainPanel, -1)

        self.guessButton = wx.Button(parent=self.mainPanel, label="Guess")
        self.guessButton.Bind(event=wx.EVT_BUTTON, handler=self.getInput)

        self.statusLabel = wx.StaticText(parent=self.mainPanel, label="A number has been chosen")

        self.attemptsLabel = wx.StaticText(parent=self.mainPanel, label="Attempts: " + str(self.__attempts))

        # Add widgets to panels
        self.mainSizer.Add(self.guessSizer)
        self.guessSizer.Add(self.guessLabel, 0, wx.ALIGN_CENTER, 0)
        self.guessSizer.Add(self.guessEntry, 0, wx.ALIGN_CENTER, 0)
        self.mainSizer.Add(self.guessButton, 0, wx.ALIGN_CENTER, 0)
        self.mainSizer.Add(self.statusLabel, 0, wx.ALIGN_CENTER, 0)
        self.mainSizer.Add(self.attemptsLabel, 0, wx.ALIGN_CENTER, 0)

    def getInput(self, event):
        guessInput = self.guessEntry.GetValue()
        
        # Should happen if guess contains non-numeric characters
        try:
            guessInput = int(guessInput)
        except ValueError:
            self.statusLabel.SetLabelText("Invalid input, try again.")
            return None
        
        # Invalid guesses, ordered in terms of precedence
        if self.__guessing == False:
            self.statusLabel.SetLabelText("You already won, try restarting.")
            return None
        
        if self.__attempts == 0:
            self.statusLabel.SetLabelText("You have no attempts left")
            return None     
           
        if guessInput < 0:
            self.statusLabel.SetLabelText("Your guess can't be negative")
            return None
        
        # Valid guesses
        if guessInput < self.__randomNumber:
            self.statusLabel.SetLabelText("Your guess is too low")
            self.decrementAttempts()

        if guessInput > self.__randomNumber:
            self.statusLabel.SetLabelText("Your guess is too high")
            self.decrementAttempts()

        if guessInput == self.__randomNumber:
            self.statusLabel.SetLabelText("You guessed correctly!")
            if self.__guessing:
                self.decrementAttempts()
            self.__guessing = False
        
    # Set a random number given any limit
    # A separate function is used for if someone wants to make a limit input
    def setRandomNumber(self, limit):
        return randint(0, limit)
    
    # Decrement attempts for each guess
    def decrementAttempts(self):
        self.__attempts -= 1
        self.attemptsLabel.SetLabelText("Attempts: " + str(self.__attempts))

def main():
    app = wx.App(False)
    frame = MainWindow()
    frame.Show()
    app.MainLoop()

main()