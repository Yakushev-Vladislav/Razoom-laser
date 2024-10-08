import logging
import logging.handlers


from path_getting import PathName


class AppLogger:
    def __init__(self, name: str, level: str, message: str) -> None:
        """
        Класс работы с логом приложения.
        :param name: Имя модуля, из которого происходит запись в лог.
        :param level: Уровень логирования (debug, info, warning, error,
        critical)
        :param message:
        """
        # Создание logger и установка минимального уровня логирования
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        # Ротация лога при объеме файла больше 5 Мб
        self.handler = logging.handlers.RotatingFileHandler(
            PathName.resource_path(f"log\\app_log.log"),
            mode='w',
            encoding='utf-8',
            maxBytes=5000000,
            backupCount=5
        )

        # Настройка формата для logger
        self.formatter = logging.Formatter(
            "%(asctime)s | %(name)s | <%(levelname)s> | %(message)s")

        # Добавление формата к обработчику
        self.handler.setFormatter(self.formatter)
        # Добавление обработчика к logger
        self.logger.addHandler(self.handler)

        # Непосредственно запись информации в лог
        match level:
            case 'debug':
                self.logger.debug(message)
            case 'info':
                self.logger.info(message)
            case 'warning':
                self.logger.warning(message)
            case 'error':
                self.logger.error(message)
            case 'critical':
                self.logger.critical(message)
            case _:
                self.logger.info(f'{level}:  {message}')
