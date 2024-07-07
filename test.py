import configparser

my_config = configparser.ConfigParser()
my_config.read('settings/settings.ini', encoding='utf-8')
temp = my_config['STANDARD']
for k, v in temp.items():
    print(f'{k} = {v}')
