import configparser

my_config = configparser.ConfigParser()
my_config.read('settings/settings.ini')
temp = [float(x) for x in my_config['GRADATION']['depth'].split(', ')]

print(temp)
