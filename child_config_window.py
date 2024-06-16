import tkinter as tk
from tkinter import ttk


class ChildConfigSet:
    def __init__(self, parent, width, height, theme, title='Предварительная '
                                                           'настройка '
                                                           'программы',
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

        # Объявление переменных
        self.standard_costs = None

        # Чтение файлов предварительной настройки
        file_settings = open(
            'settings/config.txt',
            'r',
            encoding='utf-8'
        )
        some_data = file_settings.readlines()
        file_settings.close()

    def get_standard_costs(self):
        file_standard = open(
            'settings/standard_grav.txt',
            'r',
            encoding='utf-8'
        )
        standard_prices = file_standard.readlines()
        file_standard.close()
        self.standard_costs = dict()
        for item in standard_prices[2::]:
            temp = item.split(': ')
            self.standard_costs[temp[0]] = int(temp[1])
        return self.standard_costs

    def grab_focus(self):  # Метод сохранения фокуса на дочернем окне
        self.child_root.grab_set()
        self.child_root.focus_set()
        self.child_root.wait_window()

    def destroy_child(self):  # Метод закрытия дочернего окна
        self.child_root.destroy()
