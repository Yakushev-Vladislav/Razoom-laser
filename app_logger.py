import logging
import logging.handlers


from path_getting import PathName


class AppLogger:
    def __init__(self, name: str, level: str, message: str,
                 exc: bool = False) -> None:
        """
        Класс работы с логом приложения.
        :param name: Имя модуля, из которого происходит запись в лог.
        :param level: Уровень логирования (debug, info, warning, error,
        critical)
        :param message: Текстовое сообщение записи в лог
        :param exc: Переменная записи исключения в лог
        """
        # Создание лога и установка минимального уровня для логирования
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        # Ротация лога при объеме файла больше 500 Кб
        self.handler = logging.handlers.RotatingFileHandler(
            PathName.resource_path(f"log\\app_log.log"),
            mode='w',
            encoding='utf-8',
            maxBytes=500_000,
            backupCount=5
        )

        # Настройка формата для лога
        self.formatter = logging.Formatter(
            "%(asctime)s | %(name)s | <%(levelname)s> | %(message)s"
        )

        # Добавление формата к обработчику
        self.handler.setFormatter(self.formatter)

        # Проверяем присутствует ли уже обработчик (если да - делаем очистку)
        if self.logger.hasHandlers():
            self.logger.handlers.clear()

        # Добавление обработчика к логу
        self.logger.addHandler(self.handler)

        # Непосредственно запись информации в лог
        match level:
            case 'debug':
                self.logger.debug(message)
            case 'info':
                self.logger.info(message)
            case 'warning':
                self.logger.warning(message, exc_info=exc)
            case 'error':
                self.logger.error(message, exc_info=exc)
            case 'critical':
                self.logger.critical(message, exc_info=exc)
            case _:
                self.logger.info(f'{level}:  {message}')
