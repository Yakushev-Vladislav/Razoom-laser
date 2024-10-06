class MonochromeBMP:
    def __init__(self, file_path: str):
        """
        Инициализирует объект MonochromeBMP для работы с монохромным
        BMP изображением.
        :param file_path: Путь к BMP файлу.
        """
        self.file_path = file_path
        self.width = 0
        self.height = 0
        self.pixel_data = []
        self._read_bmp()

    def _read_bmp(self):
        """
        Читает BMP файл, извлекая ширину, высоту и данные пикселей.
        Этот метод анализирует заголовок BMP файла для получения информации
        о размере изображения, а затем считывает битовые данные
        изображения, представляющие черно-белые пиксели. Изображение в
        формате 1-битного BMP имеет выравнивание строк до кратного 4 байтам,
        что также обрабатывается в этом методе.

        :raises: FileNotFoundError, если файл не может быть найден или прочитан
        """
        with open(self.file_path, 'rb') as f:
            # Чтение заголовка BMP файла
            f.seek(18)  # Смещение к полю ширины изображения
            self.width = int.from_bytes(f.read(4), byteorder='little')
            self.height = int.from_bytes(f.read(4), byteorder='little')

            # Чтение начала массива пикселей
            f.seek(10)
            pixel_array_offset = int.from_bytes(f.read(4), byteorder='little')

            # Переход к массиву пикселей
            f.seek(pixel_array_offset)

            # В 1-битном изображении каждая строка выравнивается до ближайшего
            # кратного 4 байтам

            # Считаем, сколько байт необходимо для
            # хранения строки шириной self.width пикселей
            row_size = (self.width + 7) // 8
            # Количество байтов выравнивания (до кратности 4)
            padding = (row_size + 3) // 4 * 4 - row_size

            # Чтение данных пикселей
            for y in range(self.height):
                row = []
                for x in range(row_size):
                    byte = f.read(1)
                    byte_value = ord(byte)
                    for bit in range(8):
                        # Проверяем, что не выходим за пределы ширины
                        if x * 8 + bit < self.width:
                            row.append(
                                1 if byte_value & (1 << (7 - bit)) else 0)
                self.pixel_data.append(row)
                f.read(padding)  # Пропускаем байты выравнивания

    def count_pixels(self) -> tuple:
        """
        Подсчитывает количество белых и черных пикселей в изображении.
        Проходит по каждому пикселю изображения и подсчитывает количество
         черных (0) и белых (1) пикселей.

        :return: Кортеж (white_pixels, black_pixels), где:
                 - white_pixels: количество белых пикселей (значение 1)
                 - black_pixels: количество черных пикселей (значение 0)
        """
        white_pixels = 0
        black_pixels = 0

        for row in self.pixel_data:
            white_pixels += row.count(1)
            black_pixels += row.count(0)

        return white_pixels, black_pixels
