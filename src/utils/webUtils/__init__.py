from .ActionValidate import (
    FindCssValidate,
    FindXpathValidate,
    ClickCssValidate,
    ClickXpathValidate,
    TakeScreenShot,
    InputCss,
    InputXpath,
    Sleep,
)


ACTION = {
    "find_css": FindCssValidate,
    "find_xpath": FindXpathValidate,
    "click_css": ClickCssValidate,
    "click_xpath": ClickXpathValidate,
    "takeshot": TakeScreenShot,
    "input_css": InputCss,
    "input_xpath": InputXpath,
    "sleep": Sleep,
    # "download_html":
}
