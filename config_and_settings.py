import configparser

class Config:
    def __init__(self):

        # Чтение файла конфига в переменную main_config
        self.main_config = configparser.ConfigParser()
        self.main_config.read('settings/settings.ini')


    def deffault_settings(self):
        pass

    def is_not_use(self):  # Метод исправления ошибки статичности методов
        pass