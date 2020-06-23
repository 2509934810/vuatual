
import abc
from selenium.webdriver import Chrome

class BaseCase(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def validate(self):
        pass


class WebCase(BaseCase):
    def validate(self):
        client = Chrome()
        client.get("http://www.baidu.com")