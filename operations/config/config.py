from configparser import ConfigParser


class Config:
    def __init__(self):
        self.__configObject = ConfigParser()
        self.__configObject.read('config/project.conf')
        self.__configObject.sections()

    def get(self, category, key):
        return self.__configObject.get(category, key)

    def __new__(cls):
        if not hasattr(cls, '__instance'):
            cls.__instance = super(Config, cls).__new__(cls)
        return cls.__instance
