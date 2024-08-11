from materials import Interpolation
import configparser

file_name = 'анодированный алюминий 0.5 мм'
laser_type_config = configparser.ConfigParser()
laser_type_config.read('settings/material_data.ini',
                       encoding='utf-8')
test = Interpolation(file_name)
print(test.get_lower_and_bigger_key(50, 100))
