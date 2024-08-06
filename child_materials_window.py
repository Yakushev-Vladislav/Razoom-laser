import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import askokcancel
from materials import Materials
from binds import BindEntry
from binds import BalloonTips


class ChildMaterials:
    def __init__(self, parent, width, height, theme, title='Листовой материал',
                 resizable=(False, False), icon=None):
        """
        Дочернее окно редактирования базы листового материала.
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

        # Создание переменной, хранящей массив данных для таблицы
        self.data = []

        # Создание переменной конфигурации
        self.config_material_data = Materials()

        # Создание переменной для исключения ошибок 'event' value is not use
        self.not_use_child = None

        # Конфигурация отзывчивости окна
        self.child_root.columnconfigure(index=0, weight=1)
        self.child_root.columnconfigure(index=1, weight=50)
        self.child_root.columnconfigure(index=2, weight=1)
        self.child_root.rowconfigure(index=0, weight=1)
        self.child_root.rowconfigure(index=1, weight=2)

        # Создание формы для основных виджетов
        self.panel_settings = ttk.Frame(self.child_root, padding=(0, 0, 0, 0))
        self.panel_settings.grid(row=1, column=0, padx=0, pady=(0, 0),
                                 sticky="nsew", columnspan=3)
        # Конфигурация формы виджетов
        self.panel_settings.columnconfigure(index=0, weight=1)
        self.panel_settings.columnconfigure(index=1, weight=1)
        self.panel_settings.columnconfigure(index=2, weight=1)
        self.panel_settings.columnconfigure(index=3, weight=1)
        self.panel_settings.columnconfigure(index=4, weight=1)

        self.panel_settings.rowconfigure(index=0, weight=1)
        self.panel_settings.rowconfigure(index=1, weight=1)
        self.panel_settings.rowconfigure(index=2, weight=1)
        self.panel_settings.rowconfigure(index=3, weight=1)
        self.panel_settings.rowconfigure(index=4, weight=1)
        self.panel_settings.rowconfigure(index=5, weight=1)

        # Создание и конфигурация таблицы
        tree_scroll = ttk.Scrollbar(self.child_root)
        tree_scroll.grid(row=0, column=2, padx=0, pady=0,
                         sticky="nsew")
        self.material_table = ttk.Treeview(
            self.child_root,
            selectmode="extended",
            yscrollcommand=tree_scroll.set,
            height=8,
            columns=('#0', '#1', '#2', '#3'),
            show="headings"
        )
        self.material_table.column(0, width=195, anchor="w")
        self.material_table.column(1, width=100, anchor="center")
        self.material_table.column(2, width=100, anchor="center")
        self.material_table.column(3, width=100, anchor="center")

        self.material_table.heading(0, text="Материал", anchor="center")
        self.material_table.heading(1, text="Ширина, мм", anchor="center")
        self.material_table.heading(2, text="Высота, мм", anchor="center")
        self.material_table.heading(3, text="Стоимость, руб.",
                                    anchor="center")
        self.material_table.selection()
        self.material_table.configure(yscrollcommand=tree_scroll.set)

        # Упаковка таблицы
        self.material_table.grid(
            row=0, column=1, padx=0, pady=0, sticky="nsew"
        )

        # Добавление данных в таблицу
        self.get_data_child()

        # Создание окон ввода новой данных в таблицу
        # Окно ввода -Названия материала-
        self.ent_name_mat = ttk.Entry(
            self.panel_settings,
            width=18
        )
        self.ent_name_mat.grid(row=0, column=0, padx=10, pady=15,
                               sticky='nsew', rowspan=2)

        # Окно ввода -Ширина листа-
        self.ent_width_mat = ttk.Entry(
            self.panel_settings,
            width=18
        )
        self.ent_width_mat.grid(row=0, column=1, padx=10, pady=15,
                                sticky='nsew', rowspan=2)

        # Окно ввода -Высота листа-
        self.ent_height_mat = ttk.Entry(
            self.panel_settings,
            width=18
        )
        self.ent_height_mat.grid(row=0, column=2, padx=10, pady=15,
                                 sticky='nsew', rowspan=2)

        # Окно ввода -Стоимость материала-
        self.ent_price_mat = ttk.Entry(
            self.panel_settings,
            width=18
        )
        self.ent_price_mat.grid(row=0, column=3, padx=10, pady=15,
                                sticky='nsew', rowspan=2)

        # Кнопка добавления материала в таблицу
        self.btn_add = ttk.Button(
            self.panel_settings,
            width=4,
            text="Добавить/редактировать материал",
            command=self.click_add_data
        )
        self.btn_add.grid(row=2, column=0, padx=10, pady=15, sticky='nsew',
                          columnspan=4)

        # Форма с переключателем типа лазера и ее конфигурация
        self.panel_laser_type = ttk.Frame(self.panel_settings, padding=0)
        self.panel_laser_type.grid(row=0, column=4, padx=0, pady=(0, 0),
                                   sticky="nsew", rowspan=2)
        self.panel_laser_type.rowconfigure(index=0, weight=1)
        self.panel_laser_type.rowconfigure(index=1, weight=1)

        # Переключатели
        self.rb_laser_type = tk.IntVar(value=1)

        self.rbt_solid = ttk.Radiobutton(
            self.panel_laser_type,
            text="Диодный лазер",
            variable=self.rb_laser_type,
            value=1
        )
        self.rbt_solid.grid(row=0, column=0, padx=15, pady=(5, 0),
                            sticky="nsew")
        self.rbt_co2 = ttk.Radiobutton(
            self.panel_laser_type,
            text="Газовый лазер",
            variable=self.rb_laser_type,
            value=2
        )
        self.rbt_co2.grid(row=1, column=0, padx=15, pady=(5, 0),
                          sticky="nsew")

        # Разделительная черта
        ttk.Separator(self.panel_settings).grid(
            row=3, column=0, columnspan=5, pady=(5, 0), sticky='ew'
        )

        # Кнопка удаления выбранного материала из таблицы
        self.btn_del = ttk.Button(
            self.panel_settings,
            width=3,
            text="Удалить выбранный материал",
            command=self.click_del_data
        )
        self.btn_del.grid(
            row=5, column=0, padx=10, pady=15, sticky='nsew',
            columnspan=2)

        # Кнопка сброса таблицы "по умолчанию"
        self.btn_get_default = ttk.Button(
            self.panel_settings,
            text="Сброс",
            command=self.get_default_materials
        )
        self.btn_get_default.grid(
            row=2, column=4, padx=(0, 10), pady=15, sticky='nsew')

        # Кнопка открытия дочернего окна с матрицей стоимостей
        self.btn_matrix_run = ttk.Button(
            self.panel_settings,
            text="Редактировать таблицу стоимостей",
            command=self.run_matrix_window
        )
        self.btn_matrix_run.grid(
            row=5, column=2, padx=(10, 10), pady=15, sticky='nsew',
            columnspan=2)

        # Кнопка закрытия окна
        self.btn_destroy = ttk.Button(
            self.panel_settings,
            text="Выход",
            command=self.destroy_child
        )
        self.btn_destroy.grid(
            row=5, column=4, padx=(0, 10), pady=15, sticky='nsew')

    def add_bind_child(self):

        # Установка фонового текста в полях ввода
        BindEntry(self.ent_name_mat, text='Материал')
        BindEntry(self.ent_width_mat, text='Ширина, мм')
        BindEntry(self.ent_height_mat, text='Высота, мм')
        BindEntry(self.ent_price_mat, text='Цена, руб')

        # Установка подсказок
        BalloonTips(self.btn_del,
                    text=f'Выделите строку в таблице.')
        BalloonTips(self.btn_matrix_run,
                    text=f'Выделите строку в таблице.')

    def get_data_child(self):  # Обновление списка материалов для таблицы
        self.data = list()
        temp_data = self.config_material_data.material_config['MAIN']
        for k, v in temp_data.items():
            temp = [k]
            temp.extend([x for x in v.split(',')])
            self.data.append(temp)
        for data in self.data:
            self.material_table.insert('', index='end', values=data)

        del temp_data, temp

    def click_add_data(self):  # Метод добавления элемента в таблицу
        temp_new = self.config_material_data.material_config
        # Считывание данных с полей ввода
        new_name = self.ent_name_mat.get()
        new_width = self.ent_width_mat.get()
        new_height = self.ent_height_mat.get()
        new_price = self.ent_price_mat.get()
        type_of_laser = 'solid' if self.rb_laser_type.get() == 1 else 'gas'

        # Если поля не заполнены - вызов сообщения об ошибке
        if (new_name == '' or new_width == '' or new_height == '' or
                new_price == ''):
            tk.messagebox.showerror('Ошибка записи', 'Данные пусты')

        # Если введенные данные не подходят под формат
        elif (new_width.isdigit() is False) or (
                new_height.isdigit() is False) or (
                new_price.isdigit() is False) or (
                new_name == 'Материал'
        ):
            tk.messagebox.showerror(
                'Ошибка записи',
                'Введите данные'
            )

        # Иначе запись в файл
        else:
            temp_new['MAIN'][new_name] = (f'{new_width}, {new_height},'
                                          f' {new_price}, {type_of_laser}')
            self.config_material_data.update_materials(some_new=temp_new)

            # Обновление данных в таблице
            # Очистка таблицы
            for item in self.material_table.get_children():
                self.material_table.delete(item)

            # Запись новых данных в таблицу
            self.get_data_child()

            # Очистка и установка фонового текста в полях ввода
            self.ent_name_mat.delete(0, tk.END)
            self.ent_width_mat.delete(0, tk.END)
            self.ent_height_mat.delete(0, tk.END)
            self.ent_price_mat.delete(0, tk.END)

            BindEntry(
                self.ent_name_mat, text='Материал').to_add_entry_child()
            BindEntry(
                self.ent_width_mat, text='Ширина, мм').to_add_entry_child()
            BindEntry(
                self.ent_height_mat, text='Высота, мм').to_add_entry_child()
            BindEntry(
                self.ent_price_mat, text='Цена, руб').to_add_entry_child()

            self.child_root.update()

    def click_del_data(self):  # Удаление выбранной строки из таблицы
        deleted_data_config = self.config_material_data.material_config

        # Удаление выбранной строки
        try:  # Проверка на то, что пользователь выбрал материал
            deleted_data = self.material_table.item(
                self.material_table.focus())

            # Удаление выбранного элемента
            deleted_data_config.remove_option('MAIN',
                                              str(deleted_data['values'][0]))
            # Обновление данных в файле конфигурации
            self.config_material_data.update_materials(
                some_new=deleted_data_config)

            # Обновление данных в таблице
            # Очистка таблицы
            for item in self.material_table.get_children():
                self.material_table.delete(item)

            # Запись новых данных в таблицу
            self.get_data_child()

        except (ValueError, KeyboardInterrupt, IndexError):
            tk.messagebox.showerror(
                'Ошибка удаления!',
                'Выберите в таблице удаляемую строку.'
            )

        del deleted_data_config

    def get_default_materials(self):
        if askokcancel('Сброс настроек', 'Вы действительно хотите сбросить '
                                         'настройки по умолчанию?'):
            self.config_material_data.get_default()

        # Переопределение переменной конфигурации
        del self.config_material_data
        self.config_material_data = Materials()
        # Обновление данных в таблице
        # Очистка таблицы
        for item in self.material_table.get_children():
            self.material_table.delete(item)

        # Запись новых данных в таблицу
        self.get_data_child()

    def grab_focus(self):  # Метод сохранения фокуса на дочернем окне
        self.child_root.grab_set()
        self.child_root.focus_set()
        self.child_root.wait_window()

    def destroy_child(self):  # Метод закрытия дочернего окна
        self.child_root.destroy()

    def run_matrix_window(self):  # Метод открытия дочернего окна матрицы
        # Считывание название материала
        try:
            matrix_material_name = self.material_table.item(
                    self.material_table.focus())['values'][0]
            self.child_root.CHILD = ChildMatrixMaterial(
                self.child_root,
                700,
                450,
                laser_type='Твердотельный лазер',
                theme='forest-light',
                icon="resources/Company_logo.ico",
                material_name=matrix_material_name
            )
            self.child_root.CHILD.grab_focus()

        except (ValueError, KeyboardInterrupt, IndexError):
            tk.messagebox.showerror(
                'Ошибка конфигурирования!',
                'Выберите в таблице строку.'
            )


class ChildMatrixMaterial:
    def __init__(self, parent, width: int, height: int, theme: str,
                 laser_type: str,
                 material_name: str = None,
                 title=f'Матрица стоимостей материала',
                 resizable=(False, False), icon=None):
        """
        Дочернее окно с таблицей стоимостей изделий из выбранного материала.
        :param parent: Родительское окно (Листовой материал);
        :param width: Ширина окна;
        :param height: Высота окна;
        :param theme: Тема окна;
        :param material_name: Наименование материала для которого
        заполняется матрица;
        :param title: Название окна;
        :param resizable: Возможность растягивания окна;
        :param icon: Иконка окна;
        :laser_type: Тип оборудования для работы с данным материалом.
        """
        # Создание дочернего окна поверх основного
        self.matrix_root = tk.Toplevel(parent)
        if material_name:
            title = f'Матрица стоимостей материала "{material_name}"'
            self.matrix_root.title(title)
        else:
            self.matrix_root.title(title)
        self.matrix_root.geometry(f"{width}x{height}+20+20")
        self.matrix_root.resizable(resizable[0], resizable[1])
        if icon:
            self.matrix_root.iconbitmap(icon)

        # Установка стиля окна
        self.style_child = ttk.Style(self.matrix_root)
        self.style_child.theme_use(theme)

        # Основные виджеты окна

        # Прорисовка окна в зависимости от типа оборудования
        if laser_type == 'Твердотельный лазер':
            self.draw_solid_widget()
        else:
            self.draw_gas_widget()

    def draw_solid_widget(self):  # Метод прорисовки виджетов
        pass

    def draw_gas_widget(self):  # Метод прорисовки виджетов
        pass

    def grab_focus(self):  # Метод сохранения фокуса на дочернем окне
        self.matrix_root.grab_set()
        self.matrix_root.focus_set()
        self.matrix_root.wait_window()

    def destroy_child(self):  # Метод закрытия дочернего окна
        self.matrix_root.destroy()
