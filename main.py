from tkinter import Tk

from settings import Settings

class Wordle:    
    def __init__(self, master):
        self.master = master
        self.settings = Settings()

        self.master.title('Wordle')
        self.master.geometry(f'{self.settings.screen_width}x{self.settings.screen_height}')

if __name__ == "__main__":
    root = Tk()
    game = Wordle(root)
    root.mainloop()
