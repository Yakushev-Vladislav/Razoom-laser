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
        """
        Метод возвращения словаря "Название-стоимость"
        :return: Словарь "название - стоимость листа"
        """
        my_price = dict()
        for k, v in self.material_config['MAIN'].items():
            temp = [x for x in v.split(',')]
            my_price[k] = [float(x) for x in temp[0:3:1]][-1]
        return my_price

    def get_gab_width(self):  # Метод, возвращающий словарь Название-ширина
        """
        Метод возвращения словаря "название - ширина листа"
        :return: Словарь "название - ширина листа"
        """
        mat_gab_width = dict()
        for k, v in self.material_config['MAIN'].items():
            temp = [x for x in v.split(',')]
            mat_gab_width[k] = [float(x) for x in temp[0:3:1]][0]
        return mat_gab_width

    def get_gab_height(self):  # Метод, возвращающий словарь Название-высота
        """
        Метод возвращения словаря "название - высота листа"
        :return: Словарь "название - высота листа"
        """
        mat_gab_height = dict()
        for k, v in self.material_config['MAIN'].items():
            temp = [x for x in v.split(',')]
            mat_gab_height[k] = [float(x) for x in temp[0:3:1]][1]
        return mat_gab_height

    def get_type_of_laser(self):  # Метод, возвращающий словарь Название-лазер
        """
        Метод возвращения словаря "название - тип оборудования"
        :return: Словарь "название - тип оборудования"
        """
        mat_type_of_laser = dict()
        for k, v in self.material_config['MAIN'].items():
            mat_type_of_laser[k] = [x for x in v.split(',')][-1]
        return mat_type_of_laser

    def update_materials(self, some_new=None):  # Обновление файла конфигурации
        """
        Метод обновления файла конфигурации.
        :param some_new: Переменная конфигурации с новыми данными
        """
        if some_new:
            with (open('settings/material_data.ini', 'w', encoding='utf-8') as
                  configfile):
                some_new.write(configfile)
        else:
            with (open('settings/material_data.ini', 'w', encoding='utf-8') as
                  configfile):
                self.material_config.write(configfile)

    @staticmethod
    def del_matrix_file(material_name: str):
        """
        Метод удаления файла конфигурации с матрицей стоимости материала.
        :param material_name: Название материала/файла конфигурации.
        """
        file_path = f'settings/materials/{material_name}.ini'
        if os.path.isfile(file_path):
            os.remove(file_path)

    @staticmethod
    def add_matrix_file(material_name: str, laser_type: str):
        """
        Метод добавления файла конфигурации с матрицей стоимости материала.
        :param material_name: Название материала
        :param laser_type: Тип лазера
        """
        destination_path = f'settings/materials'
        file_new_name = f'settings/materials/{material_name}.ini'

        # Если редактируем имеющийся материал
        if os.path.exists(f'settings/materials/{material_name}.ini'):
            pass

        # Если создаем новый материал
        else:
            if laser_type == 'gas':
                source_path = 'settings/default/materials/default_gas.ini'
                file_old_name = 'settings/materials/default_gas.ini'
            else:
                source_path = 'settings/default/materials/default_solid.ini'
                file_old_name = 'settings/materials/default_solid.ini'

            # Копируем файл в папку назначения
            shutil.copy(
                source_path,
                os.path.join(destination_path)
            )

            # Переименовываем файл
            os.rename(file_old_name, file_new_name)

    @staticmethod
    def get_default():
        """
        Метод сброса файла конфигурации и стоимостей "по-умолчанию"
        """

        # Сброс основного файла конфигурации со списком материалов
        destination_path = 'settings/material_data.ini'
        source_path = 'settings/default/material_data.ini'
        if os.path.exists(destination_path):
            os.remove(destination_path)
        shutil.copy2(source_path, destination_path)

        # Сброс файлов с матрицами стоимостей
        destination_path = 'settings/materials/'
        source_path = 'settings/default/materials/'
        deleted_files = os.listdir(destination_path)
        new_files = os.listdir(source_path)
        for file in deleted_files:
            os.remove(f'settings/materials/{file}')
        for filename in new_files:
            shutil.copy(
                f'settings/default/materials/{filename}',
                f'settings/materials/{filename}'
            )

        # Удаление дефолтных файлов стоимостей для типов лазера
        laser_types = ['default_gas', 'default_solid']
        for item in laser_types:
            file_path = f'settings/materials/{item}.ini'
            if os.path.isfile(file_path):
                os.remove(file_path)


