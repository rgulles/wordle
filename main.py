from tkinter import Tk, Frame

from settings import Settings
from welcome_screen import WelcomeScreen

class Wordle:    
    def __init__(self, master):
        self.master = master
        self.settings = Settings()

        self.master.title('Wordle')
        self.master.geometry(f'{self.settings.screen_width}x{self.settings.screen_height}')
        self.master.resizable(False, False)

        self.container = Frame(self.master)
        self.container.pack()

        self.welcome_screen = WelcomeScreen(self.container)

if __name__ == "__main__":
    root = Tk()
    game = Wordle(root)
    root.mainloop()
