import configparser
import os

path = os.path.join(os.getcwd(), '03-application/chapter19/config.ini')
inifile = configparser.ConfigParser()
inifile.read(path, 'UTF-8')

print(inifile.get('settings', 'host'))
print(inifile.get('settings', 'port'))

print(inifile.get('system', 'os'))
print(inifile.get('system', 'version'))
print(inifile.get('system', 'path'))

print(inifile.get('user', 'name'))
print(inifile.get('user', 'password'))
print(inifile.get('user', 'mail'))