class Calculation:
    def __init__(self, width: int, height: int, mat_name: str):
        """
        Класс реализующий алгоритм упаковки в контейнере.
        :param width: Ширина изделия
        :param height: Высота изделия
        :param mat_name: Название материала
        """

        # Создание переменных
        self.figure_per_rows = 0
        self.figure_per_columns = 0
        self.total_1 = 0
        self.total_2 = 0

        # Получение габаритов листа с учетом коэффициента обрезков
        self.w_big = Materials().get_gab_width()[mat_name] * 0.9
        self.h_big = Materials().get_gab_height()[mat_name]
        self.width = width
        self.height = height

        # Получение стоимости выбранного материала (самого листа)
        self.price = Materials().get_mat()[mat_name]

    def figure_1(self):  # Первый метод упаковки
        """
        Первый метод упаковки.
        :return: Возможное количество размещенных изделий на листе
        """
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
        """
        Второй метод упаковки. Здесь заменены высота и ширина изделия друг
        на друга. Соответственно упаковываем повернутое на 90 градусов изделие
        :return: Возможное количество размещенных изделий на листе
        """
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
        """
        Интерфейсный метод возвращения себестоимости материала
        :return: Себестоимость материала
        """
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
        temp_cost_config = self.matrix_config['COSTS']

        # Список хранящий количество изделий в партии
        numbering_list = [1, 5, 15, 50, 150, 500, 1000]

        # Получаем граничные строки для нашего изделия
        lower_and_bigger_key = self.get_lower_and_bigger_key(height, width)

        # Границы количества изделий
        lower_index = 0
        bigger_index = -1
        for item in numbering_list:
            if numbering_list[lower_index] <= item <= num:
                lower_index = numbering_list.index(item)
            if numbering_list[bigger_index] >= item >= num:
                bigger_index = numbering_list.index(item)

        # Если попали в точку, либо вне строк (супер маленькое/большое изделие)
        if type(lower_and_bigger_key) is not list:
            # Список цен для выбранного габарита (и негабаритного изделия)
            cost_list = [int(x) for x in temp_cost_config[
                lower_and_bigger_key].split(', ')]

            return self.get_interpolation(
                num,
                [numbering_list[lower_index], cost_list[lower_index]],
                [numbering_list[bigger_index], cost_list[bigger_index]]
            )

        # Если наша точка между имеющимися габаритами
        else:
            # Создаем списки цен для большей и меньшей строк (габаритов)
            cost_lower_list = [int(x) for x in temp_cost_config[
                lower_and_bigger_key[0]].split(', ')]
            cost_bigger_list = [int(x) for x in temp_cost_config[
                lower_and_bigger_key[-1]].split(', ')]
            # Для списка получаем цену изделия с учетом нужного количества
            lower_cost = self.get_interpolation(
                num,
                [numbering_list[lower_index], cost_lower_list[lower_index]],
                [numbering_list[bigger_index], cost_lower_list[bigger_index]]
            )
            bigger_cost = self.get_interpolation(
                num,
                [numbering_list[lower_index], cost_bigger_list[lower_index]],
                [numbering_list[bigger_index], cost_bigger_list[bigger_index]]
            )
            # Интерполируем между строками (габаритами)
            lower_area = (int(lower_and_bigger_key[0].split(', ')[1]) * int(
                lower_and_bigger_key[0].split(', ')[-1]))
            bigger_area = (int(lower_and_bigger_key[1].split(', ')[1]) * int(
                lower_and_bigger_key[1].split(', ')[-1]))
            return self.get_interpolation(
                width*height,
                [lower_area, lower_cost],
                [bigger_area, bigger_cost]
            )

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
        lower_key = ['', '1_000_000', '1_000_000']
        bigger_key = ['', '0', '0']

        # Принимаем из файла значения верхней и нижней границы для материала
        for key in temp_matrix.keys():
            temp_key = key.split(', ')
            if float(temp_key[1]) * float(temp_key[2]) <= (
                    float(lower_key[1]) * float(lower_key[2])):
                lower_key = key.split(', ')
            if float(temp_key[1]) * float(temp_key[2]) >= (
                    float(bigger_key[1]) * float(bigger_key[2])):
                bigger_key = key.split(', ')

        # Считаем площадь
        area = width * height
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
            if lower_point == bigger_point:
                result = lower_point[1]
            else:
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

    def update_matrix(self, some_new=None):  # Обновление файла конфигурации
        """
        Метод обновления файла конфигурации.
        :param some_new: Переменная конфигурации с новыми данными
        """
        if some_new:
            with (open(f'settings/materials/{self.name}.ini', 'w',
                       encoding='utf-8') as configfile):
                some_new.write(configfile)
        else:
            with (open(f'settings/materials/{self.name}.ini', 'w',
                       encoding='utf-8') as configfile):
                self.matrix_config.write(configfile)

    def get_default(self):
        """
        Метод сброса матрицы стоимости до настроек "по-умолчанию".
        """
        # Сохраняем в переменные путь к файлам конфигурации
        destination_path = f'settings/materials/{self.name}.ini'
        source_path = f'settings/default/materials/{self.name}.ini'

        # Удаляем действующий файл конфигурации
        if os.path.exists(destination_path):
            os.remove(destination_path)

        # Если изделие стандартное
        if os.path.exists(source_path):
            shutil.copy2(source_path, destination_path)

        # Если изделие нестандартное, то меняем путь к файлу по-умолчанию
        else:
            destination_path = f'settings/materials'
            file_new_name = f'settings/materials/{self.name}.ini'
            if self.get_laser_type() == 'gas':
                source_path = 'settings/default/materials/default_gas.ini'
                file_old_name = 'settings/materials/default_gas.ini'
            else:
                source_path = 'settings/default/materials/default_solid.ini'
                file_old_name = 'settings/materials/default_solid.ini'

            # Копируем файл в папку назначения
            shutil.copy(
                source_path,
                os.path.join(destination_path)
            )

            # Переименовываем файл
            os.rename(file_old_name, file_new_name)
