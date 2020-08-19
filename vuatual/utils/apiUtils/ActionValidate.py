from vuatual.utils.SaveDb.mysql import Vmysql
import re
from vuatual.utils.logs import logger
from vuatual.utils.exceptions import (
    ValidateError,
    CaseBodyNotSupport,
    OtherParserError
)
# add save title


class SaveTitle(object):
    def __init__(self, client, actionItem, caseConfig):
        self.client = client
        self.actionItem = actionItem
        self.caseConfig = caseConfig

    def check(self):
        titleFormat = re.compile(r"<title>(.*)</title>")
        titles = re.findall(titleFormat, self.client.text)
        logger.info(titles)


class CheckStatusCode(object):
    def __init__(self, client,  actionItem, caseConfig):
        self.client = client
        self.actionItem = actionItem
        self.caseConfig = caseConfig

    def check(self):
        if self.client.status_code != self.actionItem.get("statusCode"):
            raise ValidateError("验证返回码失败")


class CheckJsonBody(object):
    def __init__(self, client, actionItem, caseConfig):
        self.client = client
        self.actionItem = actionItem
        self.caseConfig = caseConfig

    def check(self):
        try:
            json_body = self.client.json()
        except Exception as e:
            raise OtherParserError("other error")
        for key, value in self.actionItem.get("body").items():
            if isinstance(value, int) or isinstance(value, str):
                if json_body.get(key) != value:
                    raise ValidateError(f"验证返回体-{key}-失败")
            else:
                raise CaseBodyNotSupport(
                    f"不支持的检查body类型 key = {key}-- type(value){type(value)}")
