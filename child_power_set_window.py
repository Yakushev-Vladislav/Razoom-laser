import tkinter as tk
from tkinter import ttk

from path_getting import PathName


class ChildPowerSet(tk.Toplevel):
    def __init__(self, parent, width: int, height: int, theme: str,
                 title: str = 'Подбор режимов',
                 resizable: tuple = (False, False), icon: str | None = None):
        """
        Конфигурация дочернего окна подбора режимов для гравировки / резки
        :param parent: Класс-родитель
        :param width: Ширина окна
        :param height: Высота окна
        :param theme: Тема окна (приложения)
        :param title: Название окна
        :param resizable: Изменяемость окна. По умолчанию: (False, False)
        :param icon: Иконка окна. По умолчанию: None
        """
        super().__init__(parent)
        self.title(title)
        self.geometry(f"{width}x{height}+20+20")
        self.resizable(resizable[0], resizable[1])
        if icon:
            self.iconbitmap(PathName.resource_path(icon))

        # Установка стиля окна
        self.style_child = ttk.Style(self)
        self.style_child.theme_use(theme)

    def grab_focus(self) -> None:
        """
        Метод сохранения фокуса на дочернем окне
        """
        self.grab_set()
        self.focus_set()
        self.wait_window()

    def destroy_child(self) -> None:
        """
        Метод закрытия (разрушения) дочернего окна
        """
        self.destroy()
