import tkinter as tk
from tkinter import ttk
import configparser


class ChildConfigSet:
    def __init__(self, parent, width, height, theme, title='Предварительная '
                                                           'настройка '
                                                           'программы',
                 resizable=(False, False), icon=None):

        """
        Дочернее окно предварительных настроек программы, а также изменения
        настроек с их последующим сохранением в файл конфигурации.

        :param parent: Класс родительского окна
        :param width: Ширина окна
        :param height: Высота окна
        :param theme: Тема, используемая в родительском классе
        :param title: Название окна
        :param resizable: Изменяемость окна. По умолчанию: (False, False)
        :param icon: Иконка окна. По умолчанию: None
        """
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

    def get_standard_costs(self):
        pass

    def grab_focus(self):  # Метод сохранения фокуса на дочернем окне
        self.child_root.grab_set()
        self.child_root.focus_set()
        self.child_root.wait_window()

    def destroy_child(self):  # Метод закрытия дочернего окна
        self.child_root.destroy()


class ConfigSet:
    def __init__(self):
        """
        Класс работы с файлом конфигурации.
        """

        # Чтение файла конфигурации
        self.config = configparser.ConfigParser()
        self.config.read('settings/settings.ini')

        # Создание списков коэффициентов и стандартных настроек

    def update_settings(self):  # Обновления файла конфигурации
        with open('settings/settings.ini', 'w') as configfile:
            self.config.write(configfile)

    def default_settings(self):  # Метод сброса настроек программы до базовых
        # Формирование переменной базовой конфигурации
        string_config = """
        [INFO]
        
        [MAIN]
        min_cost = 1000
        additional_cost = 400
        one_hour_of_work = 5000
        
        [STANDARD]
        ring = 1400
        knife = 1000
        pen = 1000
        badge = 900
        thermos = 1200
        keyboard = 1500
        personal_keyboard = 2000
        
        [RATIO_SETTINGS]
        ratio_laser_diode = 1
        ratio_laser_gas = 1.15
        ratio_rotation = 1.3
        ratio_timing = 1.5
        ratio_attention = 1.15
        ratio_packing = 1.15
        ratio_hand_job = 1.15
        ratio_taxation = 1.2
        ratio_oversize = 1.8
        ratio_different_layouts = 1.2
        ratio_numbering = 1.05
        ratio_thermal_graving = 1.15
        """

        # Создание переменной класса конфигурации и считывание базовых разделов
        default_config = configparser.ConfigParser()
        default_config.read_string(string_config)
        # Заполнение информационного раздела
        default_config.set('INFO',
                           'info',
                           f'# This configuration file contains the '
                           f'following basic program settings:\n# MAIN - '
                           f'Contains the minimum cost of working '
                           f'on the equipment,as well as the cost of one '
                           f'hour of equipment;\n'
                           f'# STANDARD - Contains the cost of basic '
                           f'standard work on the equipment;\n'
                           f'# RATIO_SETTINGS - Contains the weighting '
                           f'factors of the complexity of the work performed.'
                           )

        # Запись в файл настроек "по умолчанию"
        with open('settings/settings.ini', 'w') as configfile:
            default_config.write(configfile)

        # Исправление ошибки статичности метода
        self.is_not_use()

    def is_not_use(self):  # Метод исправления ошибки статичности
        pass
