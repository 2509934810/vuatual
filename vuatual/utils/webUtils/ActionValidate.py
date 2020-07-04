import os
import time
import random
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
from vuatual.utils.exceptions import CaseFormatError, CaseRunError, ElementNotFound


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


class DownloadHtml_c(object):
    def __init__(self, client, body, filePath, timeout):
        self.client = client
        self.filePath = filePath
        self.timeout = timeout
        self.body = body

    def check(self):
        if not os.path.exists(self.filePath):
            os.makedirs(self.filePath)
        fileName = os.path.join(
            self.filePath, "{}.html".format(self.client.current_url)
        )
        for ele in self.body:
            if not check_element_by_css_can_find(self.client, self.timeout, 0.5, ele):
                raise ElementNotFound("{} not Found".format(ele))
        currentUrl = self.client.current_url
        pageSourceContent = self.client.page_source
        fileName = os.path.join(
            self.filePath, "{}.html".format(random.randrange(1, 1000))
        )
        with open(fileName, "w") as f:
            f.write(pageSourceContent)


class DownloadHtml_x(object):
    def __init__(self, client, body, filePath, timeout):
        self.client = client
        self.filePath = filePath
        self.timeout = timeout
        self.body = body

    def check(self):
        if not os.path.exists(self.filePath):
            os.makedirs(self.filePath)
        fileName = os.path.join(
            self.filePath, "{}.html".format(self.client.current_url)
        )
        for ele in self.body:
            if not check_element_by_xpath_can_find(self.client, self.timeout, 0.5, ele):
                raise ElementNotFound("{} not Found".format(ele))
        currentUrl = self.client.current_url
        pageSourceContent = self.client.page_source
        fileName = os.path.join(
            self.filePath, "{}.html".format(random.randrange(1, 1000))
        )
        with open(fileName, "w") as f:
            f.write(pageSourceContent)


class DownBanner_css(object):
    def __init__(self, client, body, filePath, timeout):
        self.client = client
        self.body = body
        self.filePath = filePath
        self.timeout = timeout

    def check(self):
        if not os.path.exists(self.filePath):
            os.makedirs(self.filePath)
        for ele in self.body:
            if not check_element_by_css_can_find(self.client, self.timeout, 0.5, ele):
                raise ElementNotFound("{} not found".format(ele))
            fileBody = find_element_by_css(self.client, ele).text
            fileName = os.path.join(self.filePath, "{}.html".format(ele))
            with open(fileName, "w") as f:
                f.write(fileBody)


class DownBanner_xpath(object):
    def __init__(self, client, body, filePath, timeout):
        self.client = client
        self.body = body
        self.filePath = filePath
        self.timeout = timeout

    def check(self):
        if not os.path.exists(self.filePath):
            os.makedirs(self.filePath)
        for ele in self.body:
            if not check_element_by_xpath_can_find(self.client, self.timeout, 0.5, ele):
                raise ElementNotFound("{} not found".format(ele))
            fileBody = find_element_by_xPath(self.client, ele).text
            fileName = os.path.join(self.filePath, "{}.html".format(ele))
            with open(fileName, "w") as f:
                f.write(fileBody)
