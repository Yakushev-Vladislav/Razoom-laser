"""
Программа создана для автоматизации многофункциональной работы операторов
специально по заказу компании "Разум".

"""

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askokcancel
from child_materials_window import ChildMaterials
from child_power_set_window import ChildPowerSet
from materials import Materials, Calculation
from child_config_window import ChildConfigSet
from child_config_window import ConfigSet
from math import ceil


class Window:
    def __init__(self):

        # Создание основного окна и его конфигурация
        self.root = tk.Tk()
        self.root.title("Расчет стоимости работы")
        self.root.option_add("*tearOff", False)
        self.root.iconbitmap("resources/Company_logo.ico")
        self.root.resizable(True, True)

        # Минимальные размеры окна и расположение
        self.root.geometry(f"{1000}x{650}+200+100")
        self.root.minsize(1000, 650)
        self.root.geometry("%dx%d" % (self.root.winfo_width(),
                                      self.root.winfo_height()))

        # Создание стиля и его конфигурация
        self.style = ttk.Style(self.root)
        self.theme = 'forest-light'
        self.root.tk.call("source", "resources/forest-dark.tcl")
        self.root.tk.call("source", "resources/forest-light.tcl")
        self.style.theme_use(self.theme)

        # Создание переменных
        self.main_settings = ConfigSet().config
        self.bool_rotation = tk.BooleanVar(value=False)
        self.bool_different = tk.BooleanVar(value=False)
        self.bool_1 = tk.BooleanVar(value=False)
        self.bool_2 = tk.BooleanVar(value=False)
        self.bool_3 = tk.BooleanVar(value=False)
        self.bool_4 = tk.BooleanVar(value=False)
        self.bool_5 = tk.BooleanVar(value=False)
        self.bool_6 = tk.BooleanVar(value=False)
        self.bool_7 = tk.BooleanVar(value=False)
        self.bool_8 = tk.BooleanVar(value=False)
        self.bool_9 = tk.BooleanVar(value=False)
        self.rb = tk.IntVar(value=1)
        self.not_use = None

        # Создание словаря для связи списка со стоимостями
        self.standard_items = {
            "Жетон/Брелок": "badge",
            "Кольцо": "ring",
            "Ручка": "pen",
            "Нож": "knife",
            "Термокружка/Термос": "thermos",
            "Клавиатура": "keyboard",
            "Клавиатура с пробелом": "personal_keyboard"
        }

        # Создание основных вкладок
        self.tabs_control = ttk.Notebook(self.root)
        self.tab_1 = ttk.Frame(self.tabs_control)
        self.tab_2 = ttk.Frame(self.tabs_control)

        # Конфигурация отзывчивости вкладок
        self.tab_1.columnconfigure(index=0, weight=1)
        self.tab_1.columnconfigure(index=1, weight=2)
        self.tab_1.rowconfigure(index=0, weight=4)
        self.tab_1.rowconfigure(index=1, weight=1)
        self.tab_1.rowconfigure(index=2, weight=4)

        self.tab_2.columnconfigure(index=0, weight=1)
        self.tab_2.columnconfigure(index=1, weight=50)
        self.tab_2.rowconfigure(index=0, weight=1)
        self.tab_2.rowconfigure(index=1, weight=4)

        # Добавление вкладок в набор
        self.tabs_control.add(self.tab_1, text='Расчет')
        self.tabs_control.add(self.tab_2, text='Листовой материал')
        # Упаковка вкладок
        self.tabs_control.pack(fill='both', expand=True)

        # ____________________1 ВКЛАДКА____________________

        # Создание формы для виджетов основного расчета
        self.panel_1 = ttk.Frame(self.tab_1, padding=(0, 0, 0, 0))
        self.panel_1.grid(row=0, column=0, padx=10, pady=(10, 0),
                          sticky="nsew", rowspan=1)

        # Создание формы для переключателей
        self.panel_2 = ttk.LabelFrame(
            self.tab_1,
            text="Углубленный расчет",
            padding=(20, 20)
        )
        self.panel_2.grid(row=0, column=1, padx=(10, 20), pady=(10, 5),
                          sticky="nsew")

        # Создание формы расчета по времени работы оборудования
        self.panel_3 = ttk.LabelFrame(
            self.tab_1,
            text="Время работы оборудования",
            padding=(20, 20)
        )
        self.panel_3.grid(row=2, column=0, padx=(10, 20), pady=(10, 20),
                          sticky="nsew")

        # Создание формы для вывода результатов
        self.panel_4 = ttk.LabelFrame(
            self.tab_1,
            text="Результаты расчета",
            padding=(20, 20)
        )
        self.panel_4.grid(row=2, column=1, padx=(10, 20), pady=(10, 20),
                          sticky="nsew")

        # Конфигурация форм
        self.panel_1.columnconfigure(index=0, weight=1)
        self.panel_1.columnconfigure(index=1, weight=2)
        self.panel_1.rowconfigure(index=0, weight=1)
        self.panel_1.rowconfigure(index=1, weight=1)
        self.panel_1.rowconfigure(index=2, weight=1)
        self.panel_1.rowconfigure(index=3, weight=1)
        self.panel_1.rowconfigure(index=4, weight=1)
        self.panel_1.rowconfigure(index=5, weight=1)
        self.panel_1.rowconfigure(index=6, weight=1)
        self.panel_1.rowconfigure(index=7, weight=1)
        self.panel_1.rowconfigure(index=8, weight=1)

        self.panel_2.columnconfigure(index=0, weight=1)
        self.panel_2.columnconfigure(index=1, weight=1)
        self.panel_2.rowconfigure(index=0, weight=2)
        self.panel_2.rowconfigure(index=1, weight=2)
        self.panel_2.rowconfigure(index=2, weight=2)
        self.panel_2.rowconfigure(index=3, weight=2)
        self.panel_2.rowconfigure(index=4, weight=2)
        self.panel_2.rowconfigure(index=5, weight=1)
        self.panel_2.rowconfigure(index=6, weight=1)
        self.panel_2.rowconfigure(index=7, weight=1)

        self.panel_3.columnconfigure(index=0, weight=1)
        self.panel_3.columnconfigure(index=1, weight=1)
        self.panel_3.rowconfigure(index=0, weight=1)
        self.panel_3.rowconfigure(index=1, weight=1)
        self.panel_3.rowconfigure(index=2, weight=1)

        # Создание выпадающего списка стандартных изделий
        ttk.Label(self.panel_1, text="Стандартное изделие:").grid(
            row=0, column=0, padx=10, pady=(5, 10), sticky='ns')
        self.combo_list = [
            "Нет",
            "Жетон/Брелок",
            "Кольцо",
            "Ручка",
            "Термокружка/Термос",
            "Нож",
            "Клавиатура",
            "Клавиатура с пробелом"
        ]
        self.combo_products = ttk.Combobox(
            self.panel_1,
            values=self.combo_list,
            width=20
        )
        self.combo_products.current(0)
        self.combo_products.grid(row=0, column=1, padx=5, pady=(5, 10),
                                 sticky="nsew", columnspan=1)

        # Создание переключателей выбора оборудования
        self.rbt_solid = ttk.Radiobutton(
            self.panel_1,
            text="Твердотельный лазер",
            variable=self.rb,
            value=1
        )
        self.rbt_solid.grid(row=1, column=0, padx=5, pady=(20, 5),
                            sticky="ns")
        self.rbt_co2 = ttk.Radiobutton(
            self.panel_1,
            text="СО2 лазер",
            variable=self.rb,
            value=2
        )
        self.rbt_co2.grid(row=1, column=1, padx=5, pady=(20, 5),
                          sticky="ns")

        # Подписи к формам ввода области гравировки
        ttk.Label(self.panel_1, text='Размер области гравировки').grid(
            row=2, column=0, columnspan=2, padx=5, pady=(0, 10), sticky='ns'
        )
        ttk.Label(self.panel_1, text='Ширина, мм.').grid(
            row=3, column=0, padx=5, pady=5, sticky='ns'
        )
        ttk.Label(self.panel_1, text='Высота, мм.').grid(
            row=3, column=1, padx=5, pady=5, sticky='ns'
        )

        # Поля ввода габаритов изделия
        self.ent_width_grav = ttk.Entry(self.panel_1, width=30)
        self.ent_width_grav.grid(
            row=4, column=0, padx=10, pady=0, sticky='nsew'
        )
        self.ent_height_grav = ttk.Entry(self.panel_1, width=30)
        self.ent_height_grav.grid(
            row=4, column=1, padx=10, pady=0, sticky='nsew'
        )

        # Переключатель вращателя/плоскости
        self.switch_rotation = ttk.Checkbutton(
            self.panel_1,
            text="Гравировка на вращателе",
            variable=self.bool_rotation,
            style="Switch"
        )
        self.switch_rotation.grid(
            row=5, column=0, padx=5, pady=20, sticky="ns")

        # Переключатель -Разные макеты-
        self.chk_different = ttk.Checkbutton(
            self.panel_1,
            text='Гравировка разных макетов',
            variable=self.bool_different,
            style="Switch"
        )
        self.chk_different.grid(row=5, column=1, padx=5, pady=5, sticky="ns")

        # Переключатель количества изделий
        ttk.Label(self.panel_1, text='Количество изделий:').grid(
            row=6, column=0, padx=0, pady=5, sticky='ns'
        )
        self.spin_number = ttk.Spinbox(self.panel_1, from_=1, to=10000)
        self.spin_number.insert(0, '1')
        self.spin_number.grid(
            row=6, column=1, padx=0, pady=5, sticky='ns'
        )

        # Переключатель количества прицелов
        ttk.Label(self.panel_1, text='Количество прицелов:').grid(
            row=7, column=0, padx=0, pady=5, sticky='ns'
        )
        self.spin_aim = ttk.Spinbox(self.panel_1, from_=1, to=10000)
        self.spin_aim.insert(0, '1')
        self.spin_aim.grid(
            row=7, column=1, padx=0, pady=5, sticky='ns'
        )

        # Кнопка запуска расчетов
        self.btn_calculate = ttk.Button(
            self.panel_1,
            text='Рассчитать стоимость',
            command=self.get_calc
        )
        self.btn_calculate.grid(
            row=8, column=0, padx=10, pady=20, sticky='nsew', columnspan=2
        )

        # Создание переключателей в форме углубленного расчета
        self.chk_1 = ttk.Checkbutton(
            self.panel_2,
            text='Срочность',
            variable=self.bool_1
        )
        self.chk_1.grid(row=0, column=0, padx=2, pady=5, sticky="nsew")

        self.chk_2 = ttk.Checkbutton(
            self.panel_2,
            text='Распаковка/Запаковка',
            variable=self.bool_2
        )
        self.chk_2.grid(row=0, column=1, padx=2, pady=5, sticky="nsew")

        self.chk_3 = ttk.Checkbutton(
            self.panel_2,
            text='Гравировка термовлиянием',
            variable=self.bool_3
        )
        self.chk_3.grid(row=1, column=0, padx=2, pady=5, sticky="nsew")

        self.chk_4 = ttk.Checkbutton(
            self.panel_2,
            text='Негабаритное изделие',
            variable=self.bool_4
        )
        self.chk_4.grid(row=1, column=1, padx=2, pady=5, sticky="nsew")

        self.chk_5 = ttk.Checkbutton(
            self.panel_2,
            text='Счетчик',
            variable=self.bool_5
        )
        self.chk_5.grid(row=2, column=0, padx=2, pady=5, sticky="nsew")

        self.chk_6 = ttk.Checkbutton(
            self.panel_2,
            text='Оплата с НДС',
            variable=self.bool_6
        )
        self.chk_6.grid(row=2, column=1, padx=2, pady=5, sticky="nsew")

        self.chk_7 = ttk.Checkbutton(
            self.panel_2,
            text='Повышенное внимание',
            variable=self.bool_7
        )
        self.chk_7.grid(row=3, column=0, padx=2, pady=5, sticky="nsew")

        self.chk_8 = ttk.Checkbutton(
            self.panel_2,
            text='Ручные работы',
            variable=self.bool_8
        )
        self.chk_8.grid(row=3, column=1, padx=2, pady=5, sticky="nsew")

        self.chk_9 = ttk.Checkbutton(
            self.panel_2,
            text='Стыковка элементов',
            variable=self.bool_9
        )
        self.chk_9.grid(row=4, column=0, padx=2, pady=5, sticky="nsew")

        # Переключатель сложности установки
        ttk.Label(self.panel_2, text='Сложность установки').grid(
            row=5, column=0, padx=(10, 0), pady=5, sticky='nsew'
        )
        self.spin_hard = ttk.Spinbox(self.panel_2, from_=1, to=5)
        self.spin_hard.insert(0, '1')
        self.spin_hard.configure(state='readonly')
        self.spin_hard.grid(
            row=5, column=1, padx=0, pady=5, sticky='nsew'
        )

        # Переключатель глубины гравировки
        ttk.Label(self.panel_2, text='Глубина гравировки').grid(
            row=6, column=0, padx=(10, 0), pady=5, sticky='nsew'
        )
        self.spin_deep = ttk.Spinbox(self.panel_2, from_=1, to=3)
        self.spin_deep.insert(0, '1')
        self.spin_deep.configure(state='readonly')
        self.spin_deep.grid(
            row=6, column=1, padx=0, pady=5, sticky='nsew'
        )

        # Окно ввода скидки оператора
        ttk.Label(self.panel_2, text='Скидка оператора, %').grid(
            row=7, column=0, padx=(10, 0), pady=0, sticky='nsew')
        self.ent_discount = ttk.Entry(self.panel_2, width=5)
        self.ent_discount.grid(row=7, column=1, padx=0, pady=5,
                               sticky='nsew')

        # Создание ползунка изменения размера
        self.sizegrip = ttk.Sizegrip(self.root)
        self.sizegrip.place(relx=0.972, rely=0.965)

        # Виджеты вывода результатов расчета
        self.lbl_result_0 = ttk.Label(
            self.panel_4,
            text=f"Стоимость работы:"
            f"  {0:.0f}  руб/шт."
        )
        self.lbl_result_0.grid(row=0, column=1, padx=(10, 10), pady=(0, 10),
                               sticky="nsew")
        self.lbl_result_7 = ttk.Label(
            self.panel_4,
            text=f"Стоимость всей работы:"
                 f"  {0:.0f}  руб."
        )
        self.lbl_result_7.grid(row=1, column=1, padx=(10, 10), pady=(0, 10),
                               sticky="nsew")

        # Виджеты времени работы оборудования
        ttk.Label(self.panel_3, text='Время работы, мин.').grid(
            row=0, column=0, padx=0, pady=0, sticky='ns')
        self.ent_time_of_work = ttk.Entry(self.panel_3, width=5)
        self.ent_time_of_work.grid(row=1, column=0, padx=10, pady=10,
                                   sticky='nsew')
        self.btn_time_calculate = ttk.Button(
            self.panel_3,
            text='Расчёт',
            command=self.get_time_calc
        )
        self.btn_time_calculate.grid(
            row=1, column=1, padx=10, pady=10, sticky='nsew')

        self.lbl_result_time = ttk.Label(
            self.panel_3,
            text=f"Стоимость работы: "
                 f" {0:.0f}  руб/шт."
        )
        self.lbl_result_time.grid(row=3, column=0, padx=(10, 10), pady=(0, 10),
                                  sticky="ns", columnspan=2)

        # ____________________2 ВКЛАДКА____________________
        # Создание формы для виджетов
        self.panel_2_1 = ttk.Frame(self.tab_2)
        self.panel_2_1.grid(row=0, column=1, padx=20, pady=(10, 10),
                            sticky="nsew")

        # Конфигурация формы виджетов
        self.panel_2_1.columnconfigure(index=0, weight=1)
        self.panel_2_1.columnconfigure(index=1, weight=1)
        self.panel_2_1.columnconfigure(index=2, weight=1)
        self.panel_2_1.columnconfigure(index=3, weight=1)
        self.panel_2_1.rowconfigure(index=0, weight=1)
        self.panel_2_1.rowconfigure(index=1, weight=1)
        self.panel_2_1.rowconfigure(index=2, weight=1)
        self.panel_2_1.rowconfigure(index=3, weight=1)

        # Создание формы для вывода результатов
        self.panel_2_2 = ttk.LabelFrame(self.tab_2, text='Результаты')
        self.panel_2_2.grid(row=1, column=1, padx=20, pady=30,
                            sticky="nsew")

        # Конфигурация формы для вывода результатов
        self.panel_2_2.columnconfigure(index=0, weight=1)
        self.panel_2_2.columnconfigure(index=1, weight=1)
        self.panel_2_2.rowconfigure(index=0, weight=1)
        self.panel_2_2.rowconfigure(index=1, weight=1)
        self.panel_2_2.rowconfigure(index=2, weight=1)
        self.panel_2_2.rowconfigure(index=3, weight=1)

        # Виджеты ввода количества изделий
        ttk.Label(self.panel_2_1, text='Количество изделий:').grid(
            row=0, column=0, padx=(0, 5), pady=10, sticky='nsew'
        )
        self.ent_num = ttk.Entry(self.panel_2_1, width=10)
        self.ent_num.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')
        ttk.Label(self.panel_2_1, text='шт.').grid(
            row=0, column=2, padx=15, pady=10, sticky='nsew'
        )

        # Получение материалов
        self.material_list = list()
        for n in Materials().get_mat():
            self.material_list.append(n)

        # Виджеты выбора материала
        ttk.Label(self.panel_2_1, text='Выберите материал:').grid(
            row=1, column=0, padx=(0, 5), pady=10, sticky='nsew'
        )
        self.combo_mat = ttk.Combobox(
            self.panel_2_1,
            width=35,
            height=5,
            values=self.material_list
        )
        self.combo_mat.current(0)
        self.combo_mat.grid(
            row=1, column=1, padx=10, pady=10, columnspan=4, sticky='nsew'
        )

        # Подписи для полей ввода габаритов изделия
        ttk.Label(self.panel_2_1, text='Введите габариты изделия:').grid(
            row=3, column=0, padx=(0, 5), pady=10, sticky='nsew')
        ttk.Label(self.panel_2_1, text='Ширина, мм').grid(
            row=2, column=1, padx=(10, 10), pady=5, sticky='ns')
        ttk.Label(self.panel_2_1, text='Высота, мм').grid(
            row=2, column=2, padx=(10, 10), pady=5, sticky='ns')

        # Поля ввода габаритов изделия
        self.ent_width = ttk.Entry(self.panel_2_1, width=20)
        self.ent_width.grid(row=3, column=1, padx=10, pady=10, sticky='nsew')
        self.ent_height = ttk.Entry(self.panel_2_1, width=20)
        self.ent_height.grid(row=3, column=2, padx=10, pady=10, sticky='nsew')

        # Кнопка запуска расчетов
        self.btn_materials = ttk.Button(
            self.panel_2_1,
            width=15,
            text="Рассчитать",
            command=self.get_calc_mat
        )
        self.btn_materials.grid(
            row=3, column=3, padx=10, pady=10, columnspan=3, sticky='nsew'
        )

        # Виджеты результатов расчета
        # Виджет -Себестоимость одного изделия-
        self.lbl_result_1 = ttk.Label(
            self.panel_2_2,
            text=f"Себестоимость одного изделия:"
                 f"  {0:.0f}  руб."
        )
        self.lbl_result_1.grid(
            row=3, column=0, padx=(40, 10), pady=(0, 20), sticky='nsew'
        )

        # Виджет -Себестоимость партии-
        self.lbl_result_2 = ttk.Label(
            self.panel_2_2,
            text=f"Себестоимость партии:"
                 f"  {0:.0f}  руб."
        )
        self.lbl_result_2.grid(
            row=3, column=1, padx=(40, 10), pady=(0, 20), sticky='nsew'
        )

        # Виджет -Количество изделий с одного листа-
        self.lbl_result_3 = ttk.Label(
            self.panel_2_2,
            text=f"Количество изделий с одного листа:"
                 f"  {0:.0f}  шт."
        )
        self.lbl_result_3.grid(
            row=1, column=0, padx=(40, 10), pady=0, sticky='nsew'
        )

        # Виджет -Количество листов на партию-
        self.lbl_result_4 = ttk.Label(
            self.panel_2_2,
            text=f"Минимальное количество листов на партию:"
                 f"  {0:.0f}  шт."
        )
        self.lbl_result_4.grid(
            row=1, column=1, padx=(40, 10), pady=0, sticky='nsew'
        )

        # Виджет -Стоимость одного изделия партии-
        self.lbl_result_5 = ttk.Label(
            self.panel_2_2,
            text=f"Стоимость изделия:"
                 f"  {0:.0f}  руб."
        )
        self.lbl_result_5.grid(
            row=0, column=0, padx=(40, 10), pady=0, sticky='nsew'
        )

        # Виджет -Стоимость партии-
        self.lbl_result_6 = ttk.Label(
            self.panel_2_2,
            text=f"Стоимость партии:"
                 f"  {0:.0f}  руб."
        )
        self.lbl_result_6.grid(
            row=0, column=1, padx=(40, 10), pady=0, sticky='nsew'
        )

        # Разделительная черта
        ttk.Separator(self.panel_2_2).grid(
            row=2, column=0, columnspan=2, pady=0, sticky='ew'
        )

        # Кнопка обновления списка материалов
        self.btn_update = ttk.Button(
            self.panel_2_1,
            width=15,
            text="Обновить список",
            command=self.update_base
        )
        self.btn_update.grid(
            row=0, column=3, padx=10, pady=10, columnspan=3, sticky='nsew'
        )

    def draw_menu(self):  # Метод прорисовки вкладок основного меню
        # Создаем полосу меню в окне
        menu_bar = tk.Menu(self.root)

        # Создаем первое подменю -Файл-
        file_menu = tk.Menu(menu_bar)
        file_menu.add_command(label='Сохранить отчет')
        file_menu.add_command(label='Подобрать режим',
                              command=self.power_set)
        file_menu.add_command(label='Листовой материал',
                              command=self.base_of_materials)
        file_menu.add_command(label='Предварительные настройки программы',
                              command=self.run_config_window)
        file_menu.add_separator()
        file_menu.add_command(label='Выход', command=self.destroy)

        # Создаем второе подменю -Вид-
        view_menu = tk.Menu(menu_bar)
        view_menu.add_checkbutton(
            label='Темная тема',
            onvalue=1,
            offvalue=0,
            command=self.change_theme)

        # Создаем третье подменю
        help_menu = tk.Menu(menu_bar)
        help_menu.add_command(label='Справка')
        help_menu.add_separator()
        help_menu.add_command(label='О программе')

        # Конфигурация подменю и меню
        menu_bar.add_cascade(label='Файл', menu=file_menu)
        menu_bar.add_cascade(label='Вид', menu=view_menu)
        menu_bar.add_cascade(label='Помощь', menu=help_menu)
        menu_bar.add_command(label='Обновить', command=self.settings_update)
        self.root.configure(menu=menu_bar)

    def settings_update(self):
        self.main_settings = ConfigSet().config
        self.root.update()

    def run_child_materials(self):  # Открытие дочернего окна листового мат-ла.
        self.root.CHILD = ChildMaterials(
            self.root,
            820,
            500,
            theme=self.theme,
            icon="resources/Company_logo.ico"
        )
        self.root.CHILD.add_bind_child()
        self.root.CHILD.grab_focus()

    def run_child_power(self):  # Открытие дочернего окна подбора режимов
        self.root.CHILD = ChildPowerSet(
            self.root,
            540,
            450,
            theme=self.theme,
            icon="resources/Company_logo.ico"
        )
        self.root.CHILD.grab_focus()

    def run_config_window(self):
        self.root.CHILD = ChildConfigSet(
            self.root,
            700,
            450,
            standard=self.standard_items,
            theme=self.theme,
            icon="resources/Company_logo.ico"
        )
        self.root.CHILD.grab_focus()

    def base_of_materials(self):  # Запуск дочернего окна листового материала
        self.run_child_materials()

    def power_set(self):  # Запуск дочернего окна подбора режимов
        self.run_child_power()

    def configure_program(self):  # Запуск дочернего окна настроек программы
        self.run_config_window()

    def change_theme(self):  # Метод смены темы приложения
        if self.theme == 'forest-light':
            self.theme = 'forest-dark'
            self.style.theme_use(self.theme)
        else:
            self.theme = 'forest-light'
            self.style.theme_use(self.theme)
        self.root.update()

    def get_time_calc(self):
        try:  # Проверяем на то, что введено корректное число
            cost = (
                float(self.ent_time_of_work.get()) *
                int(self.main_settings['MAIN']['one_hour_of_work']) / 60

            )

            self.lbl_result_time.config(
                text=f"Стоимость работы:"
                     f"  {self.round_result(cost):.0f}  руб/шт."
            )

        except ValueError:  # Если число некорректно
            self.lbl_result_time.config(
                text=f"Стоимость работы:"
                     f"  {0:.0f}  руб/шт."
            )

    def get_calc(self):  # Метод основного и углубленного расчета

        # Формирование начальной стоимости
        if self.combo_products.get() == "Нет":  # Если не выбрано изделие
            cost = int(self.main_settings["MAIN"]["min_cost"])
        else:  # Если выбрано стандартное изделие
            cost = int(
                self.main_settings["STANDARD"][
                    self.standard_items[self.combo_products.get()]]
            )
        # Формирование значений коэффициентов
        """
        !!На будущее!! Здесь везде идет присвоение, а значит можно было 
        использовать тернарный IF, но это сильно усложняет читаемость.
        Вот пример:
        
        # Коэффициент ratio_laser __Тип лазера__
        ratio_laser = float(self.main_settings["RATIO_SETTINGS"][
                                "ratio_laser_gas"]) if (self.rb.get() == 2) \
            else float(self.main_settings["RATIO_SETTINGS"][
                           "ratio_laser_diode"])

        # Коэффициент ratio_rotation __Вращатель__
        ratio_rotation = float(self.main_settings["RATIO_SETTINGS"][
                                   "ratio_rotation"]) if (
            self.bool_rotation.get()) else 1
        """
        # Коэффициент ratio_laser __Тип лазера__
        if self.rb.get() == 2:  # Если газовый лазер
            ratio_laser = float(self.main_settings[
                "RATIO_SETTINGS"]["ratio_laser_gas"])
        else:  # Если твердотельный лазер
            ratio_laser = float(self.main_settings[
                "RATIO_SETTINGS"]["ratio_laser_diode"])

        # Коэффициент ratio_rotation __Вращатель__
        if self.bool_rotation.get():  # Если гравировка с вращением
            ratio_rotation = float(self.main_settings[
                "RATIO_SETTINGS"]["ratio_rotation"])
        else:  # Если гравировка без вращения
            ratio_rotation = 1

        # Коэффициент ratio_different_layouts __Разные макеты__
        if self.bool_different.get() and (
                int(self.spin_number.get()) > 1):  # Если разные макеты
            ratio_different_layouts = float(
                self.main_settings["RATIO_SETTINGS"][
                    "ratio_different_layouts"])
        else:  # Если один макет
            ratio_different_layouts = 1

        # Коэффициент ratio_timing __Срочность__
        if self.bool_1.get():
            ratio_timing = float(self.main_settings["RATIO_SETTINGS"][
                "ratio_timing"])
        else:
            ratio_timing = 1

        # Коэффициент ratio_packing __Распаковка/Запаковка__
        if self.bool_2.get():
            ratio_packing = float(self.main_settings["RATIO_SETTINGS"][
                "ratio_packing"])
        else:
            ratio_packing = 1

        # Коэффициент ratio_thermal_graving __Гравировка термовлиянием__
        if self.bool_3.get():
            ratio_thermal_graving = float(self.main_settings["RATIO_SETTINGS"][
                "ratio_thermal_graving"])
        else:
            ratio_thermal_graving = 1

        # Коэффициент ratio_oversize __Негабаритное изделие__
        if self.bool_4.get():
            ratio_oversize = float(self.main_settings["RATIO_SETTINGS"][
                "ratio_oversize"])
        else:
            ratio_oversize = 1

        # Коэффициент ratio_numbering __Счетчик__
        if self.bool_5.get() and (int(self.spin_number.get()) > 1):
            ratio_numbering = float(self.main_settings["RATIO_SETTINGS"][
                "ratio_numbering"])
        else:
            ratio_numbering = 1

        # Коэффициент ratio_taxation __Оплата с НДС__
        if self.bool_6.get():
            ratio_taxation = float(self.main_settings["RATIO_SETTINGS"][
                "ratio_taxation"])
        else:
            ratio_taxation = 1

        # Коэффициент ratio_attention __Повышенное внимание__
        if self.bool_7.get():
            ratio_attention = float(self.main_settings["RATIO_SETTINGS"][
                "ratio_attention"])
        else:
            ratio_attention = 1

        # Коэффициент ratio_hand_job __Ручные работы__
        if self.bool_8.get():
            ratio_hand_job = float(self.main_settings["RATIO_SETTINGS"][
                "ratio_hand_job"])
        else:
            ratio_hand_job = 1

        # Коэффициент ratio_docking __Стыковка элементов__
        if self.bool_9.get() and int(self.spin_aim.get()) > 1:
            ratio_docking = float(self.main_settings["RATIO_SETTINGS"][
                "ratio_docking"])
        else:
            ratio_docking = 1

        # Дополнительная стоимость за количество установок
        if int(self.spin_aim.get()) > 1:
            additional_cost = (
                (int(self.spin_aim.get()) - 1) *
                int(self.main_settings["MAIN"]["additional_cost"]))
        else:
            additional_cost = 0

        # Коэффициент зависимости от количества изделий
        ratio_many_items = int(self.spin_number.get()) ** (
            -float(self.main_settings["MAIN"]["many_items"]))

        # Скидка оператора
        try:
            ratio_discount = 1 - float(self.ent_discount.get()) / 100
        except ValueError:
            ratio_discount = 1

        # Расчет основной стоимости
        """
        Формула имеет следующий вид:
        Итоговая цена = (дополнительные прицелы + 
        + минимальная стоимость * коэффициенты) * учет НДС * учет скидки * 
        * учет количества изделий
        """
        main_cost = ((additional_cost + (cost * (
                ratio_laser * ratio_rotation * ratio_different_layouts *
                ratio_timing * ratio_packing * ratio_thermal_graving *
                ratio_oversize * ratio_numbering * ratio_attention *
                ratio_hand_job * ratio_docking)))
                     * ratio_taxation * ratio_many_items * ratio_discount)

        self.lbl_result_0.config(
            text=f"Стоимость работы:"
            f"  {self.round_result(main_cost):.0f}  руб/шт."
        )
        all_cost = self.round_result(main_cost) * int(self.spin_number.get())
        self.lbl_result_7.config(
            text=f"Стоимость всей работы:"
                 f"  {all_cost:.0f}  руб."
        )

    def get_calc_mat(self):  # Метод расчета себестоимости изделий

        # Получение данных с интерфейса
        material_name = self.combo_mat.get()
        number_of_products = self.ent_num.get()
        gab_width = self.ent_width.get()
        gab_height = self.ent_height.get()

        # Проверка введенных данных
        if (number_of_products.isdigit() is False) or (
                gab_width.isdigit() is False) or (
                gab_height.isdigit() is False):
            pass

        else:  # Если поля заполнены верно, выполняем расчет
            # Переводим данные в число
            number_of_products = int(number_of_products)
            gab_width = int(gab_width)
            gab_height = int(gab_height)

            # Подсчет результатов
            # Количество изделий с листа
            total_3 = max(
                Calculation(gab_width, gab_height, material_name).figure_1(),
                Calculation(gab_width, gab_height, material_name).figure_2()
            )

            # Себестоимость одного изделия
            total_1 = Calculation(
                gab_width, gab_height, material_name).get_price() / total_3

            # Себестоимость партии
            total_2 = total_1 * number_of_products

            # Потребное количество листов на партию
            total_4 = ceil(number_of_products / total_3)

            # Вывод результатов
            self.lbl_result_1.config(
                text=f"Себестоимость одного изделия:"
                     f"  {total_1:.0f}  руб."
            )
            self.lbl_result_2.config(
                text=f"Себестоимость партии:"
                     f"  {total_2:.0f}  руб."
            )
            self.lbl_result_3.config(
                text=f"Количество изделий с одного листа:"
                     f"  {total_3:.0f}  шт."
            )
            self.lbl_result_4.config(
                text=f"Количество листов на партию:"
                     f"  {total_4:.0f}  шт."
            )

    def update_base(self):  # Метод обновления списка листового материала
        self.material_list = list()
        for n in Materials().get_mat():
            self.material_list.append(n)
        self.combo_mat['values'] = self.material_list
        self.tab_2.update()
        self.root.update()

    @staticmethod
    def round_result(cost):  # Метод округления результатов расчета
        # Непосредственно округление
        if cost >= 800:
            return round(cost/50) * 50

        elif 250 <= cost < 800:
            return round(cost/10) * 10
        elif 85 <= cost < 250:
            return round(cost/5) * 5
        else:
            return cost

    def add_bind(self):  # Установка фонового текста в полях ввода (binds)
        self.to_add_entry()
        self.to_add_entry1()
        self.to_add_entry2()
        self.to_add_entry3()
        self.to_add_entry4()
        self.to_add_entry5()
        self.to_add_entry6()

        self.ent_width_grav.bind('<FocusIn>', self.erase_entry)
        self.ent_width_grav.bind('<FocusOut>', self.to_add_entry)

        self.ent_height_grav.bind('<FocusIn>', self.erase_entry1)
        self.ent_height_grav.bind('<FocusOut>', self.to_add_entry1)

        self.ent_num.bind('<FocusIn>', self.erase_entry2)
        self.ent_num.bind('<FocusOut>', self.to_add_entry2)

        self.ent_width.bind('<FocusIn>', self.erase_entry3)
        self.ent_width.bind('<FocusOut>', self.to_add_entry3)

        self.ent_height.bind('<FocusIn>', self.erase_entry4)
        self.ent_height.bind('<FocusOut>', self.to_add_entry4)

        self.ent_time_of_work.bind('<FocusIn>', self.erase_entry5)
        self.ent_time_of_work.bind('<FocusOut>', self.to_add_entry5)

        self.ent_discount.bind('<FocusIn>', self.erase_entry6)
        self.ent_discount.bind('<FocusOut>', self.to_add_entry6)

    def erase_entry(self, event=None):
        if self.ent_width_grav.get() == '-':
            self.ent_width_grav.delete(0, 'end')
        self.not_use = event

    def erase_entry1(self, event=None):
        if self.ent_height_grav.get() == '-':
            self.ent_height_grav.delete(0, 'end')
        self.not_use = event

    def erase_entry2(self, event=None):
        if self.ent_num.get() == '-':
            self.ent_num.delete(0, 'end')
        self.not_use = event

    def erase_entry3(self, event=None):
        if self.ent_width.get() == '-':
            self.ent_width.delete(0, 'end')
        self.not_use = event

    def erase_entry4(self, event=None):
        if self.ent_height.get() == '-':
            self.ent_height.delete(0, 'end')
        self.not_use = event

    def erase_entry5(self, event=None):
        if self.ent_time_of_work.get() == '-':
            self.ent_time_of_work.delete(0, 'end')
        self.not_use = event

    def erase_entry6(self, event=None):
        if self.ent_discount.get() == '-':
            self.ent_discount.delete(0, 'end')
        self.not_use = event

    def to_add_entry(self, event=None):
        if self.ent_width_grav.get() == "":
            self.ent_width_grav.insert(0, '-')
        self.not_use = event

    def to_add_entry1(self, event=None):
        if self.ent_height_grav.get() == "":
            self.ent_height_grav.insert(0, '-')
        self.not_use = event

    def to_add_entry2(self, event=None):
        if self.ent_num.get() == "":
            self.ent_num.insert(0, '-')
        self.not_use = event

    def to_add_entry3(self, event=None):
        if self.ent_width.get() == "":
            self.ent_width.insert(0, '-')
        self.not_use = event

    def to_add_entry4(self, event=None):
        if self.ent_height.get() == "":
            self.ent_height.insert(0, '-')
        self.not_use = event

    def to_add_entry5(self, event=None):
        if self.ent_time_of_work.get() == "":
            self.ent_time_of_work.insert(0, '-')
        self.not_use = event

    def to_add_entry6(self, event=None):
        if self.ent_discount.get() == "":
            self.ent_discount.insert(0, '-')
        self.not_use = event

    def run(self):  # Метод, реализующий запуск программы
        # Удаление пустых строк из файла перед запуском
        with open("resources/materials_data.txt", 'r') as f1:
            lines = f1.readlines()
        new_lines = list()
        for line in lines:
            if len(line.strip()):
                new_lines.append(line)
        with open("resources/materials_data.txt", 'w') as f2:
            f2.writelines(new_lines)

        # Прорисовка виджетов и окна
        self.add_bind()
        self.draw_menu()
        self.root.mainloop()

    def destroy(self):  # Метод, реализующий закрытие программы
        choice = askokcancel('Выход', 'Вы действительно хотите выйти?')
        if choice:
            self.root.destroy()


if __name__ == "__main__":  # Запуск программы
    window = Window()
    window.run()
