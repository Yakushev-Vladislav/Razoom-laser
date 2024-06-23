import configparser
"""
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
"""

data = [0, 1, 'text']

for item in data:
    print(f'{item} is True')
    if item:
        print(True)
    else:
        print(False)
