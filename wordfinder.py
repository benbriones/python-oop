from random import choice


class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, file):
        """initializes and reads files, outputs how many words passed """
        self.file = file
        self.words = []
        self.readfile(self.file)

    def __repr__(self):
        return f"<current words are: {self.words}>"

    def readfile(self, to_be_opened):
        """method for dunder to output words length"""
        opened_file = open(to_be_opened)
        for line in opened_file:
            self.words.append(line[:-1])

        opened_file.close()

        print(f"{len(self.words)} words read")

    def random(self):
        """outputs random word from word list"""
        return choice(self.words)


class SpecialWordFinder(WordFinder):
    """Child class of word finder, skips empty spaces and category names"""

    def __init__(self, file):
        """filters out empty spaces and category names, outputs random word"""
        super().__init__(file)
        self.words = [word for word in self.words if not word.startswith(
            '#') and not word == '']

        print(super().random())

    def __repr__(self):
        return super().__repr__()
