'''
from configparser import ConfigParser

from pydantic import ConfigError

file = 'test2.pdf'                  # le nom de fichier qui va etre configuré 
config = ConfigParser()
config.read(file)

print(config.sections )
'''
from configparser import ConfigParser

#Get the configparser object
config_object = ConfigParser()



    #Read config.ini file
config_object = ConfigParser()
config_object.read("config.ini")

#Get the password


def getPathBySection(section):
    try:
        value = config_object.get(section, 'path')
        userinfo = config_object[section]
        return value
    except ConfigParser.NoOptionError:
        print(f"No option '{key}' in section 'SETTINGS'")
        return 0
