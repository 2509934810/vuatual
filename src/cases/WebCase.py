from core import BaseCase
import pytest
import os
from selenium import webdriver
from utils.webUtils.clientAction import (
    check_element_by_css_can_click,
    check_element_by_css_can_find,
)
from utils.webUtils.getClient import getClient
from utils.webUtils import ACTION


class WebCase(BaseCase):
    def __init__(self, name, parent, caseItem, authConfig):
        super(BaseCase, self).__init__(name, parent)
        self.caseItem = caseItem
        self.authConfig = authConfig
        self.name = name

    def runtest(self):
        client = getClient(
            self.authConfig.get("browserType", "chrome"),
            executePath=self.authConfig.get(
                "browserPath", "/usr/local/bin/chromedriver"
            ),
        )
        # to add check case format
        try:
            client.get(self.caseItem.get("url"))
            for checkbody in self.caseItem.get("check"):
                _runcheck(client, self.name, checkbody)
        finally:
            client.quit()


def _runcheck(client, name, checkBody):
    body = checkBody.get("body")
    checkType = checkBody.get("type")
    timeout = checkBody.get("timeout")
    if checkType == "takeshot":
        filePath = os.path.join(os.path.abspath(os.path.curdir), "tmp/screenshot")
        if not os.path.exists(filePath):
            os.makedirs(filePath)
        fileName = os.path.join(filePath, "{}_{}.png".format(name, body))
        ACTION.get(checkType)(client, fileName).check()
    else:
        ACTION.get(checkType)(client, body, timeout).check()
