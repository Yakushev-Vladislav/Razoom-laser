import os
import shutil
import logging


from path_getting import PathName


class AppLogger:
    def __init__(self, name: str, level: str, message: str, info: bool =
                 False, *args, **kwargs) -> None:
        """
        Класс работы с логом приложения.
        :param name: Имя модуля, из которого происходит запись в лог;
        :param level: Уровень логирования (debug, info, warning, error,
        critical) пользовательский уровень calc позволяет записать подробный
        лог о расчете, пользовательский уровень bmp позволяет записать
        подробный лог о характеристиках .bmp изображения;
        :param message: Текстовое сообщение записи в лог;
        :param info: Переменная записи подробной информации об исключении
        (True - если требуется информация, False (по умолчанию) - если не
        требуется).
        :param args: Кортеж позиционных аргументов.
        :param kwargs: Словарь именованных аргументов. В расчетных методах
        передаются результаты.
        """

        # Создание переменных для передачи методам
        self.name = name

        # Убираем предупреждение о неиспользованном параметре
        for _ in args:
            pass

        # Настройка формата для лога
        self.formatter = logging.Formatter(
            "%(asctime)s | %(name)s | <%(levelname)s> | %(message)s"
        )

        # Непосредственно запись информации в лог
        match level.lower():
            case 'calc':  # Запись результатов расчета стоимостей / времени
                # Формирование результатов расчетов для записи
                results = '\n'
                for _, v in kwargs.items():
                    results += f'{v}\n'

                # Ротация лога, если это необходимо
                self.manual_rotation_log(
                    'log\\app_log.log',
                    'log\\app_log_backup.log'
                )
                self.manual_rotation_log(
                    'log\\calculation\\calc_log.log',
                    'log\\calculation\\calc_log_backup.log',
                    bytes_size=1_000_000
                )

                # Запись в лог
                self.logger('log\\app_log.log').info(f'{message}')
                self.logger('log\\calculation\\calc_log.log').info(
                    f'{message}:{results}')
            case 'bmp':  # Запись параметров считанного .bmp файла
                # Формирование параметров изображения для записи
                results = '\n'
                for _, v in kwargs.items():
                    results += f'{v}\n'

                # Ротация лога, если это необходимо
                self.manual_rotation_log(
                    'log\\app_log.log',
                    'log\\app_log_backup.log'
                )
                self.manual_rotation_log(
                    'log\\calculation\\bmp_calc_log.log',
                    'log\\calculation\\bmp_calc_log_backup.log',
                    bytes_size=500_000
                )

                # Запись в лог
                self.logger('log\\app_log.log').info(f'{message}')
                self.logger('log\\calculation\\bmp_calc_log.log').info(
                    f'{message}:{results}')
            case 'info':  # Логирование информации
                # Ротация лога, если это необходимо
                self.manual_rotation_log(
                    'log\\app_log.log',
                    'log\\app_log_backup.log'
                )
                # Запись в лог
                self.logger('log\\app_log.log').info(f'{message}')
            case 'warning':  # Логирование предупреждений
                # Ротация лога, если это необходимо
                self.manual_rotation_log(
                    'log\\app_log.log',
                    'log\\app_log_backup.log'
                )
                self.manual_rotation_log(
                    'log\\warnings\\warnings_log.log',
                    'log\\warnings\\warnings_log_backup.log'
                )

                # Запись в лог
                self.logger('log\\app_log.log').warning(f'{message}')
                self.logger(
                    'log\\warnings\\warnings_log.log').warning(
                    f'{message}', exc_info=info)
            case 'error':  # Логирование ошибок
                # Ротация лога, если это необходимо
                self.manual_rotation_log(
                    'log\\app_log.log',
                    'log\\app_log_backup.log'
                )
                self.manual_rotation_log(
                    'log\\errors\\errors_log.log',
                    'log\\errors\\errors_log_backup.log'
                )

                # Запись в лог
                self.logger('log\\app_log.log').error(f'{message}')
                self.logger(
                    'log\\errors\\errors_log.log').error(
                    f'{message}', exc_info=info)
            case _:  # Логирование любой дополнительной информации
                # Ротация лога, если это необходимо
                self.manual_rotation_log(
                    'log\\app_log.log',
                    'log\\app_log_backup.log'
                )
                # Запись в лог
                self.logger('log\\app_log.log').info(f'{level}:  {message}')

    def logger(self, path: str) -> logging.Logger:
        """
        Метод возвращает настроенный пользователем лог.
        :param path: Путь к файлу лога
        :return: Лог (в назначенном пути), в который передается сообщение.
        """
        # Создание лога и установка минимального уровня для логирования
        logger = logging.getLogger(self.name)
        logger.setLevel(logging.DEBUG)

        # Проверяем присутствует ли уже обработчик (если да - делаем очистку)
        if logger.hasHandlers():
            logger.handlers.clear()

        # Не передаем записи журнала обработчикам (исключение дублирования)
        logger.propagate = False

        # Создание обработчика
        handler = logging.FileHandler(
            PathName.resource_path(path),
            encoding='utf-8')

        # Добавление формата к обработчику
        handler.setFormatter(self.formatter)

        # Добавление обработчика к логу
        logger.addHandler(handler)

        return logger

    @staticmethod
    def manual_rotation_log(
                   path_log_file: str,
                   backup_log_file: str,
                   bytes_size: int = 1_500_000) -> None:
        """
        Ручная ротация лога. Т.к. при использовании стандартного метода
        ротации лога по объему файла выходит ошибка: PermissionError:
        [WinError 32] Процесс не может получить доступ к файлу, так как
        этот файл занят другим процессом: <Путь к файлу лога> ->
        <Путь к backup файлу лога>.

        :param path_log_file: Путь к файлу лога;
        :param backup_log_file: Путь к backup файлу лога;
        :param bytes_size: Объем файла лога, при котором происходит ротация
        (по-умолчанию 1.5 Мб).
        """
        try:
            # Если объем файла больше заданного, то делаем ротацию
            if (os.path.exists(PathName.resource_path(path_log_file)) and
                    os.path.getsize(PathName.resource_path(path_log_file))
                    >= bytes_size):
                # Копируем данные в backup файл
                with open(
                        PathName.resource_path(path_log_file),
                        'r',
                        encoding='utf-8') as source_file:
                    with open(
                            PathName.resource_path(backup_log_file),
                            'w',
                            encoding='utf-8') as backup_file:
                        shutil.copyfileobj(source_file, backup_file)
                # Очищаем данные из основного файла
                with open(
                        PathName.resource_path(path_log_file),
                        'w',
                        encoding='utf-8') as source_file:
                    source_file.write('')
        except Exception as e:
            _ = e
            pass
