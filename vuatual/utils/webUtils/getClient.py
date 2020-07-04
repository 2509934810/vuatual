from selenium.webdriver import Chrome, Firefox


def getClient(clientType, executePath="/usr/local/bin/chromedriver"):
    if clientType == "chrome":
        return Chrome(executable_path=executePath)
    elif clientType == "firefox":
        return Firefox(executable_path=executePath)
    else:
        return Chrome(executable_path=executePath)
