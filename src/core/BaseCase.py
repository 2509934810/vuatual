import pytest


class BaseCase(pytest.Item):
    def __init__(self, name, parent, value):
        super.__init__(name, parent)
        self.value = value
        self.name = name

    def runtest(self):
        print(self.value)
