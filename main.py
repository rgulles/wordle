from tkinter import Tk

class Wordle:    
    def __init__(self, master):
        self.master = master
        
        self.master.title('Wordle')
        self.master.geometry('600x700')

if __name__ == "__main__":
    root = Tk()
    game = Wordle(root)
    root.mainloop()
