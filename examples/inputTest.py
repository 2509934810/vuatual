from selenium import webdriver

client = webdriver.Chrome()
client.get("http://www.baidu.com")
client.find_element_by_xpath('//*[@id="kw"]').send_keys("鸡蛋")
