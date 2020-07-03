from utils.SaveDb.mysql import Vmysql
import re
from utils.logs import logger

# add save title
class SaveTitle(object):
    def __init__(self, client, caseItem, caseConfig):
        self.client = client
        self.caseItem = caseItem
        self.caseConfig = caseConfig

    def check(self):
        titleFormat = re.compile(r"<title>([.*?])<title>")
        titles = re.findall(titleFormat, self.client.text)
        logger.info(titles)
