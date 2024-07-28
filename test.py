import configparser

test = configparser.ConfigParser()
test.read('settings/material_data.ini', encoding='utf-8')
data = test['MAIN']
my_price = {}
for k, v in data.items():
    my_price[k] = [float(x) for x in v.split(',')][-1]

print(my_price)
