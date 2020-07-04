class CaseParserError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class CaseTypeNotFound(Exception):
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


class ElementNotFound(object):
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
