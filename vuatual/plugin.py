import pytest
import yaml
from vuatual.cases import CASETYPE
from vuatual.utils.exceptions import CaseParserError, CaseTypeNotFound


def pytest_collection_modifyitems(config, items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


# def pytest_collect_directory(path, parent):
# print(path. parent)
# def pytest_collect_file(path, parent):
#     print(path, parent)


def pytest_collect_file(parent, path):
    allowYamlFile = [".yaml", ".yml"]
    if path.ext in allowYamlFile and path.basename.startswith("test"):
        return YamlFile(path, parent)


class YamlFile(pytest.File):
    def collect(self):
        items = yaml.safe_load(self.fspath.open(encoding="utf-8"))
        if not isinstance(items, dict):
            raise CaseParserError("case file must be a dict")
        caseType, cases, authConfig = (
            items.get("type"),
            items.get("cases"),
            items.get("config"),
        )
        # check case
        _checkCaseType(caseType)
        for case in cases:
            yield CASETYPE.get(caseType)(case.get("name"), self, case, authConfig)


def _checkCaseType(caseType):
    if caseType not in CASETYPE.keys():
        raise CaseTypeNotFound(
            "the {} case is not supported in our framework".format(caseType)
        )


def pytest_addoption(parser):
    parser.addoption(
        "--cases", action="append", default=[], help="please input the Case Path"
    )
