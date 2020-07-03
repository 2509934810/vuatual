from core import BaseCase
import pytest
from utils.apiUtils.getSession import getSession
from utils.apiUtils import ACTION


class ApiCase(BaseCase):
    def __init__(self, name, parent, caseItem, authConfig):
        super(BaseCase, self).__init__(name, parent)
        self.caseItem = caseItem
        self.authConfig = authConfig
        self.name = name

    def runtest(self):
        apiType = self.caseItem.get("type")
        url = self.caseItem.get("ip")
        if apiType == "get":
            session = getSession().get(url)
        else:
            session = getSession().post(url)
        for action in self.caseItem.get("check"):
            ACTION.get(action.get("type"))(
                session, self.caseItem, self.authConfig
            ).check()
