import pytest


import click
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import pytest


@click.group()
@click.pass_context
def entrypoint(version):
    pass


@entrypoint.command(
    context_settings=dict(ignore_unknown_options=True, allow_extra_args=True)
)
@click.argument("cases", type=click.Path(exists=True))
@click.pass_context
def run(ctx, cases):
    """[run]
    """
    __run_test(cases, ctx.args)


@entrypoint.command()
def collect():
    """[collect]
    """
    click.echo("collect")


def __run_test(file, pytest_args):
    args = [file, "-v"]
    pytest_args += args
    pytest_args += ["-W", "ignore::UserWarning"]
    return pytest.main(args=pytest_args)
