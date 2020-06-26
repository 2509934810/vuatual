from .ActionValidate import (
    FindCssValidate,
    FindXpathValidate,
    ClickCssValidate,
    ClickXpathValidate,
    TakeScreenShot,
)


ACTION = {
    "find_css": FindCssValidate,
    "find_xpath": FindXpathValidate,
    "click_css": ClickCssValidate,
    "click_xpath": ClickXpathValidate,
    "takeshot": TakeScreenShot,
}
