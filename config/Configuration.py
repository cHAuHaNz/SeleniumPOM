from configparser import ConfigParser


def read_value(section, key):
    parser = ConfigParser()
    parser.read('config/config.ini')
    return parser.get(section, key)
