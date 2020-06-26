from core import BaseCase


class WebCase(BaseCase):
    def __init__(self, name, parent, value):
        super.__init__(name, parent)
        self.name = self.name
        self.value = value

    def runtest(self):
        print(self.value)


# import abc
# from selenium.webdriver import Chrome

# class BaseCase(metaclass = abc.ABCMeta):
#     @abc.abstractmethod
#     def validate(self):
#         pass


# class WebCase(BaseCase):
#     def validate(self):
#         client = Chrome()
#         client.get("http://www.baidu.com")
