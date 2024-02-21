from random import choice

#TODO: change file to file path
class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, file):
        """initializes and reads files, outputs how many words passed """
        # self.file = file
        self.words = []
        self.readfile(file)
        print(f"{len(self.words)} words read")

#TODO: name of class and len(words) = "
    def __repr__(self):
        return f"<current words are: {self.words}>"

#TODO: change to be opened to file_path
    def readfile(self, to_be_opened):
        """method for dunder to output words length"""
        opened_file = open(to_be_opened)
        for line in opened_file:
            self.words.append(line[:-1])
#TODO: use strip method
        opened_file.close()

    def random(self):
        """outputs random word from word list"""
        return choice(self.words)


class SpecialWordFinder(WordFinder):
    """Child class of word finder, skips empty spaces and category names"""
    # def __init__(self, file):
    #     """filters out empty spaces and category names, outputs random word"""
    #     super().__init__(file)
    #     self.words = [word for word in self.words if not word.startswith(
    #         '#') and not word == '']

    #     print(super().random())

    def readfile(self, file_path):
        super().readfile(file_path)
        self.words = [word for word in self.words if not word.startswith('#') and not word == '']


    def __repr__(self):
        return super().__repr__()
