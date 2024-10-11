import logging
import logging.handlers


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
                results = '\n'
                for _, v in kwargs.items():
                    results += f'{v}\n'
                self.logger('log\\app_log.log').info(f'{message}')
                self.logger('log\\calculation\\calc_log.log').info(
                    f'{message}:{results}')
            case 'bmp':  # Запись параметров считанного .bmp файла
                results = '\n'
                for _, v in kwargs.items():
                    results += f'{v}\n'
                self.logger('log\\app_log.log').info(f'{message}')
                self.logger('log\\calculation\\bmp_calc_log.log').info(
                    f'{message}:{results}')
            case 'info':  # Логирование информации
                self.logger('log\\app_log.log').info(f'{message}')
            case 'warning':  # Логирование предупреждений
                self.logger('log\\app_log.log').warning(f'{message}')
                self.logger(
                    'log\\warnings\\app_log.log').warning(f'{message}',
                                                          exc_info=info)
            case 'error':  # Логирование ошибок
                self.logger('log\\app_log.log').error(f'{message}')
                self.logger(
                    'log\\errors\\app_log.log').error(f'{message}',
                                                      exc_info=info)
            case _:  # Логирование любой дополнительной информации
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

        # Не передаем записи журнала обработчикам (исключение дублирования)
        logger.propagate = False

        # Ротация лога при объеме файла больше 1,5 Мб
        handler = logging.handlers.RotatingFileHandler(
            PathName.resource_path(path),
            mode='w',
            encoding='utf-8',
            maxBytes=1_500_000,
            backupCount=5
        )

        # Добавление формата к обработчику
        handler.setFormatter(self.formatter)

        # Проверяем присутствует ли уже обработчик (если да - делаем очистку)
        if logger.hasHandlers():
            logger.handlers.clear()

        # Добавление обработчика к логу
        logger.addHandler(handler)

        return logger
