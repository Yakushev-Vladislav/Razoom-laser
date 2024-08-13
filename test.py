from materials import Interpolation
import configparser

file_name = 'оргстекло 4 мм'
laser_type_config = configparser.ConfigParser()
laser_type_config.read('settings/material_data.ini',
                       encoding='utf-8')
test = Interpolation(file_name)
width = 100
height = 250
num = 100
print(f'{test.get_lower_and_bigger_key(width, height)}  --  {num} шт.')
print('_'*70)
print(f'{test.get_cost(height, width, num):.0f} руб/шт')
print(f'{(test.get_cost(height, width, num) * num):.0f} руб итого')
print('_'*70)
