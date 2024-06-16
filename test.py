file_standard = open(
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
