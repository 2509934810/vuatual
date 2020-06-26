import os
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
