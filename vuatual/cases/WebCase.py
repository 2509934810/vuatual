from vuatual.core import BaseCase
import pytest
import os
from selenium import webdriver
from vuatual.utils.webUtils.clientAction import (
    check_element_by_css_can_click,
    check_element_by_css_can_find,
)
from vuatual.utils.webUtils.getClient import getClient
from vuatual.utils.webUtils import ACTION
from vuatual.utils.exceptions import ChromeDriverError, ActionCheckError


class WebCase(BaseCase):
    def __init__(self, name, parent, caseItem, authConfig):
        super(BaseCase, self).__init__(name, parent)
        self.caseItem = caseItem
        self.authConfig = authConfig
        self.name = name

    def runtest(self):
        try:
            client = getClient(
                self.authConfig.get("browserType", "chrome"),
                executePath=self.authConfig.get(
                    "browserPath", "/usr/local/bin/chromedriver"
                ),
            )
        except Exception:
            raise ChromeDriverError(
                """
                    =========================chrome driver error=======================================\n
                    chrome driver not found in path\n
                    Please Download  the plugin in http://npm.taobao.org/mirrors/chromedriver/ \n
                    ===================================================================================\n
                """
            )
        # to add check case format
        try:
            client.get(self.caseItem.get("url"))
            for checkbody in self.caseItem.get("check"):
                _runcheck(client, self.name, checkbody, self.authConfig)
        finally:
            client.quit()


def _check_path_exist(basepath):
    if not os.path.exists(basepath):
        os.makedirs(basepath)


def _runcheck(client, name, checkBody, config):
    checkType = checkBody.get("type")
    basepath = config.get("filepath", "./tmp")
    _check_path_exist(basepath)
    # 确定验证类型
    ACTION_KEYS = ACTION.keys()
    try:
        assert checkType in ACTION_KEYS
    except AssertionError:
        raise ActionCheckError(
            f"""
            {checkType} is not a ActionType
            actionType contains {ACTION_KEYS}
        """
        )
    ACTION.get(checkType)(client, config).check(checkBody)
    # if checkType == "takeshot":
    #     filePath = os.path.join(os.path.abspath(os.path.curdir), "tmp/screenshot")
    #     if not os.path.exists(filePath):
    #         os.makedirs(filePath)
    #     fileName = os.path.join(filePath, "{}_{}.png".format(name, body))
    #     ACTION.get(checkType)(client, fileName).check()
    # elif checkType == "sleep":
    #     ACTION.get(checkType)(client, body).check()
    # elif (
    #     checkType == "dwn_html_css"
    #     or checkType == "dwn_html_xpath"
    #     or checkType == "dwn_banner_css"
    #     or checkType == "dwn_banner_xpath"
    # ):
    #     ACTION.get(checkType)(client, body, filePath, timeout).check()
    # else:
    #     ACTION.get(checkType)(client, body, timeout).check()
