import pymorphy2
import re


class MorphAnalyzer:

    def __init__(self):
        self.__morph = pymorphy2.MorphAnalyzer()

    def __normolize(self, sentence):
        return re.compile('[a-я]+').findall(sentence.lower())

    def normalForm(self, sentence):
        result = list()
        for word in self.__normolize(sentence):
            try:
                result.append(f"{word}: {self.__morph.parse(word)[0].normal_form}")
            except AttributeError as error:
                pass
        return result

    def grammars(self, sentence):
        result = list()
        for word in self.__normolize(sentence):
            try:
                result.append(f"{word}: {self.__morph.parse(word)[0].tag.cyr_repr}")
            except AttributeError as error:
                pass
        return result

    def inflect(self, sentence, to):
        result = list()
        for word in self.__normolize(sentence):
            try:
                result.append(f"{word}: {self.__morph.parse(word)[0].inflect(frozenset(to)).word}")
            except AttributeError as error:
                pass
        return result

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(MorphAnalyzer, cls).__new__(cls)
        return cls.instance
