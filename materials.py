import configparser


class Materials:
    def __init__(self):

        """
        Класс, реализующий получение параметров (ширина, высота,
        цена) листового материала.
        """

        # Создание файла конфигурации
        self.material_config = configparser.ConfigParser()
        self.material_config.read('settings/material_data.ini',
                                  encoding='utf-8')

    def get_mat(self):  # Метод, возвращающий словарь Название-стоимость
        my_price = dict()
        for k, v in self.material_config['MAIN'].items():
            my_price[k] = [float(x) for x in v.split(',')][-1]
        return my_price

    def get_gab_width(self):  # Метод, возвращающий словарь Название-ширина
        mat_gab_width = dict()
        for k, v in self.material_config['MAIN'].items():
            mat_gab_width[k] = [float(x) for x in v.split(',')][0]
        return mat_gab_width

    def get_gab_height(self):  # Метод, возвращающий словарь Название-высота
        mat_gab_height = dict()
        for k, v in self.material_config['MAIN'].items():
            mat_gab_height[k] = [float(x) for x in v.split(',')][1]
        return mat_gab_height

    def update_materials(self, some_new=None):  # Обновление файла конфигурации
        if some_new:
            with (open('settings/material_data.ini', 'w', encoding='utf-8') as
                  configfile):
                some_new.write(configfile)
        else:
            with (open('settings/material_data.ini', 'w', encoding='utf-8') as
                  configfile):
                self.material_config.write(configfile)

    @staticmethod
    def get_default():
        string_materials = """
        [INFO]
        info = # Файл содержит список параметров основного листового материала
        
        [MAIN]
        Анодированный алюминий 0.5 мм = 400, 200, 1000
        Двухслойный пластик 1.5 мм = 1200, 600, 5000
        Двухслойный пластик 1.5 мм (Китай) = 1200, 600, 1850
        Двухслойный пластик 0.6 мм = 1200, 600, 2500
        Самоклеящийся пластик 0.1 мм = 600, 300, 1420
        ПЭТ 0.5 мм = 2000, 1250, 1000
        ПЭТ 1 мм = 2000, 1250, 1500
        ПЭТ 1.5 мм = 2000, 1250, 2000
        Фанера 4 мм = 1525, 1525, 650
        Оргстекло 4 мм = 2050, 1500, 6000
        Оргстекло 3 мм = 2050, 1500, 4510
        """
        default_materials = configparser.ConfigParser()
        default_materials.read_string(string_materials)
        with (open('settings/material_data.ini', encoding='utf-8') as
              configfile):
            default_materials.write(configfile)


class Calculation:
    def __init__(self, w, h, mat_name):

        """
        Класс, реализующий расчет себестоимости изделия по выбранному
        материалу.
        """

        # Создание переменных
        self.figure_per_rows = 0
        self.figure_per_columns = 0
        self.total_1 = 0
        self.total_2 = 0

        # Получение габаритов листа с учетом коэффициента обрезков
        self.w_big = Materials().get_gab_width()[mat_name] * 0.9
        self.h_big = Materials().get_gab_height()[mat_name]
        self.width = w
        self.height = h

        # Получение стоимости выбранного материала (самого листа)
        self.price = Materials().get_mat()[mat_name]

    def figure_1(self):  # Первый метод упаковки
        try:
            # Проверка максимальной вместимости контейнера в строках и столбцах
            self.figure_per_rows = self.w_big // self.width
            self.figure_per_columns = self.h_big // self.height
            self.total_1 += int(self.figure_per_rows * self.figure_per_columns)

            # После заполнения строк проверяем вместимость оставшейся части
            # листа, при этом переворачиваем изделие и проверяем на вместимость
            if (self.w_big - (
                    self.figure_per_rows * self.width)) >= self.height:
                x_2 = (self.w_big
                       - (self.figure_per_rows * self.width)) // self.height
                y_2 = self.h_big // self.width
                self.total_1 += int(x_2 * y_2)
        except ZeroDivisionError:
            self.total_1 = 0
        # Возвращаем количество изделий с листа первым методом
        return self.total_1

    def figure_2(self):  # Второй метод упаковки (изделие повернуто на 90 гр.)
        try:
            # Проверка максимальной вместимости контейнера в строках и столбцах
            self.figure_per_rows = self.w_big // self.height
            self.figure_per_columns = self.h_big // self.width
            self.total_2 += int(self.figure_per_rows * self.figure_per_columns)

            # После заполнения строк проверяем вместимость оставшейся части
            # листа, при этом переворачиваем изделие и проверяем на вместимость
            if (self.w_big - (
                    self.figure_per_rows * self.height)) >= self.width:
                x_2 = (self.h_big
                       - (self.figure_per_rows * self.height)) // self.width
                y_2 = self.h_big // self.height
                self.total_2 += int(x_2 * y_2)

        except ZeroDivisionError:
            self.total_2 = 0
        # Возвращаем количество изделий с листа вторым методом
        return self.total_2

    def get_price(self):  # Метод, возвращающий себестоимость материала
        return self.price
