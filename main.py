from tkinter import Tk, Frame

from settings import Settings
from welcome_screen import WelcomeScreen
from difficulty_screen import DifficultyScreen

class Wordle:    
    def __init__(self, master):
        self.master = master
        self.settings = Settings()

        self.master.title('Wordle')
        self.master.geometry(f'{self.settings.screen_width}x{self.settings.screen_height}')
        self.master.resizable(False, False)

        self.container = Frame(self.master)
        self.container.pack()

        self.show_welcome_screen()

    def show_welcome_screen(self):
        for widget in self.container.winfo_children():
            widget.pack_forget()
       
        self.welcome_screen = WelcomeScreen(self.container, self.show_difficulty_screen)

    def show_difficulty_screen(self):
        for widget in self.container.winfo_children():
            widget.pack_forget()
       
        self.difficulty_screen = DifficultyScreen(self.container, self.show_welcome_screen)

if __name__ == "__main__":
    root = Tk()
    game = Wordle(root)
    root.mainloop()
