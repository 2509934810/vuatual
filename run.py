import click
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import pytest

@click.command()
@click.option("--count", default=1, help="Number of greetings")
@click.option("--name", prompt="Your name", help="the person to greet")
def hello(count, name):
    client = webdriver.Chrome()
    client.get("http://www.baidu.com")
    WebDriverWait(client, 10, 0.5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#su")))
    for _ in range(count):
        click.echo(f"hello {name}")
    pytest.main()

hello()


