import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askokcancel
import configparser



class ChildConfigSet:
    def __init__(self, parent, width, height, theme, standard,
                 title='Предварительная настройка программы',
                 resizable=(False, False), icon=None):

        """
        Дочернее окно предварительных настроек программы, а также изменения
        настроек с их последующим сохранением в файл конфигурации.

        :param parent: Класс родительского окна
        :param width: Ширина окна
        :param height: Высота окна
        :param theme: Тема, используемая в родительском классе
        :param standard: Словарь стандартных изделий и их конфигураций
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
        self.standard_names = standard

        # Создание вкладок окна
        self.child_tabs_control = ttk.Notebook(self.child_root)
        self.tab_1 = ttk.Frame(self.child_tabs_control)
        self.tab_2 = ttk.Frame(self.child_tabs_control)

        # Конфигурация отзывчивости вкладок окна
        self.tab_1.columnconfigure(index=0, weight=1)
        self.tab_1.columnconfigure(index=1, weight=1)
        self.tab_1.columnconfigure(index=2, weight=1)
        self.tab_1.rowconfigure(index=0, weight=1)
        self.tab_1.rowconfigure(index=1, weight=1)
        self.tab_1.rowconfigure(index=2, weight=1)
        self.tab_1.rowconfigure(index=3, weight=1)
        self.tab_1.rowconfigure(index=4, weight=1)
        self.tab_1.rowconfigure(index=5, weight=1)
        self.tab_1.rowconfigure(index=6, weight=1)
        self.tab_1.rowconfigure(index=7, weight=1)
        self.tab_1.rowconfigure(index=8, weight=1)
        self.tab_1.rowconfigure(index=9, weight=1)
        self.tab_1.rowconfigure(index=10, weight=1)
        self.tab_1.rowconfigure(index=11, weight=1)
        self.tab_1.rowconfigure(index=12, weight=1)
        self.tab_1.rowconfigure(index=13, weight=1)
        self.tab_1.rowconfigure(index=14, weight=1)

        self.tab_2.columnconfigure(index=0, weight=1)
        self.tab_2.columnconfigure(index=1, weight=50)
        self.tab_2.columnconfigure(index=2, weight=1)
        self.tab_2.rowconfigure(index=0, weight=1)
        self.tab_2.rowconfigure(index=1, weight=2)

        # Конфигурация форм вкладок
        self.tab_2_panel_1 = ttk.Frame(self.tab_2, padding=(0, 0, 0, 0))
        self.tab_2_panel_1.grid(row=0, column=0, padx=0, pady=(0, 0),
                                sticky="nsew")
        self.tab_2_panel_2 = ttk.Frame(self.tab_2, padding=(0, 0, 0, 0))
        self.tab_2_panel_2.grid(row=1, column=0, padx=0, pady=(0, 0),
                                sticky="nsew", columnspan=3)

        # Конфигурация отзывчивости форм
        self.tab_2_panel_2.columnconfigure(index=0, weight=1)
        self.tab_2_panel_2.columnconfigure(index=1, weight=1)
        self.tab_2_panel_2.columnconfigure(index=2, weight=1)
        self.tab_2_panel_2.columnconfigure(index=3, weight=1)
        self.tab_2_panel_2.rowconfigure(index=0, weight=1)
        self.tab_2_panel_2.rowconfigure(index=1, weight=2)
        self.tab_2_panel_2.rowconfigure(index=2, weight=1)
        self.tab_2_panel_2.rowconfigure(index=3, weight=1)
        self.tab_2_panel_2.rowconfigure(index=4, weight=2)

        # Добавление вкладок в набор
        self.child_tabs_control.add(self.tab_1, text='Основные настройки')
        self.child_tabs_control.add(self.tab_2, text='Стандартные изделия')
        # Упаковка вкладок
        self.child_tabs_control.pack(fill='both', expand=True)

        # ___ Создание виджетов 1 вкладки ___
        # Информация по первому блоку
        ttk.Label(self.tab_1, text='Блок настройки базовых цен',
                  foreground='red').grid(
            row=0, column=0, padx=0, pady=0, sticky='ns', columnspan=3
        )

        # Окно ввода __ Минимальная стоимость работы __
        ttk.Label(self.tab_1, text='Мин. стоимость').grid(
            row=1, column=0, padx=0, pady=0, sticky='ns'
        )
        self.ent_minimum = ttk.Entry(
            self.tab_1,
            width=20
        )
        self.ent_minimum.grid(row=2, column=0, padx=5, pady=5,
                           sticky='nsew')

        # Окно ввода __ Доп стоимость за прицел __
        ttk.Label(self.tab_1, text='Стоимость доп. прицела').grid(
            row=1, column=1, padx=0, pady=0, sticky='ns'
        )
        self.ent_additional = ttk.Entry(
            self.tab_1,
            width=20
        )
        self.ent_additional.grid(row=2, column=1, padx=5, pady=5,
                              sticky='nsew')

        # Окно ввода __ Стоимость часа работы __
        ttk.Label(self.tab_1, text='Стоимость часа работы').grid(
            row=1, column=2, padx=0, pady=0, sticky='ns'
        )
        self.ent_additional = ttk.Entry(
            self.tab_1,
            width=20
        )
        self.ent_additional.grid(row=2, column=2, padx=5, pady=5,
                                 sticky='nsew')

        # Разделительная черта
        ttk.Separator(self.tab_1).grid(
            row=3, column=0, columnspan=3, pady=0, sticky='ew'
        )

        # Информация по второму блоку
        ttk.Label(self.tab_1,
                  text='Блок настройки весовых коэффициентов',
                  foreground='red').grid(
            row=4, column=0, padx=0, pady=0, sticky='ns', columnspan=3
        )

        # Окно ввода ratio_laser_gas __Тип лазера__
        ttk.Label(self.tab_1, text='СО2 лазер').grid(
            row=5, column=0, padx=0, pady=0, sticky='ns'
        )
        self.ent_ratio_laser_gas = ttk.Entry(
            self.tab_1,
            width=20
        )
        self.ent_ratio_laser_gas.grid(row=6, column=0, padx=5, pady=5,
                                 sticky='nsew')

        # Окно ввода ratio_rotation __Вращатель__
        ttk.Label(self.tab_1, text='Вращатель').grid(
            row=5, column=1, padx=0, pady=0, sticky='ns'
        )
        self.ent_ratio_rotation = ttk.Entry(
            self.tab_1,
            width=20
        )
        self.ent_ratio_rotation.grid(row=6, column=1, padx=5, pady=5,
                                      sticky='nsew')

        # Окно ввода ratio_timing __Срочность__
        ttk.Label(self.tab_1, text='Срочность').grid(
            row=5, column=2, padx=0, pady=0, sticky='ns'
        )
        self.ent_ratio_timing = ttk.Entry(
            self.tab_1,
            width=20
        )
        self.ent_ratio_timing.grid(row=6, column=2, padx=5, pady=5,
                                     sticky='nsew')

                # Окно ввода ratio_packing __Распаковка/Запаковка__
        ttk.Label(self.tab_1, text='Распаковка/Запаковка').grid(
            row=7, column=0, padx=0, pady=0, sticky='ns'
        )
        self.ent_ratio_packing = ttk.Entry(
            self.tab_1,
            width=20
        )
        self.ent_ratio_packing.grid(row=8, column=0, padx=5, pady=5,
                                              sticky='nsew')

        # Окно ввода ratio_thermal_graving __Гравировка термовлиянием__
        ttk.Label(self.tab_1, text='Грав. термовлиянием').grid(
            row=7, column=1, padx=0, pady=0, sticky='ns'
        )
        self.ent_ratio_thermal_graving = ttk.Entry(
            self.tab_1,
            width=20
        )
        self.ent_ratio_thermal_graving.grid(row=8, column=1, padx=5, pady=5,
                                    sticky='nsew')

        # Окно ввода ratio_oversize __Негабаритное изделие__
        ttk.Label(self.tab_1, text='Негабаритное изделие').grid(
            row=7, column=2, padx=0, pady=0, sticky='ns'
        )
        self.ent_ratio_oversize = ttk.Entry(
            self.tab_1,
            width=20
        )
        self.ent_ratio_oversize.grid(row=8, column=2, padx=5, pady=5,
                                            sticky='nsew')


        # Окно ввода ratio_taxation __Оплата с НДС__
        ttk.Label(self.tab_1, text='Оплата с НДС').grid(
            row=9, column=0, padx=0, pady=0, sticky='ns'
        )
        self.ent_ratio_taxation = ttk.Entry(
            self.tab_1,
            width=20
        )
        self.ent_ratio_taxation.grid(row=10, column=0, padx=5, pady=5,
                                      sticky='nsew')

        # Окно ввода ratio_rotation __Повышенное внимание__
        ttk.Label(self.tab_1, text='Повышенное внимание').grid(
            row=9, column=1, padx=0, pady=0, sticky='ns'
        )
        self.ent_ratio_rotation = ttk.Entry(
            self.tab_1,
            width=20
        )
        self.ent_ratio_rotation.grid(row=10, column=1, padx=5, pady=5,
                                     sticky='nsew')

        # Окно ввода ratio_hand_job __Ручные работы__
        ttk.Label(self.tab_1, text='Ручные работы').grid(
            row=9, column=2, padx=0, pady=0, sticky='ns'
        )
        self.ent_ratio_hand_job = ttk.Entry(
            self.tab_1,
            width=20
        )
        self.ent_ratio_hand_job.grid(row=10, column=2, padx=5, pady=5,
                                     sticky='nsew')

        # Окно ввода ratio_numbering __Счетчик__
        ttk.Label(self.tab_1, text='Счетчик').grid(
            row=11, column=0, padx=0, pady=0, sticky='ns'
        )
        self.ent_ratio_numbering = ttk.Entry(
            self.tab_1,
            width=20
        )
        self.ent_ratio_numbering.grid(row=12, column=0, padx=5, pady=5,
                                      sticky='nsew')

        # Окно ввода ratio_different_layouts __Разные макеты__
        ttk.Label(self.tab_1, text='Разные макеты').grid(
            row=11, column=1, padx=0, pady=0, sticky='ns'
        )
        self.ent_ratio_different_layouts = ttk.Entry(
            self.tab_1,
            width=20
        )
        self.ent_ratio_different_layouts.grid(row=12, column=1, padx=5, pady=5,
                                              sticky='nsew')

        # Создание кнопки обновления коэффициентов в программе
        self.btn_update_settings = ttk.Button(
            self.tab_1,
            width=10,
            text="Сохранить настройки",
            command=self.click_update_settings
        )
        self.btn_update_settings.grid(
            row=14, column=0, padx=5, pady=10, sticky='nsew', columnspan=2
        )

        # Разделительная черта
        ttk.Separator(self.tab_1).grid(
            row=13, column=0, columnspan=3, pady=5, sticky='ew'
        )

        # Создание кнопки сброса настроек "По умолчанию"
        self.btn_default_settings = ttk.Button(
            self.tab_1,
            width=10,
            text="Сбросить настройки",
            command=self.click_default_settings
        )
        self.btn_default_settings.grid(
            row=12, column=2, padx=5, pady=5, sticky='nsew'
        )

        # Создание кнопки закрытия дочернего окна
        self.btn_destroy = ttk.Button(
            self.tab_1,
            width=10,
            text="Выход",
            command=self.destroy_child
        )
        self.btn_destroy.grid(
            row=14, column=2, padx=5, pady=10, sticky='nsew'
        )

        # ___ Создание виджетов 2 вкладки ___
        # Создание и конфигурация таблицы
        tree_scroll = ttk.Scrollbar(self.tab_2)
        tree_scroll.grid(row=0, column=2, padx=0, pady=0,
                         sticky="nsew")
        self.standard_table = ttk.Treeview(
            self.tab_2,
            selectmode="extended",
            yscrollcommand=tree_scroll.set,
            height=4,
            columns=('#0', '#1', '#2', '#3'),
            show="headings"
        )
        self.standard_table.column(0, width=0, anchor="w")
        self.standard_table.column(1, width=195, anchor="w")
        self.standard_table.column(2, width=100, anchor="center")
        self.standard_table.column(3, width=100, anchor="center")

        self.standard_table.heading(0, text="", anchor="center")
        self.standard_table.heading(1, text="Наименование", anchor="center")
        self.standard_table.heading(2, text="Eng", anchor="center")
        self.standard_table.heading(3, text="Стоимость работы, руб",
                                    anchor="center")
        self.standard_table.selection()
        self.standard_table.configure(yscrollcommand=tree_scroll.set)

        # Упаковка таблицы
        self.standard_table.grid(
            row=0, column=1, padx=0, pady=0, sticky="nsew"
        )

        # Добавление данных в таблицу
        self.data_table = self.get_standard_costs()
        self.i_data = -1
        for data in self.data_table:
            self.i_data += 1
            temp_list = list()
            temp_list.append(f'{self.i_data}:')
            temp_list.extend(data)
            self.standard_table.insert('', index='end', values=temp_list)

        # Окно ввода __ Название работы __
        ttk.Label(self.tab_2_panel_2, text='Название работы').grid(
            row=0, column=0, padx=0, pady=(5,0), sticky='ns'
        )
        self.ent_name = ttk.Entry(
            self.tab_2_panel_2,
            width=20
        )
        self.ent_name.grid(row=1, column=0, padx=5, pady=(5, 10),
                           sticky='nsew')

        # Окно ввода __ Название для конфигурации __
        ttk.Label(self.tab_2_panel_2,
                  text='Название для конфигурации').grid(
            row=0, column=1, padx=5, pady=5, sticky='ns'
        )
        self.ent_name_for_config = ttk.Entry(
            self.tab_2_panel_2,
            width=20
        )
        self.ent_name_for_config.grid(row=1, column=1, padx=5, pady=(5, 10),
                                      sticky='nsew')

        # Окно ввода __ Стоимость работы __
        ttk.Label(self.tab_2_panel_2,
                  text='Стоимость работы').grid(
            row=0, column=2, padx=0, pady=5, sticky='ns'
        )
        self.ent_cost = ttk.Entry(
            self.tab_2_panel_2,
            width=20
        )
        self.ent_cost.grid(row=1, column=2, padx=5, pady=(5, 10),
                                      sticky='nsew')

        # Создание кнопки добавления работы
        self.btn_add_new_element = ttk.Button(
            self.tab_2_panel_2,
            width=10,
            text="Добавить",
            command=self.click_add
        )
        self.btn_add_new_element.grid(
            row=1, column=3, padx=5, pady=(5, 10), sticky='nsew')

        # Разделительная черта
        ttk.Separator(self.tab_2_panel_2).grid(
            row=2, column=0, columnspan=4, pady=5, sticky='ew'
        )

        # Окно ввода __ Номер удаляемой строки __
        ttk.Label(self.tab_2_panel_2,
                  text='Номер удаляемой строки').grid(
            row=3, column=0, padx=0, pady=0, sticky='ns'
        )
        self.ent_delete_element = ttk.Entry(
            self.tab_2_panel_2,
            width=20
        )
        self.ent_delete_element.grid(row=4, column=0, padx=5, pady=(10, 40),
                           sticky='nsew')

        # Создание кнопки удаления работы
        self.btn_delete_element = ttk.Button(
            self.tab_2_panel_2,
            width=10,
            text="Удалить элемент",
            command=self.click_delete_element
        )
        self.btn_delete_element.grid(
            row=4, column=1, padx=5, pady=(10, 40), sticky='nsew')

        # Создание кнопки перехода на начальную вкладку
        self.btn_back_to_tab_1 = ttk.Button(
            self.tab_2_panel_2,
            width=10,
            text="Вернуться",
            command=self.click_back
        )
        self.btn_back_to_tab_1.grid(
            row=4, column=3, padx=5, pady=(10, 40), sticky='nsew')

    def get_standard_costs(self):  # Метод получения данных для таблицы
        table_data = list()
        # Считывание информации из конфига
        costs = ConfigSet().config
        for item in self.standard_names:
            temp = [
                item,
                self.standard_names[item],
                costs["STANDARD"][self.standard_names[item]]
            ]
            table_data.append(temp)
        return table_data

    def click_back(self):
        self.child_tabs_control.select(self.tab_1)

    def click_add(self):
        pass

    def click_update_settings(self):
        pass

    def click_default_settings(self):
        if askokcancel('Сброс настроек', 'Вы действительно хотите сбросить '
                                         'настройки по умолчанию?'):
            ConfigSet().default_settings()

    def click_delete_element(self):
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
