import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import configparser


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
        self.child_root.geometry(f"{width}x{height}+200+100")
        self.child_root.resizable(resizable[0], resizable[1])
        if icon:
            self.child_root.iconbitmap(icon)

        # Установка стиля окна
        self.style_child = ttk.Style(self.child_root)
        self.style_child.theme_use(theme)

        # Создание переменной, хранящей массив данных для таблицы
        self.dannye = []

        # Создание переменной для исключения ошибок 'event' value is not use
        self.not_use_child = None

        # Конфигурация отзывчивости окна
        self.child_root.columnconfigure(index=0, weight=1)
        self.child_root.columnconfigure(index=1, weight=50)
        self.child_root.columnconfigure(index=2, weight=1)
        self.child_root.rowconfigure(index=0, weight=1)
        self.child_root.rowconfigure(index=1, weight=2)

        # Создание форм окна
        self.panel_1 = ttk.Frame(self.child_root, padding=(0, 0, 0, 0))
        self.panel_1.grid(row=0, column=0, padx=0, pady=(0, 0),
                          sticky="nsew")
        self.panel_2 = ttk.Frame(self.child_root, padding=(0, 0, 0, 0))
        self.panel_2.grid(row=1, column=0, padx=0, pady=(0, 0),
                          sticky="nsew", columnspan=3)

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
        for data in self.dannye:
            self.i_data += 1
            temp_list = list()
            temp_list.append(f'{self.i_data}:')
            temp_list.extend(data)
            self.material_table.insert('', index='end', values=temp_list)

        # Создание окон ввода новой данных в таблицу
        # Окно ввода -Названия материала-
        ttk.Label(self.panel_2, text='Название материала').grid(
            row=0, column=0, padx=0, pady=5, sticky='ns'
        )
        self.name_mat = ttk.Entry(
            self.panel_2,
            width=24
        )
        # self.name_mat.insert(0, 'Введите название материала')
        self.name_mat.grid(row=1, column=0, padx=10, pady=5, sticky='nsew')

        # Окно ввода -Ширина листа-
        ttk.Label(self.panel_2, text='Ширина листа, мм').grid(
            row=0, column=1, padx=0, pady=5, sticky='ns'
        )
        self.width_mat = ttk.Entry(
            self.panel_2,
            width=24
        )
        # self.width_mat.insert(0, '0 мм.')
        self.width_mat.grid(row=1, column=1, padx=10, pady=5, sticky='nsew')

        # Окно ввода -Высота листа-
        ttk.Label(self.panel_2, text='Высота листа, мм').grid(
            row=0, column=2, padx=0, pady=5, sticky='ns'
        )
        self.height_mat = ttk.Entry(
            self.panel_2,
            width=24
        )
        # self.height_mat.insert(0, '0 мм.')
        self.height_mat.grid(row=1, column=2, padx=10, pady=5, sticky='nsew')

        # Окно ввода -Стоимость материала-
        ttk.Label(self.panel_2, text='Стоимость, руб').grid(
            row=0, column=3, padx=0, pady=5, sticky='ns'
        )
        self.price_mat = ttk.Entry(
            self.panel_2,
            width=24
        )
        # self.price_mat.insert(0, '0 руб.')
        self.price_mat.grid(row=1, column=3, padx=10, pady=5, sticky='nsew')

        # Кнопка добавления материала в таблицу
        self.btn_add = ttk.Button(
            self.panel_2,
            width=4,
            text="Добавить материал",
            command=self.click_add_data
        )
        self.btn_add.grid(row=2, column=1, padx=10, pady=15, sticky='nsew',
                          columnspan=2)

        # Разделительная черта
        ttk.Separator(self.panel_2).grid(
            row=3, column=0, columnspan=4, pady=10, sticky='ew'
        )

        # Поле ввода для удаления из таблицы
        ttk.Label(self.panel_2, text='Введите номер строки').grid(
            row=4, column=0, padx=0, pady=15, sticky='ns'
        )
        self.delete_data = ttk.Entry(
            self.panel_2,
            width=24
        )
        self.delete_data.grid(
            row=5,
            column=0,
            padx=10,
            pady=(5, 25),
            sticky='ew'
        )

        # Кнопка удаления материала из таблицы
        self.btn_del = ttk.Button(
            self.panel_2,
            width=3,
            text="Удалить материал",
            command=self.click_del_data
        )
        self.btn_del.grid(
            row=5, column=1, padx=15, pady=(5, 25), sticky='nsew')

        # Кнопка закрытия окна
        self.btn_destroy = ttk.Button(
            self.panel_2,
            text="Выход",
            command=self.destroy_child
        )
        self.btn_destroy.grid(
            row=5, column=3, padx=(5, 10), pady=(5, 25), sticky='nsew')

    def add_bind_child(self):

        # Установка фонового текста в полях ввода
        self.to_add_entry_child()
        self.to_add_entry_child1()
        self.to_add_entry_child2()
        self.to_add_entry_child3()
        self.to_add_entry_child4()

        self.name_mat.bind('<FocusIn>', self.erase_entry_child)
        self.name_mat.bind('<FocusOut>', self.to_add_entry_child)

        self.width_mat.bind('<FocusIn>', self.erase_entry_child1)
        self.width_mat.bind('<FocusOut>', self.to_add_entry_child1)

        self.height_mat.bind('<FocusIn>', self.erase_entry_child2)
        self.height_mat.bind('<FocusOut>', self.to_add_entry_child2)

        self.price_mat.bind('<FocusIn>', self.erase_entry_child3)
        self.price_mat.bind('<FocusOut>', self.to_add_entry_child3)

        self.delete_data.bind('<FocusIn>', self.erase_entry_child4)
        self.delete_data.bind('<FocusOut>', self.to_add_entry_child4)

    def erase_entry_child(self, event=None):
        if self.name_mat.get() == '-':
            self.name_mat.delete(0, 'end')
        self.not_use_child = event

    def erase_entry_child1(self, event=None):
        if self.width_mat.get() == '-':
            self.width_mat.delete(0, 'end')
        self.not_use_child = event

    def erase_entry_child2(self, event=None):
        if self.height_mat.get() == '-':
            self.height_mat.delete(0, 'end')
        self.not_use_child = event

    def erase_entry_child3(self, event=None):
        if self.price_mat.get() == '-':
            self.price_mat.delete(0, 'end')
        self.not_use_child = event

    def erase_entry_child4(self, event=None):
        if self.delete_data.get() == '-':
            self.delete_data.delete(0, 'end')
        self.not_use_child = event

    def to_add_entry_child(self, event=None):
        if self.name_mat.get() == "":
            self.name_mat.insert(0, '-')
        self.not_use_child = event

    def to_add_entry_child1(self, event=None):
        if self.width_mat.get() == "":
            self.width_mat.insert(0, '-')
        self.not_use_child = event

    def to_add_entry_child2(self, event=None):
        if self.height_mat.get() == "":
            self.height_mat.insert(0, '-')
        self.not_use_child = event

    def to_add_entry_child3(self, event=None):
        if self.price_mat.get() == "":
            self.price_mat.insert(0, '-')
        self.not_use_child = event

    def to_add_entry_child4(self, event=None):
        if self.delete_data.get() == "":
            self.delete_data.insert(0, '-')
        self.not_use_child = event

    def get_data_child(self):  # Считывание данных из файла
        self.dannye = list()
        file_dannye = open(
            'resources/materials_data.txt',
            'r',
            encoding='utf-8'
        )
        temp_dannye = file_dannye.readlines()
        for x in temp_dannye:
            self.dannye.append(x.split(','))
        file_dannye.close()

    def click_add_data(self):  # Метод добавления элемента в таблицу

        # Считывание данных с полей ввода
        new_name = self.name_mat.get()
        new_width = self.width_mat.get()
        new_height = self.height_mat.get()
        new_price = self.price_mat.get()

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
            with open(
                    'resources/materials_data.txt',
                    'a',
                    encoding='utf-8'
            ) as file:
                file.seek(0, 2)
                file.write(
                    f'\n{new_name}, {new_width}, {new_height}, {new_price}'
                )
            file.close()

            # Обновление данных в таблице
            self.i_data += 1
            new_data = [f'{self.i_data}:', new_name, new_width, new_height,
                        new_price]
            self.material_table.insert('', index='end', values=new_data)
            self.child_root.update()

    def click_del_data(self):  # Удаление выбранной строки из таблицы
        # Получение строки для удаления
        deleted_data = self.delete_data.get()

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
            num = int(deleted_data)
            # Считывание данных
            with open(
                    'resources/materials_data.txt',
                    'r',
                    encoding='utf-8'
            ) as file:
                lines = file.readlines()
                if '' in lines:
                    lines.remove('')
                elif '\n' in lines:
                    lines.remove('\n')
                file.close()

            # Удаление выбранной строки и запись данных в файл
            with open(
                    'resources/materials_data.txt',
                    'w',
                    encoding='utf-8'
            ) as file2:
                del lines[num]
                filter(None, lines)
                file2.write(''.join(lines))
                file2.close()

            # Обновление данных в таблице
            # Очистка таблицы
            for item in self.material_table.get_children():
                self.material_table.delete(item)
            self.get_data_child()

            # Запись новых данных в таблицу
            self.i_data = -1
            for data in self.dannye:
                self.i_data += 1
                temp_list = list()
                temp_list.append(f'{self.i_data}:')
                temp_list.extend(data)
                self.material_table.insert('', index='end',
                                           values=temp_list)
                self.child_root.update()

    def grab_focus(self):  # Метод сохранения фокуса на дочернем окне
        self.child_root.grab_set()
        self.child_root.focus_set()
        self.child_root.wait_window()

    def destroy_child(self):  # Метод закрытия дочернего окна
        self.child_root.destroy()
