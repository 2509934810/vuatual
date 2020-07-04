from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def check_element_by_css_can_find(client, timeout, pollTime, cssSelector):
    return WebDriverWait(client, timeout).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, cssSelector))
    )


def check_element_by_xpath_can_find(client, timeout, pollTime, xPath):
    return WebDriverWait(client, timeout).until(
        EC.visibility_of_element_located((By.XPATH, xPath))
    )


def check_element_by_css_can_click(client, timeout, pollTime, cssSelector):
    return WebDriverWait(client, timeout).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, cssSelector))
    )


def check_element_by_xpath_can_click(client, timeout, pollTime, xPath):
    return WebDriverWait(client, timeout).until(
        EC.element_to_be_clickable((By.XPATH, xPath))
    )


def find_element_by_css(client, cssSelector):
    return client.find_element_by_css_selector(css_selector=cssSelector)


def find_element_by_xPath(client, xPath):
    return client.find_element_by_xpath(xpath=xPath)


def find_elements_by_css(client, cssSelector):
    return client.find_elements_by_css_selector(cssSelector)


def find_elements_by_xPath(client, xPath):
    return client.find_elements_by_xpath(xPath)
