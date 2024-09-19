import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askokcancel
import configparser
import os
import shutil
from binds import BindEntry, BalloonTips


class ChildConfigSet:
    def __init__(self, parent, width, height, theme,
                 title='Предварительная настройка программы',
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
        self.child_root.geometry(f"{width}x{height}+20+20")
        self.child_root.resizable(resizable[0], resizable[1])
        if icon:
            self.child_root.iconbitmap(icon)

        # Установка стиля окна
        self.style_child = ttk.Style(self.child_root)
        self.style_child.theme_use(theme)

        # Объявление переменных
        self.child_temp_config = ConfigSet()
        self.not_use = None
        # Создание вкладок окна
        self.child_tabs_control = ttk.Notebook(self.child_root)
        self.tab_main_settings = ttk.Frame(self.child_tabs_control)
        self.tab_sheet_materials = ttk.Frame(self.child_tabs_control)
        self.tab_industrial_settings = ttk.Frame(self.child_tabs_control)

        # Конфигурация отзывчивости вкладок окна
        self.tab_main_settings.columnconfigure(index=0, weight=1)
        self.tab_main_settings.columnconfigure(index=1, weight=1)
        self.tab_main_settings.columnconfigure(index=2, weight=1)
        self.tab_main_settings.columnconfigure(index=3, weight=1)
        self.tab_main_settings.rowconfigure(index=0, weight=1)
        self.tab_main_settings.rowconfigure(index=1, weight=1)
        self.tab_main_settings.rowconfigure(index=2, weight=1)
        self.tab_main_settings.rowconfigure(index=3, weight=1)
        self.tab_main_settings.rowconfigure(index=4, weight=1)
        self.tab_main_settings.rowconfigure(index=5, weight=1)
        self.tab_main_settings.rowconfigure(index=6, weight=1)
        self.tab_main_settings.rowconfigure(index=7, weight=1)
        self.tab_main_settings.rowconfigure(index=8, weight=1)
        self.tab_main_settings.rowconfigure(index=9, weight=1)
        self.tab_main_settings.rowconfigure(index=10, weight=1)
        self.tab_main_settings.rowconfigure(index=11, weight=1)
        self.tab_main_settings.rowconfigure(index=12, weight=1)
        self.tab_main_settings.rowconfigure(index=13, weight=1)
        self.tab_main_settings.rowconfigure(index=14, weight=1)

        self.tab_sheet_materials.columnconfigure(index=0, weight=1)
        self.tab_sheet_materials.columnconfigure(index=1, weight=50)
        self.tab_sheet_materials.columnconfigure(index=2, weight=1)
        self.tab_sheet_materials.rowconfigure(index=0, weight=2)
        self.tab_sheet_materials.rowconfigure(index=1, weight=1)

        # Конфигурация форм вкладок
        self.tab_2_panel_table = ttk.Frame(
            self.tab_sheet_materials, padding=(0, 0, 0, 0))
        self.tab_2_panel_table.grid(row=0, column=0, padx=0, pady=(0, 0),
                                    sticky="nsew")
        self.tab_2_panel_widgets = ttk.Frame(
            self.tab_sheet_materials, padding=(0, 0, 0, 0))
        self.tab_2_panel_widgets.grid(row=1, column=0, padx=0, pady=(0, 0),
                                      sticky="nsew", columnspan=3)

        # Конфигурация отзывчивости форм
        self.tab_2_panel_widgets.columnconfigure(index=0, weight=1)
        self.tab_2_panel_widgets.columnconfigure(index=1, weight=1)
        self.tab_2_panel_widgets.columnconfigure(index=2, weight=1)
        self.tab_2_panel_widgets.rowconfigure(index=0, weight=1)
        self.tab_2_panel_widgets.rowconfigure(index=1, weight=1)
        self.tab_2_panel_widgets.rowconfigure(index=2, weight=1)

        # Добавление вкладок в набор
        self.child_tabs_control.add(
            self.tab_main_settings, text='Частные лица')
        self.child_tabs_control.add(
            self.tab_sheet_materials, text='Стандартные изделия')
        # Пока уберем: self.child_tabs_control.add(
        # Пока уберем:     self.tab_industrial_settings, text='Оптовый расчет')

        # Упаковка вкладок
        self.child_tabs_control.pack(fill='both', expand=True)

        # ___ Создание виджетов 1 вкладки ___
        # Информация по первому блоку
        ttk.Label(
            self.tab_main_settings, text='Блок настройки базовых цен, руб.',
            foreground='red').grid(
            row=0, column=0, padx=0, pady=0, sticky='ns', columnspan=4
        )

        # Окно ввода __ Минимальная стоимость работы __
        ttk.Label(self.tab_main_settings, text='Мин. стоимость').grid(
            row=1, column=0, padx=0, pady=0, sticky='ns'
        )
        self.ent_minimum = ttk.Entry(
            self.tab_main_settings,
            width=20
        )
        self.ent_minimum.grid(row=2, column=0, padx=5, pady=5,
                              sticky='nsew')

        # Окно ввода __ Доп стоимость за прицел __
        ttk.Label(self.tab_main_settings, text='Стоимость доп. прицела').grid(
            row=1, column=1, padx=0, pady=0, sticky='ns'
        )
        self.ent_additional = ttk.Entry(
            self.tab_main_settings,
            width=20
        )
        self.ent_additional.grid(row=2, column=1, padx=5, pady=5,
                                 sticky='nsew')

        # Окно ввода __ Стоимость часа работы __
        ttk.Label(self.tab_main_settings, text='Стоимость часа работы').grid(
            row=1, column=2, padx=0, pady=0, sticky='ns'
        )
        self.ent_one_hour = ttk.Entry(
            self.tab_main_settings,
            width=20
        )
        self.ent_one_hour.grid(row=2, column=2, padx=5, pady=5,
                               sticky='nsew')

        # Окно ввода __ Степень градации __
        ttk.Label(self.tab_main_settings, text='Степень градации').grid(
            row=1, column=3, padx=0, pady=0, sticky='ns'
        )
        self.ent_many_items = ttk.Entry(
            self.tab_main_settings,
            width=20
        )
        self.ent_many_items.grid(row=2, column=3, padx=5, pady=5,
                                 sticky='nsew')

        # Разделительная черта
        ttk.Separator(self.tab_main_settings).grid(
            row=3, column=0, columnspan=4, pady=0, sticky='ew'
        )

        # Информация по второму блоку
        ttk.Label(self.tab_main_settings,
                  text='Блок настройки весовых коэффициентов',
                  foreground='red').grid(
            row=4, column=0, padx=0, pady=0, sticky='ns', columnspan=4
        )

        # Окно ввода ratio_laser_gas __Тип лазера__
        ttk.Label(self.tab_main_settings, text='СО2 лазер').grid(
            row=5, column=0, padx=0, pady=0, sticky='ns'
        )
        self.ent_ratio_laser_gas = ttk.Entry(
            self.tab_main_settings,
            width=20
        )
        self.ent_ratio_laser_gas.grid(row=6, column=0, padx=5, pady=5,
                                      sticky='nsew')

        # Окно ввода ratio_rotation __Вращатель__
        ttk.Label(self.tab_main_settings, text='Вращатель').grid(
            row=5, column=1, padx=0, pady=0, sticky='ns'
        )
        self.ent_ratio_rotation = ttk.Entry(
            self.tab_main_settings,
            width=20
        )
        self.ent_ratio_rotation.grid(row=6, column=1, padx=5, pady=5,
                                     sticky='nsew')

        # Окно ввода ratio_timing __Срочность__
        ttk.Label(self.tab_main_settings, text='Срочность').grid(
            row=5, column=2, padx=0, pady=0, sticky='ns'
        )
        self.ent_ratio_timing = ttk.Entry(
            self.tab_main_settings,
            width=20
        )
        self.ent_ratio_timing.grid(row=6, column=2, padx=5, pady=5,
                                   sticky='nsew')

        # Окно ввода ratio_attention __Повышенное внимание__
        ttk.Label(self.tab_main_settings, text='Повышенное внимание').grid(
            row=5, column=3, padx=0, pady=0, sticky='ns'
        )
        self.ent_ratio_attention = ttk.Entry(
            self.tab_main_settings,
            width=20
        )
        self.ent_ratio_attention.grid(row=6, column=3, padx=5, pady=5,
                                      sticky='nsew')

        # Окно ввода ratio_packing __Распаковка/Запаковка__
        ttk.Label(self.tab_main_settings, text='Распаковка/Запаковка').grid(
            row=7, column=0, padx=0, pady=0, sticky='ns'
        )
        self.ent_ratio_packing = ttk.Entry(
            self.tab_main_settings,
            width=20
        )
        self.ent_ratio_packing.grid(row=8, column=0, padx=5, pady=5,
                                    sticky='nsew')

        # Окно ввода ratio_hand_job __Ручные работы__
        ttk.Label(self.tab_main_settings, text='Ручные работы').grid(
            row=7, column=1, padx=0, pady=0, sticky='ns'
        )
        self.ent_ratio_hand_job = ttk.Entry(
            self.tab_main_settings,
            width=20
        )
        self.ent_ratio_hand_job.grid(row=8, column=1, padx=5, pady=5,
                                     sticky='nsew')

        # Окно ввода ratio_docking __Стыковка элементов__
        ttk.Label(self.tab_main_settings, text='Стыковка элементов').grid(
            row=7, column=2, padx=0, pady=0, sticky='ns'
        )
        self.ent_ratio_docking = ttk.Entry(
            self.tab_main_settings,
            width=20
        )
        self.ent_ratio_docking.grid(row=8, column=2, padx=5, pady=5,
                                    sticky='nsew')

        # Окно ввода ratio_oversize __Негабаритное изделие__
        ttk.Label(self.tab_main_settings, text='Негабаритное изделие').grid(
            row=7, column=3, padx=0, pady=0, sticky='ns'
        )
        self.ent_ratio_oversize = ttk.Entry(
            self.tab_main_settings,
            width=20
        )
        self.ent_ratio_oversize.grid(row=8, column=3, padx=5, pady=5,
                                     sticky='nsew')

        # Окно ввода ratio_different_layouts __Разные макеты__
        ttk.Label(self.tab_main_settings, text='Разные макеты').grid(
            row=9, column=0, padx=0, pady=0, sticky='ns'
        )
        self.ent_ratio_different_layouts = ttk.Entry(
            self.tab_main_settings,
            width=20
        )
        self.ent_ratio_different_layouts.grid(row=10, column=0, padx=5, pady=5,
                                              sticky='nsew')
        # Окно ввода ratio_numbering __Счетчик__
        ttk.Label(self.tab_main_settings, text='Счетчик').grid(
            row=9, column=1, padx=0, pady=0, sticky='ns'
        )
        self.ent_ratio_numbering = ttk.Entry(
            self.tab_main_settings,
            width=20
        )
        self.ent_ratio_numbering.grid(row=10, column=1, padx=5, pady=5,
                                      sticky='nsew')

        # Окно ввода ratio_thermal_graving __Гравировка термовлиянием__
        ttk.Label(self.tab_main_settings, text='Термовлияние').grid(
            row=9, column=2, padx=0, pady=0, sticky='ns'
        )
        self.ent_ratio_thermal_graving = ttk.Entry(
            self.tab_main_settings,
            width=20
        )
        self.ent_ratio_thermal_graving.grid(row=10, column=2, padx=5, pady=5,
                                            sticky='nsew')

        # Окно ввода ratio_taxation __Оплата с НДС__
        ttk.Label(
            self.tab_main_settings, text='Оплата по счету: ООО, ИП').grid(
            row=9, column=3, padx=0, pady=0, sticky='ns'
        )
        self.ent_ratio_taxation = ttk.Entry(
            self.tab_main_settings,
            width=20
        )
        self.ent_ratio_taxation.grid(row=10, column=3, padx=5, pady=5,
                                     sticky='nsew')

        # Окно ввода gradation_difficult __Сложность установки__
        ttk.Label(self.tab_main_settings, text='Сложность установки').grid(
            row=11, column=0, padx=0, pady=0, sticky='ns', columnspan=1
        )
        self.ent_gradation_difficult = ttk.Entry(
            self.tab_main_settings,
            width=20
        )
        self.ent_gradation_difficult.grid(row=12, column=0, padx=5, pady=5,
                                          sticky='nsew', columnspan=1)

        # Окно ввода gradation_depth __Глубина гравировки__
        ttk.Label(self.tab_main_settings, text='Глубина гравировки').grid(
            row=11, column=1, padx=0, pady=0, sticky='ns', columnspan=1
        )
        self.ent_gradation_depth = ttk.Entry(
            self.tab_main_settings,
            width=20
        )
        self.ent_gradation_depth.grid(row=12, column=1, padx=5, pady=5,
                                      sticky='nsew', columnspan=1)

        # Окно ввода gradation_area __Коэффициенты площади__
        ttk.Label(self.tab_main_settings, text='Коэффициенты площади').grid(
            row=11, column=2, padx=0, pady=0, sticky='ns', columnspan=1
        )
        self.ent_gradation_area = ttk.Entry(
            self.tab_main_settings,
            width=20
        )
        self.ent_gradation_area.grid(row=12, column=2, padx=5, pady=5,
                                     sticky='nsew', columnspan=1)

        # Разделительная черта
        ttk.Separator(self.tab_main_settings).grid(
            row=13, column=0, columnspan=4, pady=5, sticky='ew'
        )

        # Создание кнопки обновления коэффициентов в программе
        self.btn_update_settings = ttk.Button(
            self.tab_main_settings,
            width=10,
            text="Сохранить настройки",
            command=self.click_update_settings
        )
        self.btn_update_settings.grid(
            row=14, column=0, padx=5, pady=10, sticky='nsew', columnspan=2
        )

        # Создание кнопки сброса настроек "По умолчанию"
        self.btn_default_settings = ttk.Button(
            self.tab_main_settings,
            width=10,
            text="Сбросить настройки",
            command=self.click_default_settings
        )
        self.btn_default_settings.grid(
            row=14, column=2, padx=5, pady=10, sticky='nsew'
        )

        # Создание кнопки закрытия дочернего окна
        self.btn_destroy = ttk.Button(
            self.tab_main_settings,
            width=10,
            text="Выход",
            command=self.destroy_child
        )
        self.btn_destroy.grid(
            row=14, column=3, padx=5, pady=10, sticky='nsew'
        )

        # ___ Создание виджетов 2 вкладки ___
        # Создание и конфигурация таблицы
        tree_scroll = ttk.Scrollbar(self.tab_sheet_materials)
        tree_scroll.grid(row=0, column=2, padx=0, pady=0,
                         sticky="nsew")
        self.standard_table = ttk.Treeview(
            self.tab_sheet_materials,
            selectmode="extended",
            yscrollcommand=tree_scroll.set,
            height=4,
            columns=('#1', '#2'),
            show="headings"
        )
        self.standard_table.column(0, width=400, anchor="w")
        self.standard_table.column(1, width=300, anchor="center")

        self.standard_table.heading(0, text="Название работы", anchor="center")
        self.standard_table.heading(1, text="Стоимость работы, руб",
                                    anchor="center")
        self.standard_table.selection()
        self.standard_table.configure(yscrollcommand=tree_scroll.set)

        # Упаковка таблицы
        self.standard_table.grid(
            row=0, column=1, padx=0, pady=0, sticky="nsew"
        )

        # Добавление данных в таблицу
        self.get_standard_costs()

        # Окно ввода __ Название работы __
        self.ent_name = ttk.Entry(
            self.tab_2_panel_widgets,
            width=10,
            takefocus=False
        )
        self.ent_name.grid(row=0, column=0, padx=5, pady=(5, 10),
                           sticky='nsew', columnspan=1)

        # Окно ввода __ Стоимость работы __
        self.ent_cost = ttk.Entry(
            self.tab_2_panel_widgets,
            width=10,
            takefocus=False
        )
        self.ent_cost.grid(row=0, column=1, padx=5, pady=(5, 10),
                           sticky='nsew')

        # Создание кнопки добавления работы
        self.btn_add_new_element = ttk.Button(
            self.tab_2_panel_widgets,
            width=10,
            text="Добавить/изменить работу",
            command=self.click_add_standard
        )
        self.btn_add_new_element.grid(
            row=0, column=2, padx=5, pady=(5, 10), sticky='nsew', columnspan=1)

        # Разделительная черта
        ttk.Separator(self.tab_2_panel_widgets).grid(
            row=1, column=0, columnspan=4, pady=5, sticky='ew'
        )

        # Окно ввода __ Номер удаляемой строки __

        # Создание кнопки удаления работы
        self.btn_delete_element = ttk.Button(
            self.tab_2_panel_widgets,
            width=10,
            text="Удалить элемент",
            command=self.click_delete_element
        )
        self.btn_delete_element.grid(
            row=2, column=0, padx=5, pady=(10, 20), sticky='nsew',
            columnspan=2)

        # Создание кнопки перехода на начальную вкладку
        self.btn_back_to_tab_1 = ttk.Button(
            self.tab_2_panel_widgets,
            width=10,
            text="Вернуться",
            command=self.click_back
        )
        self.btn_back_to_tab_1.grid(
            row=2, column=2, padx=5, pady=(10, 20), sticky='nsew')

        # Запись данных в окна ввода
        self.update_data_in_widgets()
        self.add_bind_entry()
        self.add_tips()

    def update_data_in_widgets(self):  # Запись/обновление данных в окнах ввода
        # Считывание данных в переменные
        update_config = ConfigSet().config
        ratio_from_config = update_config['RATIO_SETTINGS']
        main_from_config = update_config['MAIN']
        gradation_from_config = update_config['GRADATION']

        # Очистка полей ввода для обновления данных
        # Первый блок
        self.ent_minimum.delete(0, tk.END)
        self.ent_additional.delete(0, tk.END)
        self.ent_one_hour.delete(0, tk.END)
        self.ent_many_items.delete(0, tk.END)

        # Второй блок
        self.ent_ratio_laser_gas.delete(0, tk.END)
        self.ent_ratio_rotation.delete(0, tk.END)
        self.ent_ratio_timing.delete(0, tk.END)
        self.ent_ratio_packing.delete(0, tk.END)
        self.ent_ratio_thermal_graving.delete(0, tk.END)
        self.ent_ratio_oversize.delete(0, tk.END)
        self.ent_ratio_taxation.delete(0, tk.END)
        self.ent_ratio_attention.delete(0, tk.END)
        self.ent_ratio_hand_job.delete(0, tk.END)
        self.ent_ratio_numbering.delete(0, tk.END)
        self.ent_ratio_different_layouts.delete(0, tk.END)
        self.ent_ratio_docking.delete(0, tk.END)
        self.ent_gradation_difficult.delete(0, tk.END)
        self.ent_gradation_depth.delete(0, tk.END)
        self.ent_gradation_area.delete(0, tk.END)

        # Запись значений в окнах ввода
        # Первый блок
        self.ent_minimum.insert(0, main_from_config['min_cost'])
        self.ent_additional.insert(0, main_from_config['additional_cost'])
        self.ent_one_hour.insert(0, main_from_config['one_hour_of_work'])
        self.ent_many_items.insert(0, main_from_config['many_items'])

        # Второй блок
        self.ent_ratio_laser_gas.insert(
            0, ratio_from_config['ratio_laser_gas'])
        self.ent_ratio_rotation.insert(
            0, ratio_from_config['ratio_rotation'])
        self.ent_ratio_timing.insert(
            0, ratio_from_config['ratio_timing'])
        self.ent_ratio_packing.insert(
            0, ratio_from_config['ratio_packing'])
        self.ent_ratio_thermal_graving.insert(
            0, ratio_from_config['ratio_thermal_graving'])
        self.ent_ratio_oversize.insert(
            0, ratio_from_config['ratio_oversize'])
        self.ent_ratio_attention.insert(
            0, ratio_from_config['ratio_attention'])
        self.ent_ratio_hand_job.insert(
            0, ratio_from_config['ratio_hand_job'])
        self.ent_ratio_numbering.insert(
            0, ratio_from_config['ratio_numbering'])
        self.ent_ratio_different_layouts.insert(
            0, ratio_from_config['ratio_different_layouts'])
        self.ent_ratio_docking.insert(
            0, ratio_from_config['ratio_docking'])
        self.ent_ratio_taxation.insert(
            0, ratio_from_config['ratio_taxation'])
        self.ent_gradation_difficult.insert(
            0, gradation_from_config['difficult'])
        self.ent_gradation_depth.insert(
            0, gradation_from_config['depth'])
        self.ent_gradation_area.insert(
            0, gradation_from_config['area'])

        # Обновление данных в таблице второй вкладки
        for item in self.standard_table.get_children():
            self.standard_table.delete(item)

        self.get_standard_costs()

        # Очистка полей ввода второй вкладки
        self.ent_name.delete(0, tk.END)
        self.ent_cost.delete(0, tk.END)

        BindEntry(self.ent_cost, text='Стоимость, руб').to_add_entry_child()
        BindEntry(self.ent_name, text='Название').to_add_entry_child()

        self.child_root.update()

        del (update_config, ratio_from_config, main_from_config,
             gradation_from_config)

    def get_standard_costs(self):  # Метод получения данных для таблицы
        table_data = list()
        # Считывание информации из конфига
        costs = self.child_temp_config.config["STANDARD"]
        for k, v in costs.items():
            temp = [k, v]
            table_data.append(temp)
        for data in table_data:
            self.standard_table.insert('', index='end', values=data)

        del costs

    def click_back(self):  # Метод возвращения на первую вкладку
        self.child_tabs_control.select(self.tab_main_settings)

    def click_add_standard(self):  # Метод добавления новой стандартной работы
        # Создание локальной переменной конфигурации
        add_config = self.child_temp_config.config

        # Считываем с окон новые данные
        try:
            add_config['STANDARD'][self.ent_name.get()] = (
                str(int(self.ent_cost.get())))
        except ValueError:
            tk.messagebox.showerror(
                'Ошибка добавления',
                'Стоимость работы введена некорректно!'
            )

        # Записываем данные в файл
        self.child_temp_config.update_settings(some_new=add_config)

        # Обновление данных в таблице
        self.update_data_in_widgets()

        del add_config

    def click_update_settings(self):  # Метод сохранения настроек
        # Создание переменной конфигурации
        new_config = self.child_temp_config.config

        # Запись новых данных в переменную конфигурации
        # Первый блок
        try:  # Валидация введенных данных
            new_config['MAIN']['min_cost'] = str(
                int(self.ent_minimum.get()))
            new_config['MAIN']['additional_cost'] = str(
                int(self.ent_additional.get()))
            new_config['MAIN']['one_hour_of_work'] = str(
                int(self.ent_one_hour.get()))
            new_config['MAIN']['many_items'] = str(
                float(self.ent_many_items.get()))

        except ValueError:
            tk.messagebox.showerror(
                'Ошибка добавления',
                'Данные первого блока введены некорректно!'
            )
            self.update_data_in_widgets()

        # Второй блок
        try:
            new_config['RATIO_SETTINGS']['ratio_laser_gas'] = str(
                float(self.ent_ratio_laser_gas.get()))
            new_config['RATIO_SETTINGS']['ratio_rotation'] = str(
                float(self.ent_ratio_rotation.get()))
            new_config['RATIO_SETTINGS']['ratio_timing'] = str(
                float(self.ent_ratio_timing.get()))
            new_config['RATIO_SETTINGS']['ratio_attention'] = str(
                float(self.ent_ratio_attention.get()))
            new_config['RATIO_SETTINGS']['ratio_packing'] = str(
                float(self.ent_ratio_packing.get()))
            new_config['RATIO_SETTINGS']['ratio_hand_job'] = str(
                float(self.ent_ratio_hand_job.get()))
            new_config['RATIO_SETTINGS']['ratio_oversize'] = str(
                float(self.ent_ratio_oversize.get()))
            new_config['RATIO_SETTINGS']['ratio_different_layouts'] = str(
                float(self.ent_ratio_different_layouts.get()))
            new_config['RATIO_SETTINGS']['ratio_numbering'] = str(
                float(self.ent_ratio_numbering.get()))
            new_config['RATIO_SETTINGS']['ratio_thermal_graving'] = str(
                float(self.ent_ratio_thermal_graving.get()))
            new_config['RATIO_SETTINGS']['ratio_docking'] = str(
                float(self.ent_ratio_docking.get()))

            [float(x) for x in
                self.ent_ratio_taxation.get().split(',')]
            [float(x) for x in
                self.ent_gradation_difficult.get().split(',')]
            [float(x) for x in
                self.ent_gradation_depth.get().split(',')]

            new_config['RATIO_SETTINGS']['ratio_taxation'] = (
                self.ent_ratio_taxation.get())
            new_config['GRADATION']['difficult'] = (
                self.ent_gradation_difficult.get())
            new_config['GRADATION']['depth'] = (
                self.ent_gradation_depth.get())

        except ValueError:
            tk.messagebox.showerror(
                'Ошибка добавления',
                'Данные второго блока введены некорректно!'
            )
            self.update_data_in_widgets()

        try:
            temp_list_area = [float(x) for x in
                              self.ent_gradation_area.get().split(',')]

            if len(temp_list_area) == 2:
                new_config['GRADATION']['area'] = (
                    self.ent_gradation_area.get())
            else:
                tk.messagebox.showerror(
                    'Ошибка добавления',
                    'В поле ввода габаритов гравировки должны быть 2 значения!'
                    '\n -> Первое для диодного лазера;\n'
                    '-> Второе для газового лазера.'
                )

        except ValueError:
            tk.messagebox.showerror(
                'Ошибка добавления',
                'Данные габаритов гравировки введены некорректно!'
            )
            self.update_data_in_widgets()

        # Запись в файл конфигурации
        self.child_temp_config.update_settings(some_new=new_config)

    def click_default_settings(self):  # Метод сброса настроек "По умолчанию"
        if askokcancel('Сброс настроек', 'Вы действительно хотите сбросить '
                                         'настройки по умолчанию?'):
            self.child_temp_config.default_settings()

            # Переопределяем переменную конфигурации после сброса
            self.child_temp_config = ConfigSet()

        # Обновляем данные в полях ввода и таблице
        self.update_data_in_widgets()
        self.child_root.update()

    def click_delete_element(self):  # Метод удаления стандартной работы
        # Создаем переменную конфигурации
        config_with_deleted_item = self.child_temp_config.config

        try:
            # Считывание данных из окна ввода
            deleted_item = self.standard_table.item(
                    self.standard_table.focus())
            if askokcancel('Удаление элемента',
                           f'Вы действительно хотите удалить:\n'
                           f'"{str(deleted_item["values"][0])}"'):
                # Удаление элемента
                config_with_deleted_item.remove_option(
                    'STANDARD', str(deleted_item['values'][0]))
                # Обновление данных в файле
                self.child_temp_config.update_settings(
                    some_new=config_with_deleted_item)
        except (ValueError, KeyboardInterrupt, IndexError):
            tk.messagebox.showerror(
                'Ошибка удаления!',
                'Выберите в таблице удаляемую строку.'
            )
        # Обновление данных в таблице
        self.update_data_in_widgets()

        del config_with_deleted_item

    def add_bind_entry(self):  # Установка фонового текста в полях ввода
        BindEntry(self.ent_cost, text='Стоимость, руб')
        BindEntry(self.ent_name, text='Название')

        self.standard_table.bind('<Button-1>', self.bind_treeview)

    def add_tips(self):
        """
        Метод добавления подсказок к элементам интерфейса.
        """
        # Виджеты первой вкладки
        BalloonTips(self.ent_minimum,
                    text=f'Минимальная стоимость работы, руб.')
        BalloonTips(self.ent_additional,
                    text=f'Стоимость доп. установки/прицела, руб.')
        BalloonTips(self.ent_one_hour,
                    text=f'Стоимость одного часа работы\nоборудования, руб.')

        BalloonTips(self.ent_many_items,
                    text=f'Степень функции, y=a*x^(-c),\n'
                         f'{"‾"*70}\n'
                         f'где y - искомый коэффициент понижения цены;\n'
                         f'      a - поправка расчета (принято 0.85);\n'
                         f'      с - степень функции (вводимая величина).')
        BalloonTips(self.ent_ratio_laser_gas,
                    text=f'Коэффициент увеличения цены\n'
                         f'для газового лазера.\n\n'
                         f'Подразумевается, что для твердотельного\n'
                         f'лазера коэффициент равен 1.')
        BalloonTips(self.ent_ratio_rotation,
                    text=f'Коэффициент увеличения цены\n'
                         f'для гравировки на вращателе.')
        BalloonTips(self.ent_ratio_timing,
                    text=f'Коэффициент для работы в выходной день\n'
                         f'или работы сверх очереди.')
        BalloonTips(self.ent_ratio_attention,
                    text=f'Коэффициент для гравировки любых ювелирных\n'
                         f'изделий, а также других изделий (материалов),\n'
                         f'требующих особой осторожности.')
        BalloonTips(self.ent_ratio_packing,
                    text=f'Коэффициент, учитывающий большие\n'
                         f'затраты времени на распаковку/запаковку\n'
                         f'изделий.')
        BalloonTips(self.ent_ratio_hand_job,
                    text=f'Коэффициент, учитывающий шлифовку,\n'
                         f'снятие краски и др. виды работ,\n'
                         f'требующие больших временных затрат.')
        BalloonTips(self.ent_ratio_docking,
                    text=f'Коэффициент для гравировки со\n'
                         f'стыковкой элементов.')
        BalloonTips(self.ent_ratio_oversize,
                    text=f'Коэффициент, учитывающий, что для гравировки\n'
                         f'требуется снятие головы лазера.')
        BalloonTips(self.ent_ratio_different_layouts,
                    text=f'Коэффициент для гравировки разных макетов\n'
                         f'в рамках одной партии изделий.')
        BalloonTips(self.ent_ratio_numbering,
                    text=f'Коэффициент для гравировки партии\n'
                         f'со сквозной нумерацией (или другой'
                         f'нумерацией) с использование счетчика.')
        BalloonTips(self.ent_ratio_thermal_graving,
                    text=f'Коэффициент для гравировки термовлиянием.')
        BalloonTips(self.ent_ratio_taxation,
                    text=f'Коэффициент учета НДС при оплате\n'
                         f'по счету ООО и счету ИП.\n'
                         f'{"‾"*55}\n'
                         f'Порядок записи коэффициентов:\n'
                         f'1 - Значение для счета ООО;\n'
                         f'2 - Значение для счета ИП')
        BalloonTips(self.ent_gradation_difficult,
                    text=f'Ступенчатый коэффициент сложности гравировки.\n'
                         f'{"‾"*82}\n'
                         f'Коэффициент записывается по возрастанию\n'
                         f'в следующем порядке:\n'
                         f'1 - Привязка к 1 габариту или грани;\n'
                         f'2 - Привязка к координатному расположению,\n'
                         f'рамкам, базовым точкам, попадание по окружности;\n'
                         f'3 - Сложность пространственная: тяжело установить\n'
                         f'или прицелить изделие из-за его габаритов/формы;\n'
                         f'4 - Строгая привязка к параллельности и граням \n'
                         f'(Например, валы Маенкова);\n'
                         f'5 - Очень сложное выставление и привязка\n'
                         f'(Например гравировка на спиральном кольце \n'
                         f'на тонкой грани.'
                    )
        BalloonTips(self.ent_gradation_depth,
                    text=f'Ступенчатый коэффициент глубины гравировки.\n'
                         f'{"‾" * 75}\n'
                         f'Коэффициент записывается по возрастанию\n'
                         f'в следующем порядке:\n'
                         f'1 - Типовая гравировка до 25 проходов;\n'
                         f'2 - Гравировка до 50 проходов;\n'
                         f'3 - Гравировка  до 150 проходов;\n'
                         f'4 - Гравировка  до 300 проходов;\n'
                         f'5 - Гравировка  более 300 проходов.'
                    )
        BalloonTips(self.ent_gradation_area,
                    text=f'Коэффициент, учитывающий размер гравировки.\n'
                         f'{"‾" * 75}\n'
                         f'Записываются числа, учитывающие гравировку во\n'
                         f'все рабочее поле оборудования:\n'
                         f'1 - Коэффициент для твердотельного лазера;\n'
                         f'2 - Коэффициент для газового лазера.'
                    )
        BalloonTips(self.btn_default_settings,
                    text='Сброс настроек "по-умолчанию".')

        # Виджеты второй вкладки
        BalloonTips(self.ent_name,
                    text=f'Название изделия/работы.\n\n'
                    f'Выделите двойным нажатием строку в таблице,\n'
                    f'чтобы редактировать существующее изделие/работу.')
        BalloonTips(self.ent_cost,
                    text=f'Стоимость работы, руб.')
        BalloonTips(self.btn_delete_element,
                    text=f'Для удаления выделите строку в таблице.')

    def bind_treeview(self, event=None):
        try:  # Проверка на то, что пользователь выбрал материал
            data = self.standard_table.item(
                self.standard_table.focus())
            self.ent_name.delete(0, tk.END)
            self.ent_cost.delete(0, tk.END)
            BindEntry(self.ent_name, text=str(data["values"][0]))
            BindEntry(self.ent_cost, text=str(data["values"][1]))
        except (ValueError, KeyboardInterrupt, IndexError):
            self.ent_name.delete(0, tk.END)
            self.ent_cost.delete(0, tk.END)
            self.add_bind_entry()
        self.not_use = event

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
        self.config.read('settings/settings.ini', encoding='utf-8')

    def update_settings(self, some_new=None):  # Обновления файла конфигурации
        if some_new:
            with (open('settings/settings.ini', 'w', encoding='utf-8') as
                  configfile):
                some_new.write(configfile)
        else:
            with (open('settings/settings.ini', 'w', encoding='utf-8') as
                  configfile):
                self.config.write(configfile)

    @staticmethod
    def default_settings():  # Метод сброса настроек программы до базовых
        destination_path = 'settings/settings.ini'
        source_path = 'settings/default/settings.ini'
        if os.path.exists(destination_path):
            os.remove(destination_path)
        shutil.copy2(source_path, destination_path)


class RatioArea:
    def __init__(self, area_min, area_max, ratio_max, ratio_min=1):
        """
        Класс реализующий линейную и квадратичную зависимость для расчета
        коэффициента увеличения стоимости в зависимости от размеров
        гравировки.

        :param area_min: Максимальная площадь без доплаты
        :param area_max: Максимальная площадь полного поля станка
        :param ratio_max: Максимальный коэффициент для полного поля
        :param ratio_min: Минимальный коэффициент стандартной работы
        """
        self.area_min = area_min
        self.area_max = area_max
        self.ratio_max = ratio_max
        self.ratio_min = ratio_min

    def get_linear_ratio(self, area):  # Метод получения линейной зависимости
        """
        Обеспечение линейной зависимости по каноническому уравнению прямой
        :param area: Площадь гравировки
        :return: Коэффициент доплаты
        """
        try:
            if area <= self.area_min:
                return self.ratio_min
            elif area >= self.area_max:
                return self.ratio_max
            else:
                return (
                    (((area - self.area_min) * abs(
                        self.ratio_max-self.ratio_min)) / (
                        self.area_max - self.area_min)) + self.ratio_min
                )
        except TypeError:
            return 1

    def get_polynomial(self, area):  # Метод получения квадратичной зависимости
        """
        Обеспечение квадратичной зависимости для коэффициента
        :param area: Площадь гравировки
        :return: Коэффициент доплаты
        """
        if area <= self.area_min:
            return self.ratio_min
        elif area >= self.area_max:
            return self.ratio_max
        else:
            return (
                ((self.ratio_max - self.ratio_min) / (
                        (self.area_max - self.area_min) ** 2)) * (
                    (area - self.area_min) ** 2) + self.ratio_min
            )
