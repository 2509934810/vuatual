from selenium.webdriver import Chrome


def Auth(client, authConfig):
    """[base auth]

    Args:
        client ([type]): [description]
        authConfig ([type]): [description]
    """
    client = Chrome()
    authKeys = authConfig.keys()
    _checkAuth(authConfig)
    for authKey in authKeys:
        if authKey.startswith("account"):
            accountInfo = authConfig.get("accountInfo")
    # to add client click input


def _checkAuth(authConfig):
    """[summary]

    Args:
        authConfig ([type]): [description]
    check authConfig
    checkType cssSelector
              Xpath
    """
    authKeys = _getAllKeys(authConfig)
    assert "accountInfo" in authKeys
    assert "passwordInfo" in authKeys
    if not "password_xpath" in authKeys and not "password_seclector" in authKeys:
        raise KeyError("{}".format("password_format"))
    if not "account_xpath" in authKeys and not "account_seclector" in authKeys:
        raise KeyError("{}".format("account_format"))
    if not "submit_xpath" in authKeys and not "submit_seclector" in authKeys:
        raise KeyError("{}".format("submit_format"))


def _getAllKeys(authConfig):
    keys = []
    if isinstance(authConfig, str):
        return None
    if isinstance(authConfig, dict):
        values = []
        for key, value in authConfig.items():
            keys.append(key)
            if not value is None:
                values.append(value)
        keys.extend(_getAllKeys(values))
        return keys
    if isinstance(authConfig, list):
        for auth in authConfig:
            if not auth is None:
                if not _getAllKeys(auth) is None:
                    keys.extend(_getAllKeys(auth))
        return keys


if __name__ == "__main__":
    keys = {
        "key1": ["1", "2", "3"],
        "key2": [{"key3": "4", "key4": "5", "key5": {"key6": "6"}}],
    }
    print(_getAllKeys(keys))
