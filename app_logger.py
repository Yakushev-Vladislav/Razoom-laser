import logging
import logging.handlers


from path_getting import PathName


class AppLogger:
    def __init__(self, name: str, level: str, message: str, info: bool =
                 False) -> None:
        """
        Класс работы с логом приложения.
        :param name: Имя модуля, из которого происходит запись в лог.
        :param level: Уровень логирования (debug, info, warning, error,
        critical)
        :param message: Текстовое сообщение записи в лог
        """
        # Создание переменных для передачи методам
        self.name = name

        # Настройка формата для лога
        self.formatter = logging.Formatter(
            "%(asctime)s | %(name)s | <%(levelname)s> | %(message)s"
        )

        # Непосредственно запись информации в лог
        match level:
            case 'calc':
                self.logger('log\\app_log.log').info(f'{message}')
                self.logger('log\\calculation\\calc_log.log').info(
                    f'{message}')
            case 'info':
                self.logger('log\\app_log.log').info(f'{message}')
            case 'warning':
                self.logger('log\\app_log.log').warning(f'{message}')
                self.logger(
                    'log\\warnings\\app_log.log').warning(f'{message}',
                                                          exc_info=info)
            case 'error':
                self.logger('log\\app_log.log').error(f'{message}')
                self.logger(
                    'log\\errors\\app_log.log').error(f'{message}',
                                                      exc_info=info)
            case _:
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

        # Ротация лога при объеме файла больше 500 Кб
        handler = logging.handlers.RotatingFileHandler(
            PathName.resource_path(path),
            mode='w',
            encoding='utf-8',
            maxBytes=500_000,
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
