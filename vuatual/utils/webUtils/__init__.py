from .ActionValidate import (
    FindCssValidate,
    FindXpathValidate,
    ClickCssValidate,
    ClickXpathValidate,
    TakeScreenShot,
    InputCss,
    InputXpath,
    Sleep,
    DownloadHtml_c,
    DownloadHtml_x,
    DownBanner_css,
    DownBanner_xpath,
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
    "dwn_html_css": DownloadHtml_c,
    "dwn_html_xpath": DownloadHtml_x,
    "dwn_banner_css": DownBanner_css,
    "dwn_banner_xpath": DownBanner_xpath,
}
