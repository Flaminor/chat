import tkinter as tk

class Application(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("chat")
        self.geometry("400x700")


if __name__ == "__main__":
    app =Application()
    app.mainloop()
