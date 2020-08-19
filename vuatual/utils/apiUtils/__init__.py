from .ActionValidate import (
    SaveTitle,
    CheckStatusCode,
    CheckJsonBody
)

ACTION = {"get_title": SaveTitle,
          "check_statusCode": CheckStatusCode,
          "check_json_body": CheckJsonBody}
