from random import choice


class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, file_path):
        """initializes and reads files, outputs how many words passed """
        self.words = self.read_file(file_path)
        print(f"{len(self.words)} words read")

    def __repr__(self):
        return f"<{self.__class__.__name__} words length: {len(self.words)} words>"

    def read_file(self, file_path):
        """method for dunder to output words length"""
        word_list = []

        opened_file = open(file_path)
        for line in opened_file:
            word_list.append(line.strip())

        opened_file.close()

        return word_list

    def random(self):
        """outputs random word from word list"""
        return choice(self.words)


class SpecialWordFinder(WordFinder):
    """Child class of word finder, skips empty spaces and category names"""

    def read_file(self, file_path):
        """returns list of words but filters out category names and empty spaces"""
        return [word for word in super().read_file(file_path) if not word.startswith('#') and not word == '']

    # def __repr__(self):
    #     return super().__repr__()
