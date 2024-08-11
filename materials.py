import configparser
import os
import shutil


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
            temp = [x for x in v.split(',')]
            my_price[k] = [float(x) for x in temp[0:3:1]][-1]
        return my_price

    def get_gab_width(self):  # Метод, возвращающий словарь Название-ширина
        mat_gab_width = dict()
        for k, v in self.material_config['MAIN'].items():
            temp = [x for x in v.split(',')]
            mat_gab_width[k] = [float(x) for x in temp[0:3:1]][0]
        return mat_gab_width

    def get_gab_height(self):  # Метод, возвращающий словарь Название-высота
        mat_gab_height = dict()
        for k, v in self.material_config['MAIN'].items():
            temp = [x for x in v.split(',')]
            mat_gab_height[k] = [float(x) for x in temp[0:3:1]][1]
        return mat_gab_height

    def get_type_of_laser(self):  # Метод, возвращающий словарь Название-лазер
        mat_type_of_laser = dict()
        for k, v in self.material_config['MAIN'].items():
            mat_type_of_laser[k] = [x for x in v.split(',')][-1]
        return mat_type_of_laser

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
        destination_path = 'settings/material_data.ini'
        source_path = 'settings/default/material_data.ini'
        if os.path.exists(destination_path):
            os.remove(destination_path)
        shutil.copy2(source_path, destination_path)


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


class Interpolation:
    def __init__(self, file_name: str):
        """
        Класс реализующий интерполяционный расчет стоимости изделия из
        выбранного материала.
        :param file_name: Название материала (файла стоимостей)
        """
        self.matrix_config = configparser.ConfigParser()
        self.matrix_config.read(f'settings/materials/{file_name}.ini',
                                encoding='utf-8')
        self.name = file_name

    def get_laser_type(self):
        """
        Метод возвращает строковое значение типа лазера.
        :return: Тип лазера.
        """
        name = self.name
        laser_type_config = configparser.ConfigParser()
        laser_type_config.read('settings/material_data.ini',
                               encoding='utf-8')
        laser_type = laser_type_config['MAIN'][name].split(', ')[-1]
        del laser_type_config
        return laser_type

    def get_cost(self, height: int, width: int, num: int):
        """
        Метод получения стоимости изделия.
        :param height: Высота изделия
        :param width: Ширина изделия
        :param num: Количество изделий
        :return: Стоимость одного изделия
        """
        temp_config = self.matrix_config['MAIN']
        pass

    def get_lower_and_bigger_key(self, width: int, height: int):
        """
        Метод получения строк (ключей) для ближайшего большего и меньшего
        габаритов.
        :param width: Ширина изделия
        :param height: Высота изделия
        :return: Список строк (ключей) для ближайшего большего и меньшего
        габаритов.
        """

        temp_matrix = self.matrix_config['COSTS']

        # Начальные значения верхней и нижней границ
        lower_key = ['маленькие (50х30мм)', '50', '30']
        if self.get_laser_type() == 'gas':
            bigger_key = ['Огромные (600х400мм)', '600', '400']
        else:
            bigger_key = ['негабаритные (300х200мм)', '300', '200']
        area = width * height
        # Считаем площадь
        key_get_point = False

        # Получаем для наших габаритов нижнюю и верхнюю границу:
        for k, v in temp_matrix.items():
            temp = k.split(', ')

            # Если попали в точку
            if int(temp[1]) * int(temp[2]) == area:
                key_get_point = True
                lower_key = k.split(', ')
                break

            # Нижняя точка
            if int(temp[1]) * int(temp[2]) < area and (
                    (int(temp[1]) * int(temp[2])) >= (int(lower_key[1]) * int(
                    lower_key[2]))):
                lower_key = k.split(', ')
            # Верхняя точка
            if int(temp[1]) * int(temp[2]) >= area and (
                    (int(temp[1]) * int(temp[2])) <= (int(bigger_key[1]) * int(
                    bigger_key[2]))):
                bigger_key = k.split(', ')

        # Если попали в точку
        if key_get_point:
            return ', '.join(lower_key)

        # Если за границами точек
        elif lower_key == bigger_key:
            return ', '.join(lower_key)

        # Если в границах точек
        else:
            return [', '.join(lower_key), ', '.join(bigger_key)]

    @staticmethod
    def get_interpolation(point: int, lower_point: list, bigger_point: list):
        """
        Метод интерполяции значений между двумя точками.
        Формула интерполяции имеет вид:
            result = (|p-x_2|/|x_2-x_1|)*y_1 + (|p-x_1|/|x_2-x_1|)*y_2,

            где (x_1, y_1) - нижняя точка и ее значение;
                (x_2, y_2) - верхняя точка и ее значение;
                p - искомая точка.
        :param point: Передаваемая искомая точка
        :param lower_point: Ближайшая нижняя точка и ее значение;
        :param bigger_point: Ближайшая верхняя точка и ее значение;
        :return: Значение (цены, размера и др.) для искомой точки.
        """
        try:
            lower_diff = abs(
                int(point) - int(lower_point[0])
            ) / abs((int(bigger_point[0]) - int(lower_point[0])))
            bigger_diff = abs(
                int(point) - int(bigger_point[0])
            ) / abs((int(bigger_point[0]) - int(lower_point[0])))

            result = (
                lower_diff * bigger_point[1] + bigger_diff * lower_point[1]
            )
        except ValueError:
            print('Переданы неправильные значения!')
            result = 0

        return result
