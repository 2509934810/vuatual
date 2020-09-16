from vuatual.core import BaseCase
import pytest
from vuatual.utils.apiUtils.getSession import getSession
from vuatual.utils.apiUtils import ACTION
from vuatual.utils.exceptions import (
    ApiTypeNotSupport,
    ActionNotSupport,
    RequestConnError,
)


class ApiCase(BaseCase):
    def __init__(self, name, parent, caseItem, authConfig):
        super(BaseCase, self).__init__(name, parent)
        self.caseItem = caseItem
        self.authConfig = authConfig
        self.name = name

    def runtest(self):
        apiType = self.caseItem.get("type")
        path = self.caseItem.get("url")
        url = f"""{self.authConfig.get("protocol")}://{self.authConfig.get("host")}{path}"""
        if apiType == "get":
            # 根据params组成url
            params = self.caseItem.get("params")
            if params:
                url += "?" + "&".join(
                    ["{}={}".format(key, value) for key, value in params.items()]
                )
            try:
                session = getSession().get(url)
            except Exception:
                raise RequestConnError(
                    """===============================\n
                       connection error\n
                       please check the url {}\n
                       ===============================""".format(
                        url
                    )
                )
        elif apiType == "post":
            # 从文件获得post的数据
            headers = {"Content-Type": "application/json"}
            data = self.caseItem.get("data")
            session = getSession().post(url, data=data, headers=headers)
        elif apiType == "delete":
            session = getSession().delete(url)
        else:
            raise ApiTypeNotSupport("only support get post delete")
        for action in self.caseItem.get("check"):
            if action.get("type") not in ACTION.keys():
                raise ActionNotSupport(f"""不支持的Check 类型 {action.get("type")}""")
            ACTION.get(action.get("type"))(session, action, self.authConfig).check()
