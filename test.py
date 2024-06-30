s = '1'

try:
    my_shit = float(s)
    print('hi')
except ValueError:
    print("Нет")

print('hi2')


import tkinter as tk


class Fullscreen_Window:

    def __init__(self):
        self.tk = tk.Tk()
        self.tk.config(bg='black')
        self.state = False
        self.tk.bind("<F11>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.end_fullscreen)

    def toggle_fullscreen(self, event=None):
        self.state = not self.state
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.tk.attributes("-fullscreen", False)
        return "break"


if __name__ == '__main__':
    w = Fullscreen_Window()
    w.tk.mainloop()

