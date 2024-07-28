import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askokcancel
import configparser


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
        self.child_root.geometry(f"{width}x{height}+100+100")
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
        self.tab_1 = ttk.Frame(self.child_tabs_control)
        self.tab_2 = ttk.Frame(self.child_tabs_control)
        self.tab_3 = ttk.Frame(self.child_tabs_control)

        # Конфигурация отзывчивости вкладок окна
        self.tab_1.columnconfigure(index=0, weight=1)
        self.tab_1.columnconfigure(index=1, weight=1)
        self.tab_1.columnconfigure(index=2, weight=1)
        self.tab_1.columnconfigure(index=3, weight=1)
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
        self.tab_2_panel_2.rowconfigure(index=0, weight=1)
        self.tab_2_panel_2.rowconfigure(index=1, weight=1)
        self.tab_2_panel_2.rowconfigure(index=2, weight=1)
        self.tab_2_panel_2.rowconfigure(index=3, weight=1)
        self.tab_2_panel_2.rowconfigure(index=4, weight=1)

        # Добавление вкладок в набор
        self.child_tabs_control.add(self.tab_1, text='Частные лица')
        self.child_tabs_control.add(self.tab_2, text='Стандартные изделия')
        self.child_tabs_control.add(self.tab_3, text='Оптовый расчет')

        # Упаковка вкладок
        self.child_tabs_control.pack(fill='both', expand=True)

        # ___ Создание виджетов 1 вкладки ___
        # Информация по первому блоку
        ttk.Label(self.tab_1, text='Блок настройки базовых цен, руб.',
                  foreground='red').grid(
            row=0, column=0, padx=0, pady=0, sticky='ns', columnspan=4
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
        self.ent_one_hour = ttk.Entry(
            self.tab_1,
            width=20
        )
        self.ent_one_hour.grid(row=2, column=2, padx=5, pady=5,
                               sticky='nsew')

        # Окно ввода __ Степень градации __
        ttk.Label(self.tab_1, text='Степень градации').grid(
            row=1, column=3, padx=0, pady=0, sticky='ns'
        )
        self.ent_many_items = ttk.Entry(
            self.tab_1,
            width=20
        )
        self.ent_many_items.grid(row=2, column=3, padx=5, pady=5,
                                 sticky='nsew')

        # Разделительная черта
        ttk.Separator(self.tab_1).grid(
            row=3, column=0, columnspan=4, pady=0, sticky='ew'
        )

        # Информация по второму блоку
        ttk.Label(self.tab_1,
                  text='Блок настройки весовых коэффициентов',
                  foreground='red').grid(
            row=4, column=0, padx=0, pady=0, sticky='ns', columnspan=4
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

        # Окно ввода ratio_attention __Повышенное внимание__
        ttk.Label(self.tab_1, text='Повышенное внимание').grid(
            row=5, column=3, padx=0, pady=0, sticky='ns'
        )
        self.ent_ratio_attention = ttk.Entry(
            self.tab_1,
            width=20
        )
        self.ent_ratio_attention.grid(row=6, column=3, padx=5, pady=5,
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

        # Окно ввода ratio_hand_job __Ручные работы__
        ttk.Label(self.tab_1, text='Ручные работы').grid(
            row=7, column=1, padx=0, pady=0, sticky='ns'
        )
        self.ent_ratio_hand_job = ttk.Entry(
            self.tab_1,
            width=20
        )
        self.ent_ratio_hand_job.grid(row=8, column=1, padx=5, pady=5,
                                     sticky='nsew')

        # Окно ввода ratio_docking __Стыковка элементов__
        ttk.Label(self.tab_1, text='Стыковка элементов').grid(
            row=7, column=2, padx=0, pady=0, sticky='ns'
        )
        self.ent_ratio_docking = ttk.Entry(
            self.tab_1,
            width=20
        )
        self.ent_ratio_docking.grid(row=8, column=2, padx=5, pady=5,
                                    sticky='nsew')

        # Окно ввода ratio_oversize __Негабаритное изделие__
        ttk.Label(self.tab_1, text='Негабаритное изделие').grid(
            row=7, column=3, padx=0, pady=0, sticky='ns'
        )
        self.ent_ratio_oversize = ttk.Entry(
            self.tab_1,
            width=20
        )
        self.ent_ratio_oversize.grid(row=8, column=3, padx=5, pady=5,
                                     sticky='nsew')

        # Окно ввода ratio_different_layouts __Разные макеты__
        ttk.Label(self.tab_1, text='Разные макеты').grid(
            row=9, column=0, padx=0, pady=0, sticky='ns'
        )
        self.ent_ratio_different_layouts = ttk.Entry(
            self.tab_1,
            width=20
        )
        self.ent_ratio_different_layouts.grid(row=10, column=0, padx=5, pady=5,
                                              sticky='nsew')
        # Окно ввода ratio_numbering __Счетчик__
        ttk.Label(self.tab_1, text='Счетчик').grid(
            row=9, column=1, padx=0, pady=0, sticky='ns'
        )
        self.ent_ratio_numbering = ttk.Entry(
            self.tab_1,
            width=20
        )
        self.ent_ratio_numbering.grid(row=10, column=1, padx=5, pady=5,
                                      sticky='nsew')

        # Окно ввода ratio_thermal_graving __Гравировка термовлиянием__
        ttk.Label(self.tab_1, text='Термовлияние').grid(
            row=9, column=2, padx=0, pady=0, sticky='ns'
        )
        self.ent_ratio_thermal_graving = ttk.Entry(
            self.tab_1,
            width=20
        )
        self.ent_ratio_thermal_graving.grid(row=10, column=2, padx=5, pady=5,
                                            sticky='nsew')

        # Окно ввода ratio_taxation __Оплата с НДС__
        ttk.Label(self.tab_1, text='Оплата по счету: ООО, ИП').grid(
            row=9, column=3, padx=0, pady=0, sticky='ns'
        )
        self.ent_ratio_taxation = ttk.Entry(
            self.tab_1,
            width=20
        )
        self.ent_ratio_taxation.grid(row=10, column=3, padx=5, pady=5,
                                     sticky='nsew')

        # Окно ввода gradation_difficult __Сложность установки__
        ttk.Label(self.tab_1, text='Сложность установки').grid(
            row=11, column=0, padx=0, pady=0, sticky='ns', columnspan=1
        )
        self.ent_gradation_difficult = ttk.Entry(
            self.tab_1,
            width=20
        )
        self.ent_gradation_difficult.grid(row=12, column=0, padx=5, pady=5,
                                          sticky='nsew', columnspan=1)

        # Окно ввода gradation_depth __Глубина гравировки__
        ttk.Label(self.tab_1, text='Глубина гравировки').grid(
            row=11, column=1, padx=0, pady=0, sticky='ns', columnspan=1
        )
        self.ent_gradation_depth = ttk.Entry(
            self.tab_1,
            width=20
        )
        self.ent_gradation_depth.grid(row=12, column=1, padx=5, pady=5,
                                      sticky='nsew', columnspan=1)

        # Окно ввода gradation_area __Коэффициенты площади__
        ttk.Label(self.tab_1, text='Коэффициенты площади').grid(
            row=11, column=2, padx=0, pady=0, sticky='ns', columnspan=1
        )
        self.ent_gradation_area = ttk.Entry(
            self.tab_1,
            width=20
        )
        self.ent_gradation_area.grid(row=12, column=2, padx=5, pady=5,
                                     sticky='nsew', columnspan=1)

        # Разделительная черта
        ttk.Separator(self.tab_1).grid(
            row=13, column=0, columnspan=4, pady=5, sticky='ew'
        )

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

        # Создание кнопки сброса настроек "По умолчанию"
        self.btn_default_settings = ttk.Button(
            self.tab_1,
            width=10,
            text="Сбросить настройки",
            command=self.click_default_settings
        )
        self.btn_default_settings.grid(
            row=14, column=2, padx=5, pady=10, sticky='nsew'
        )

        # Создание кнопки закрытия дочернего окна
        self.btn_destroy = ttk.Button(
            self.tab_1,
            width=10,
            text="Выход",
            command=self.destroy_child
        )
        self.btn_destroy.grid(
            row=14, column=3, padx=5, pady=10, sticky='nsew'
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
        self.data_table = self.get_standard_costs()
        for data in self.data_table:
            self.standard_table.insert('', index='end', values=data)

        # Окно ввода __ Название работы __
        ttk.Label(self.tab_2_panel_2, text='Название работы').grid(
            row=0, column=0, padx=0, pady=(5, 0), sticky='ns'
        )
        self.ent_name = ttk.Entry(
            self.tab_2_panel_2,
            width=20
        )
        self.ent_name.grid(row=1, column=0, padx=5, pady=(5, 10),
                           sticky='nsew', columnspan=1)

        # Окно ввода __ Стоимость работы __
        ttk.Label(self.tab_2_panel_2,
                  text='Стоимость работы').grid(
            row=0, column=1, padx=0, pady=5, sticky='ns'
        )
        self.ent_cost = ttk.Entry(
            self.tab_2_panel_2,
            width=20
        )
        self.ent_cost.grid(row=1, column=1, padx=5, pady=(5, 10),
                           sticky='nsew')

        # Создание кнопки добавления работы
        self.btn_add_new_element = ttk.Button(
            self.tab_2_panel_2,
            width=10,
            text="Добавить работу",
            command=self.click_add_standard
        )
        self.btn_add_new_element.grid(
            row=1, column=2, padx=5, pady=(5, 10), sticky='nsew', columnspan=1)

        # Разделительная черта
        ttk.Separator(self.tab_2_panel_2).grid(
            row=2, column=0, columnspan=4, pady=5, sticky='ew'
        )

        # Окно ввода __ Номер удаляемой строки __
        ttk.Label(self.tab_2_panel_2,
                  text='Название удаляемого элемента').grid(
            row=3, column=0, padx=0, pady=0, sticky='ns'
        )
        self.ent_delete_element = ttk.Entry(
            self.tab_2_panel_2,
            width=10
        )
        self.ent_delete_element.grid(row=4, column=0, padx=5, pady=(10, 20),
                                     sticky='nsew')

        # Создание кнопки удаления работы
        self.btn_delete_element = ttk.Button(
            self.tab_2_panel_2,
            width=10,
            text="Удалить элемент",
            command=self.click_delete_element
        )
        self.btn_delete_element.grid(
            row=4, column=1, padx=5, pady=(10, 20), sticky='nsew')

        # Создание кнопки перехода на начальную вкладку
        self.btn_back_to_tab_1 = ttk.Button(
            self.tab_2_panel_2,
            width=10,
            text="Вернуться",
            command=self.click_back
        )
        self.btn_back_to_tab_1.grid(
            row=4, column=2, padx=5, pady=(10, 20), sticky='nsew')

        # Запись данных в окна ввода
        self.update_data_in_widgets()
        self.add_bind_entry()

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

        self.data_table = self.get_standard_costs()
        for data in self.data_table:
            self.standard_table.insert('', index='end', values=data)

        # Очистка полей ввода второй вкладки
        self.ent_name.delete(0, tk.END)
        self.ent_cost.delete(0, tk.END)
        self.ent_delete_element.delete(0, tk.END)

        self.to_add_entry()
        self.to_add_entry1()
        self.to_add_entry2()

        del (update_config, ratio_from_config, main_from_config,
             gradation_from_config)

    def get_standard_costs(self):  # Метод получения данных для таблицы
        table_data = list()
        # Считывание информации из конфига
        costs = self.child_temp_config.config["STANDARD"]
        for k, v in costs.items():
            temp = [k, v]
            table_data.append(temp)
        return table_data

    def click_back(self):  # Метод возвращения на первую вкладку
        self.child_tabs_control.select(self.tab_1)

    def click_add_standard(self):  # Метод добавления новой стандартной работы
        # Создание переменной конфигурации
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
        self.update_data_in_widgets()
        self.child_root.update()

    def click_delete_element(self):  # Метод удаления стандартной работы
        # Создаем переменную конфигурации
        config_with_deleted_item = self.child_temp_config.config

        # Считывание данных из окна ввода и удаление выбранного элемента
        config_with_deleted_item.remove_option(
            'STANDARD', self.ent_delete_element.get()
        )

        # Обновление данных в файле
        self.child_temp_config.update_settings(
            some_new=config_with_deleted_item)

        # Обновление данных в таблице
        self.update_data_in_widgets()

        del config_with_deleted_item

    def add_bind_entry(self):  # Установка фонового текста в полях ввода
        self.to_add_entry()
        self.to_add_entry1()
        self.to_add_entry2()

        self.ent_cost.bind('<FocusIn>', self.erase_entry)
        self.ent_cost.bind('<FocusOut>', self.to_add_entry)

        self.ent_name.bind('<FocusIn>', self.erase_entry1)
        self.ent_name.bind('<FocusOut>', self.to_add_entry1)

        self.ent_delete_element.bind('<FocusIn>', self.erase_entry2)
        self.ent_delete_element.bind('<FocusOut>', self.to_add_entry2)

    def erase_entry(self, event=None):
        if self.ent_cost.get() == '-':
            self.ent_cost.delete(0, 'end')
        self.not_use = event

    def erase_entry1(self, event=None):
        if self.ent_name.get() == '-':
            self.ent_name.delete(0, 'end')
        self.not_use = event

    def erase_entry2(self, event=None):
        if self.ent_delete_element.get() == '-':
            self.ent_delete_element.delete(0, 'end')
        self.not_use = event

    def to_add_entry(self, event=None):
        if self.ent_cost.get() == "":
            self.ent_cost.insert(0, '-')
        self.not_use = event

    def to_add_entry1(self, event=None):
        if self.ent_name.get() == "":
            self.ent_name.insert(0, '-')
        self.not_use = event

    def to_add_entry2(self, event=None):
        if self.ent_delete_element.get() == "":
            self.ent_delete_element.insert(0, '-')
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
        # Формирование переменной базовой конфигурации
        string_config = """
        [INFO]
        
        [MAIN]
        min_cost = 1000
        additional_cost = 400
        one_hour_of_work = 5000
        many_items = 0.42
        
        [STANDARD]
        Кольцо = 1400
        Кольцо с 2-х сторон = 2200
        Нож = 1000
        Ручка = 1000
        Жетон/Брелок = 1000
        Термос/Термокружка = 1000
        Клавиатура = 1500
        Клавиатура с пробелом = 2000
        
        [RATIO_SETTINGS]
        ratio_laser_gas = 1.15
        ratio_rotation = 1.2
        ratio_timing = 1.5
        ratio_attention = 1.15
        ratio_packing = 1.15
        ratio_hand_job = 1.15
        ratio_taxation = 1.2, 1.07
        ratio_oversize = 1.8
        ratio_different_layouts = 1.15
        ratio_numbering = 1.1
        ratio_thermal_graving = 1.15
        ratio_docking = 1.15
        
        [GRADATION]
        difficult = 1, 1.2, 1.3, 1.5, 1.8
        depth = 1, 1.15, 1.3, 1.5, 2
        area = 1.5, 7
        
        [INDUSTRIAL_MAIN]
        industrial__hour_of_work = 4000
        industrial_all_area_cost = 1500
        industrial_timing_correction = 0.96
        
        [RATIO_INDUSTRIAL_SETTINGS]
        industrial_ratio_laser_gas = 1.15
        industrial_ratio_rotation = 1.2
        industrial_ratio_timing = 1.5
        industrial_ratio_attention = 1.15
        industrial_ratio_packing = 1.15
        industrial_ratio_hand_job = 1.15
        industrial_ratio_taxation = 1.2, 1.07
        industrial_ratio_oversize = 1.8
        industrial_ratio_different_layouts = 1.15
        industrial_ratio_numbering = 1.1
        industrial_ratio_thermal_graving = 1.15
        industrial_ratio_docking = 1.15
        
        [INDUSTRIAL_GRADATION]
        industrial_difficult = 1, 1.3, 1.5, 1.8, 2.0
        industrial_depth = 1, 1.3, 1.5, 2, 3
        industrial_area = 1, 1.15, 1.2, 1.5
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
        with (open('settings/settings.ini', 'w', encoding='utf-8') as
              configfile):
            default_config.write(configfile)


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
