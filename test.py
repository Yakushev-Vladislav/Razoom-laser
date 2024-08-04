import configparser

my_data = []
temp_file = configparser.ConfigParser()
temp_file.read('settings/material_data.ini', encoding='utf-8')
temp_data = temp_file['MAIN']
for k, v in temp_data.items():
    temp = [k]
    temp.extend([float(x) for x in v.split(',')])
    my_data.append(temp)

print(*my_data, sep='\n')


