import tkinter as tk
from tkinter import ttk


class ChildPowerSet:
    def __init__(self, parent, width, height, theme, title='Подбор режимов',
                 resizable=(False, False), icon=None):
        # Создание дочернего окна поверх основного
        self.child_root = tk.Toplevel(parent)
        self.child_root.title(title)
        self.child_root.geometry(f"{width}x{height}+200+100")
        self.child_root.resizable(resizable[0], resizable[1])
        if icon:
            self.child_root.iconbitmap(icon)

        # Установка стиля окна
        self.style_child = ttk.Style(self.child_root)
        self.style_child.theme_use(theme)

    def grab_focus(self):  # Метод сохранения фокуса на дочернем окне
        self.child_root.grab_set()
        self.child_root.focus_set()
        self.child_root.wait_window()

    def destroy_child(self):  # Метод закрытия дочернего окна
        self.child_root.destroy()
