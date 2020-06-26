from core import BaseCase
import pytest
from selenium import webdriver


class WebCase(BaseCase):
    def __init__(self, name, parent, caseItem, authConfig):
        super(BaseCase, self).__init__(name, parent)
        self.caseItem = caseItem
        self.authConfig = authConfig

    def runtest(self):
        client = webdriver.Chrome()
        client.get("http://www.baidu.com")
        print(self.caseItem)
