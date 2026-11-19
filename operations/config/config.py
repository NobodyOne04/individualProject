from configparser import ConfigParser


class Config:
    def __init__(self):
        if hasattr(self, '_Config__configObject'):  # cached instance: already read
            return
        self.__configObject = ConfigParser()
        self.__configObject.read('config/project.conf')

    def get(self, category, key):
        return self.__configObject.get(category, key)

    def __new__(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Config, cls).__new__(cls)
        return cls._instance
