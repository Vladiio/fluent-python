import re
import reprlib


RE_WORLD = re.compile('\w+')


class SentenceIterator:
    def __init__(self, sentence):
        self.sentence = sentence
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            world = self.sentence[self.index]
        except IndexError:
            raise StopIteration
        else:
            self.index += 1
            return world


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORLD.findall(text)

    # def __iter__(self):
        # return iter(self.words)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence({!s})'.format(reprlib.repr(self.text))


def sentence_generator(sentence):
    for world in sentence:
        yield world
