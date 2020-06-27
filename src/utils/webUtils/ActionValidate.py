import os
import time
from .clientAction import (
    find_element_by_css,
    find_element_by_xPath,
    find_elements_by_css,
    find_elements_by_xPath,
)
from .clientAction import (
    check_element_by_css_can_click,
    check_element_by_css_can_find,
    check_element_by_xpath_can_click,
    check_element_by_xpath_can_find,
)
from utils.exceptions import CaseFormatError, CaseRunError


class FindCssValidate(object):
    def __init__(self, client, body, timeout):
        self.client = client
        self.body = body
        self.timeout = timeout

    def check(self):
        for body in self.body:
            check_element_by_css_can_find(self.client, self.timeout, 0.5, body)
            find_element_by_css(self.client, body)


class FindXpathValidate(object):
    def __init__(self, client, body, timeout):
        self.client = client
        self.body = body
        self.timeout = timeout

    def check(self):
        for body in self.body:
            check_element_by_xpath_can_find(self.client, self.timeout, 0.5, body)
            find_element_by_xPath(self.client, body)


class ClickCssValidate(object):
    def __init__(self, client, body, timeout):
        self.client = client
        self.body = body
        self.timeout = timeout

    def check(self):
        for body in self.body:
            check_element_by_css_can_click(self.client, self.timeout, 0.5, body)
            find_element_by_css(self.client, body).click()


class ClickXpathValidate(object):
    def __init__(self, client, body, timeout):
        self.client = client
        self.body = body
        self.timeout = timeout

    def check(self):
        for body in self.body:
            check_element_by_xpath_can_click(self.client, self.timeout, 0.5, body)
            find_element_by_xPath(self.client, body).click()


class TakeScreenShot(object):
    def __init__(self, client, pngFile):
        self.client = client
        self.pngFile = pngFile

    def check(self):
        self.client.get_screenshot_as_file(self.pngFile)


class InputCss(object):
    def __init__(self, client, body, timeout):
        self.client = client
        self.body = body
        self.timeout = timeout

    def check(self):
        if len(self.body) != 2:
            raise CaseFormatError(
                "the case body should be a list and the first is css the second is sendKey"
            )
        check_element_by_css_can_find(self.client, self.timeout, 0.5, self.body[0])
        try:
            find_element_by_css(client, self.body[0]).send_keys(self.body[1])
        except Exception:
            raise CaseRunError("case run error")


class InputXpath(object):
    def __init__(self, client, body, timeout):
        self.client = client
        self.body = body
        self.timeout = timeout

    def check(self):
        if len(self.body) != 2:
            raise CaseFormatError(
                "the case body should be a list and the first is xpath the second is sendKey"
            )
        check_element_by_xpath_can_find(self.client, self.timeout, 0.5, self.body[0])
        find_element_by_xPath(self.client, self.body[0]).send_keys(self.body[1])


class Sleep(object):
    def __init__(self, client, body):
        self.client = client
        self.body = body

    def check(self):
        time.sleep(self.body)


from selenium import webdriver

client = webdriver.Chrome()


class DownloadHtml(object):
    def __init__(self, client, filePath):
        self.client = client
        self.filePath = filePath

    def check(self):
        if not os.path.exists(self.filePath):
            os.makedirs(self.filePath)
        fileName = os.path.join(
            self.filePath, "{}.html".format(self.client.current_url)
        )
        # to add download
