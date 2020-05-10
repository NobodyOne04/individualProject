from configparser import ConfigParser


class Config:
    def __init__(self):
        self.__dataConfigObject = ConfigParser()
        self.__dataConfigObject.read('config/project.conf')
        self.__dataConfigObject.sections()

    def get(self, category, key):
        return self.__dataConfigObject.get(category, key)

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Config, cls).__new__(cls)
        return cls.instance
