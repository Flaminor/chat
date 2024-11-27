import tkinter as tk

class Application(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("chat")
        self.geometry("400x700")
        self.champ()

    
    def champ(self): 
        self.entree = tk.Entry(self)
        self.entree.pack(fill = 'x',side= 'bottom')
        



if __name__ == "__main__" :

    app = Application()
    app.mainloop()
