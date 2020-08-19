class CaseParserError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class CaseTypeNotFound(Exception):
    """[不支持的Case类型]

    Args:
        Exception ([type]): [description]
    """

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class CaseFormatError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class CaseRunError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class ElementNotFound(Exception):
    def __init__(self):
        self.msg = msg

    def __str__(self):
        return self.msg


class DbConnection(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class SqlExecuteError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class ApiTypeNotSupport(Exception):
    """[对于api的case中不支持的请求类型类型]

    Args:
        Exception ([type]): [description]
    """

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class ValidateError(Exception):
    """[验证测试用例失败]

    Args:
        Exception ([type]): [description]
    """

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class ActionNotSupport(Exception):
    """[不支持的Case action类型]

    Args:
        Exception ([type]): [description]
    """

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class CaseBodyNotSupport(Exception):
    """[不支持的case body check]

    Args:
        Exception ([type]): [description]
    """

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class OtherParserError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg
