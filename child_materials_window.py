import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import askokcancel
from materials import Materials
from binds import BindEntry


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
            columns=('#0', '#1', '#2', '#3', '#4'),
            show="headings"
        )
        self.material_table.column(0, width=0, anchor="w")
        self.material_table.column(1, width=195, anchor="w")
        self.material_table.column(2, width=100, anchor="center")
        self.material_table.column(3, width=100, anchor="center")
        self.material_table.column(4, width=100, anchor="center")

        self.material_table.heading(0, text="", anchor="center")
        self.material_table.heading(1, text="Материал", anchor="center")
        self.material_table.heading(2, text="Ширина, мм", anchor="center")
        self.material_table.heading(3, text="Высота, мм", anchor="center")
        self.material_table.heading(4, text="Стоимость, руб.",
                                    anchor="center")
        self.material_table.selection()
        self.material_table.configure(yscrollcommand=tree_scroll.set)

        # Упаковка таблицы
        self.material_table.grid(
            row=0, column=1, padx=0, pady=0, sticky="nsew"
        )

        # Добавление данных в таблицу
        self.get_data_child()
        self.i_data = -1
        for data in self.data:
            self.i_data += 1
            temp_list = list()
            temp_list.append(f'{self.i_data}:')
            temp_list.extend(data)
            self.material_table.insert('', index='end', values=temp_list)

        # Создание окон ввода новой данных в таблицу
        # Окно ввода -Названия материала-
        ttk.Label(self.panel_settings, text='Название материала').grid(
            row=0, column=0, padx=0, pady=5, sticky='ns'
        )
        self.ent_name_mat = ttk.Entry(
            self.panel_settings,
            width=18
        )
        self.ent_name_mat.grid(row=1, column=0, padx=10, pady=5, sticky='nsew')

        # Окно ввода -Ширина листа-
        ttk.Label(self.panel_settings, text='Ширина листа, мм').grid(
            row=0, column=1, padx=0, pady=5, sticky='ns'
        )
        self.ent_width_mat = ttk.Entry(
            self.panel_settings,
            width=18
        )
        self.ent_width_mat.grid(row=1, column=1, padx=10, pady=5,
                                sticky='nsew')

        # Окно ввода -Высота листа-
        ttk.Label(self.panel_settings, text='Высота листа, мм').grid(
            row=0, column=2, padx=0, pady=5, sticky='ns'
        )
        self.ent_height_mat = ttk.Entry(
            self.panel_settings,
            width=18
        )
        self.ent_height_mat.grid(row=1, column=2, padx=10, pady=5,
                                 sticky='nsew')

        # Окно ввода -Стоимость материала-
        ttk.Label(self.panel_settings, text='Стоимость, руб').grid(
            row=0, column=3, padx=0, pady=5, sticky='ns'
        )
        self.ent_price_mat = ttk.Entry(
            self.panel_settings,
            width=18
        )
        self.ent_price_mat.grid(row=1, column=3, padx=10, pady=5,
                                sticky='nsew')

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
        ttk.Label(self.panel_settings, text='Тип лазера').grid(
            row=0, column=4, padx=0, pady=5, sticky='ns'
        )
        self.panel_laser_type = ttk.Frame(self.panel_settings, padding=0)
        self.panel_laser_type.grid(row=1, column=4, padx=0, pady=(0, 0),
                                   sticky="nsew")
        self.panel_laser_type.columnconfigure(index=0, weight=1)
        self.panel_laser_type.columnconfigure(index=1, weight=1)

        # Переключатели
        self.rb_laser_type = tk.IntVar(value=1)

        self.rbt_solid = ttk.Radiobutton(
            self.panel_laser_type,
            text="ТД",
            variable=self.rb_laser_type,
            value=1
        )
        self.rbt_solid.grid(row=0, column=0, padx=(35, 0), pady=(5, 0),
                            sticky="w")
        self.rbt_co2 = ttk.Radiobutton(
            self.panel_laser_type,
            text="СО2",
            variable=self.rb_laser_type,
            value=2
        )
        self.rbt_co2.grid(row=0, column=1, padx=(0, 40), pady=(5, 0),
                          sticky="e")

        # Разделительная черта
        ttk.Separator(self.panel_settings).grid(
            row=3, column=0, columnspan=5, pady=(5, 0), sticky='ew'
        )

        # Поле ввода для удаления из таблицы
        ttk.Label(self.panel_settings, text='Введите номер строки').grid(
            row=4, column=0, padx=0, pady=(5, 0), sticky='ns'
        )
        self.ent_delete_data = ttk.Entry(
            self.panel_settings,
            width=18
        )
        self.ent_delete_data.grid(
            row=5,
            column=0,
            padx=10,
            pady=0,
            sticky='ew'
        )

        # Кнопка удаления материала из таблицы
        self.btn_del = ttk.Button(
            self.panel_settings,
            width=3,
            text="Удалить материал",
            command=self.click_del_data
        )
        self.btn_del.grid(
            row=5, column=1, padx=10, pady=15, sticky='nsew',
            columnspan=1)

        # Кнопка сброса таблицы "по умолчанию"
        self.btn_get_default = ttk.Button(
            self.panel_settings,
            text="Сброс",
            command=self.get_default_materials
        )
        self.btn_get_default.grid(
            row=2, column=4, padx=(0, 10), pady=15, sticky='nsew')

        # Поле ввода номера строки для конфигурации матрицы стоимостей
        ttk.Label(self.panel_settings, text='Введите номер строки').grid(
            row=4, column=2, padx=0, pady=(5, 0), sticky='ns'
        )

        self.ent_configure_costs = ttk.Entry(
            self.panel_settings,
            width=18
        )
        self.ent_configure_costs.grid(
            row=5,
            column=2,
            padx=10,
            pady=0,
            sticky='ew'
        )

        # Кнопка открытия дочернего окна с матрицей стоимостей
        self.btn_matrix_run = ttk.Button(
            self.panel_settings,
            text="Таблица стоимостей",
            command=self.run_matrix_window
        )
        self.btn_matrix_run.grid(
            row=5, column=3, padx=(10, 10), pady=15, sticky='nsew',
            columnspan=1)

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
        BindEntry(self.ent_name_mat)
        BindEntry(self.ent_width_mat)
        BindEntry(self.ent_height_mat)
        BindEntry(self.ent_price_mat)
        BindEntry(self.ent_delete_data)
        BindEntry(self.ent_configure_costs)

    def get_data_child(self):  # Обновление списка материалов для таблицы
        self.data = list()
        temp_data = self.config_material_data.material_config['MAIN']
        for k, v in temp_data.items():
            temp = [k]
            temp.extend([x for x in v.split(',')])
            self.data.append(temp)

        del temp_data, temp

    def click_add_data(self):  # Метод добавления элемента в таблицу
        temp_new = self.config_material_data.material_config
        # Считывание данных с полей ввода
        new_name = self.ent_name_mat.get()
        new_width = self.ent_width_mat.get()
        new_height = self.ent_height_mat.get()
        new_price = self.ent_price_mat.get()

        # Если поля не заполнены - вызов сообщения об ошибке
        if (new_name == '' or new_width == '' or new_height == '' or
                new_price == ''):
            tk.messagebox.showerror('Ошибка записи', 'Данные пусты')

        # Если введенные данные не подходят под формат
        elif (new_width.isdigit() is False) or (
                new_height.isdigit() is False) or (
                new_price.isdigit() is False) or (
                new_name == '-'
        ):
            tk.messagebox.showerror(
                'Ошибка записи',
                'Введите данные'
            )

        # Иначе запись в файл
        else:
            temp_new['MAIN'][new_name] = (f'{new_width}, {new_height},'
                                          f' {new_price}')
            self.config_material_data.update_materials(some_new=temp_new)

            # Обновление данных в таблице
            # Очистка таблицы
            for item in self.material_table.get_children():
                self.material_table.delete(item)
            self.get_data_child()

            # Запись новых данных в таблицу
            self.i_data = -1
            for data in self.data:
                self.i_data += 1
                temp_list = list()
                temp_list.append(f'{self.i_data}:')
                temp_list.extend(data)
                self.material_table.insert('', index='end',
                                           values=temp_list)
            self.child_root.update()

            # Очистка и установка фонового текста в полях ввода
            self.ent_name_mat.delete(0, tk.END)
            self.ent_width_mat.delete(0, tk.END)
            self.ent_height_mat.delete(0, tk.END)
            self.ent_price_mat.delete(0, tk.END)

            BindEntry(self.ent_name_mat).to_add_entry_child()
            BindEntry(self.ent_width_mat).to_add_entry_child()
            BindEntry(self.ent_height_mat).to_add_entry_child()
            BindEntry(self.ent_price_mat).to_add_entry_child()

            self.child_root.update()

    def click_del_data(self):  # Удаление выбранной строки из таблицы
        deleted_data_config = self.config_material_data.material_config
        # Получение строки для удаления
        deleted_data = self.ent_delete_data.get()

        # Проверка на пустое текстовое поле
        if deleted_data == '':
            tk.messagebox.showerror(
                'Ошибка удаления',
                'Введите номер строки'
            )

        # Если ввели не число
        elif deleted_data.isdigit() is False:
            tk.messagebox.showerror(
                'Ошибка удаления',
                'Введенная вами строка не является числом'
            )

        # Если такой строки нет
        elif len(self.material_table.get_children()) < int(deleted_data) + 1:
            tk.messagebox.showerror(
                'Ошибка удаления',
                'Введен отсутствующий номер строки'
            )

        # Удаление выбранной строки
        else:
            # Считывание удаляемого элемента
            deleted_item = None
            for item in self.material_table.get_children():
                if deleted_data+':' == self.material_table.set(item, 0):
                    deleted_item = self.material_table.set(item, 1)
            # Удаление выбранного элемента
            deleted_data_config.remove_option('MAIN', deleted_item)
            # Обновление данных в файле конфигурации
            self.config_material_data.update_materials(
                some_new=deleted_data_config)

            # Обновление данных в таблице
            # Очистка таблицы
            for item in self.material_table.get_children():
                self.material_table.delete(item)
            self.get_data_child()

            # Запись новых данных в таблицу
            self.i_data = -1
            for data in self.data:
                self.i_data += 1
                temp_list = list()
                temp_list.append(f'{self.i_data}:')
                temp_list.extend(data)
                self.material_table.insert('', index='end',
                                           values=temp_list)
            self.child_root.update()
            #  Очистка и установка фонового текста в поле ввода
            self.ent_delete_data.delete(0, tk.END)
            BindEntry(self.ent_delete_data).to_add_entry_child()

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
        self.get_data_child()
        # Запись новых данных в таблицу
        self.i_data = -1
        for data in self.data:
            self.i_data += 1
            temp_list = list()
            temp_list.append(f'{self.i_data}:')
            temp_list.extend(data)
            self.material_table.insert('', index='end',
                                       values=temp_list)
            self.child_root.update()
        self.child_root.update()

    def grab_focus(self):  # Метод сохранения фокуса на дочернем окне
        self.child_root.grab_set()
        self.child_root.focus_set()
        self.child_root.wait_window()

    def destroy_child(self):  # Метод закрытия дочернего окна
        self.child_root.destroy()

    def run_matrix_window(self):  # Метод открытия дочернего окна матрицы
        print(self.material_table.item(self.material_table.focus()))
        self.child_root.CHILD = ChildMatrixMaterial(
            self.child_root,
            700,
            450,
            laser_type='Твердотельный лазер',
            theme='forest-light',
            icon="resources/Company_logo.ico"
        )
        self.child_root.CHILD.grab_focus()


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
