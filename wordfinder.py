from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __init__(self, file):
        self.file = file
        self.files = []
        self.readfile(self.file)


    def readfile(self, to_be_opened):
        opened_file = open(to_be_opened)
        for line in opened_file:
            self.files.append(line[:-1])

        opened_file.close()

        print(f"{len(self.files)} words read")

    def random(self):
        return choice(self.files)

class SpecialWordFinder(WordFinder):
    def __init__(self, file):
        super().__init__(self, file)



