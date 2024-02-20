class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """generate our initial count"""
        self.start = start
        self.currentNum = start

    def __repr__(self):
        return f"<current count is {self.currentNum}>"

    def generate(self):
        """add 1 to current number"""
        self.currentNum += 1
        return self.currentNum - 1

    def reset(self):
        """reset to original start number"""
        self.currentNum = self.start
