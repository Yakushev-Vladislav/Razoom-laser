"""file_standard = open(
    'settings/standard_grav.txt',
    'r',
    encoding='utf-8'
)
standard_prices = file_standard.readlines()
file_standard.close()
my_dict = dict()
for item in standard_prices[2::]:
    temp = item.split(': ')
    my_dict[temp[0]] = int(temp[1])
print(my_dict)
"""
import configparser

config = configparser.ConfigParser()
config.read('settings/settings.ini')

print(config.sections())
print()

for k in config['MAIN']:
    print(f"{k} = {config['MAIN'][k]}")
print('-*-'*20)
for k in config['STANDARD']:
    print(f"{k} = {config['STANDARD'][k]}")
print('-*-'*20)
for k in config['RATIO_SETTINGS']:
    print(f"{k} = {config['RATIO_SETTINGS'][k]}")