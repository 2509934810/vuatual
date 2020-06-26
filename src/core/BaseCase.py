import pytest


class BaseCase(pytest.Item):
    def __init__(self, name, parent, caseItem):
        super(BaseCase, self).__init__(parent, name)
        self.caseItem = caseItem
        self.name = name

    def runtest(self):
        print(self.caseItem)
