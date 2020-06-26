import pytest
import yaml
from cases import CASETYPE


def pytest_collection_modifyitems(config, items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")
        print(item.name)


# def pytest_collect_directory(path, parent):
# print(path. parent)
# def pytest_collect_file(path, parent):
#     print(path, parent)


def pytest_collect_file(parent, path):
    allowYamlFile = [".yaml", ".yml"]
    if path.ext in allowYamlFile and path.basename.startswitch("test"):
        return YamlFile(path, parent)


class YamlFile(pytest.File):
    def collect(self):
        cases = yaml.safe_load(self.fspath.open(encoding="utf-8"))
        for key, value in cases.items():
            yield CASETYPE.get("webcase")(name, self, value)


def pytest_addoption(parser):
    parser.addoption(
        "--cases", action="append", default=[], help="please input the Case Path"
    )
