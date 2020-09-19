import os
import time
from datetime import datetime
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
    def __init__(self, client, config):
        self.client = client
        self.config = config

    def check(self, checkBody):
        timeout = checkBody.get("timeout")
        checkBody = checkBody.get("body")
        for body in checkBody:
            check_element_by_css_can_find(self.client, timeout, 0.5, body)
            find_element_by_css(self.client, body)


class FindXpathValidate(object):
    def __init__(self, client, config):
        self.client = client
        self.config = config

    def check(self, checkBody):
        timeout = checkBody.get("timeout")
        checkBody = checkBody.get("body")
        for body in checkBody:
            check_element_by_xpath_can_find(self.client, timeout, 0.5, body)
            find_element_by_xPath(self.client, body)


class ClickCssValidate(object):
    def __init__(self, client, config):
        self.client = client
        self.config = config

    def check(self, checkBody):
        timeout = checkBody.get("timeout")
        checkBody = checkBody.get("body")
        for body in checkBody:
            check_element_by_css_can_click(self.client, timeout, 0.5, body)
            find_element_by_css(self.client, body).click()


class ClickXpathValidate(object):
    def __init__(self, client, config):
        self.client = client
        self.config = config

    def check(self, checkBody):
        timeout = checkBody.get("timeout")
        checkBody = checkBody.get("body")
        for body in checkBody:
            check_element_by_xpath_can_click(self.client, timeout, 0.5, body)
            find_element_by_xPath(self.client, body).click()


class TakeScreenShot(object):
    def __init__(self, client, config):
        self.client = client
        self.config = config

    def check(self, checkBody):
        basePath = self.config.get("filepath")
        cur_time = datetime.strftime("YY:mm:dd-HH:MM:SS", datetime.now())
        filename = f"screenshot_{cur_time}.png"
        screenShotPath = os.path.join(basePath, f"/screenshot/{filename}.png")
        self.client.get_screenshot_as_file(screenShotPath)


class InputCss(object):
    def __init__(self, client, config):
        self.client = client
        self.config = config

    def check(self, checkBody):
        body = checkBody.get("body")
        timeout = checkBody.get("timeout")
        if len(body) != 2:
            raise CaseFormatError(
                "the case body should be a list and the first is css the second is sendKey"
            )
        check_element_by_css_can_find(self.client, timeout, 0.5, body[0])
        try:
            find_element_by_css(self.client, body[0]).send_keys(body[1])
        except Exception:
            raise CaseRunError("case run error")


class InputXpath(object):
    def __init__(self, client, config):
        self.client = client
        self.config = config

    def check(self, checkBody):
        body = checkBody.get("body")
        timeout = checkBody.get("timeout")
        if len(body) != 2:
            raise CaseFormatError(
                "the case body should be a list and the first is css the second is sendKey"
            )
        check_element_by_xpath_can_find(self.client, timeout, 0.5, body[0])
        find_element_by_xPath(self.client, body[0]).send_keys(body[1])


class Sleep(object):
    def __init__(self, client, config):
        self.client = client
        self.config = config

    def check(self, checkBody):
        timeout = checkBody.get("timeout")
        assert isinstance(timeout, int)
        time.sleep(timeout)


class DownloadHtml_c(object):
    def __init__(self, client, config):
        self.client = client
        self.filePath = config.get("filepath")
        if not os.path.exists(self.filePath):
            os.makedirs(self.filePath)
        self.config = config

    def check(self, checkBody):
        timeout = checkBody.get("timeout")
        body = checkBody.get("body")
        for ele in body:
            if not check_element_by_css_can_find(self.client, timeout, 0.5, ele):
                raise ElementNotFound("{} not Found".format(ele))
        currentUrl = self.client.current_url
        pageSourceContent = self.client.page_source
        fileName = os.path.join(
            self.filePath, "{}.html".format(random.randrange(1, 1000))
        )
        with open(fileName, "w") as f:
            f.write(pageSourceContent)


class DownloadHtml_x(object):
    def __init__(self, client, config):
        self.client = client
        self.filePath = config.get("filepath")
        if not os.path.exists(self.filePath):
            os.makedirs(self.filePath)
        self.config = config

    def check(self, checkBody):
        timeout = checkBody.get("timeout")
        body = checkBody.get("body")
        for ele in body:
            if not check_element_by_xpath_can_find(self.client, timeout, 0.5, ele):
                raise ElementNotFound("{} not Found".format(ele))
        currentUrl = self.client.current_url
        pageSourceContent = self.client.page_source
        fileName = os.path.join(
            self.filePath, "{}.html".format(random.randrange(1, 1000))
        )
        with open(fileName, "w") as f:
            f.write(pageSourceContent)


class DownBanner_css(object):
    def __init__(self, client, config):
        self.client = client
        self.config = config
        self.filePath = config.get("filepath")
        if not os.path.exists(self.filePath):
            os.makedirs(self.filePath)

    def check(self, checkBody):
        timeout = checkBody.get("timeout")
        body = checkBody.get("body")
        for ele in body:
            if not check_element_by_css_can_find(self.client, timeout, 0.5, ele):
                raise ElementNotFound("{} not found".format(ele))
            fileBody = find_element_by_css(self.client, ele).text
            fileName = os.path.join(self.filePath, "{}.html".format(ele))
            with open(fileName, "w") as f:
                f.write(fileBody)


class DownBanner_xpath(object):
    def __init__(self, client, config):
        self.client = client
        self.filePath = config.get("filepath")
        if not os.path.exists(self.filePath):
            os.makedirs(self.filePath)
        self.config = config

    def check(self, checkBody):
        timeout = checkBody.get("timeout", 5)
        body = checkBody.get("body")
        for ele in body:
            if not check_element_by_xpath_can_find(self.client, timeout, 0.5, ele):
                raise ElementNotFound("{} not found".format(ele))
            fileBody = find_element_by_xPath(self.client, ele).text
            fileName = os.path.join(self.filePath, "{}.html".format(ele))
            with open(fileName, "w") as f:
                f.write(fileBody)
