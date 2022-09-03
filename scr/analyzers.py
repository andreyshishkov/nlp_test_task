from natasha import NamesExtractor
from natasha import MorphVocab
import numpy as np
import re

morph_vocab = MorphVocab()
name_extractor = NamesExtractor(morph_vocab)


class GreetingFinder:

    def __init__(self):
        self._greetings = ['здравствуйте',
                           'добрый день',
                           'приветствовать']

    def add_greeting(self, greeting):
        if type(greeting) == str:
            self._greetings.append(greeting)

    def is_greeting(self, text):
        lower_text = text.lower()
        if any(greeting in lower_text for greeting in self._greetings):
            return True
        return False


class IntroduceFinder:

    def __init__(self):
        self._introducing = ['меня зовут']

    def add_introducing(self, introducing):
        if type(introducing) == str:
            self._introducing.append(introducing)

    def is_introducing(self, text):
        lower_text = text.lower()
        if any(introducing in lower_text for introducing in self._introducing):
            return True
        return False


class NameFinder:

    def __init__(self):
        self._name_extractor = NamesExtractor(MorphVocab())

    def find_name(self, text):
        if not IntroduceFinder().is_introducing(text):
            return np.NAN
        names = self._name_extractor(text)
        if names:
            for name in names:
                name_parts = name.as_json['fact'].__dict__.values()
                name = ' '.join([part for part in name_parts if part is not None])
                return name

        return np.NAN
