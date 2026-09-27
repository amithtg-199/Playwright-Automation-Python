# conftest.py
import pytest


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
  return {
      **browser_context_args,
      "user_agent": (
          "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,"
          " like Gecko) Chrome/128.0.0.0 Safari/537.36"
      ),
      "viewport": {"width": 1920, "height": 1080},
  }


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
  return {
      **browser_type_launch_args,
      "args": ["--disable-blink-features=AutomationControlled"],
  }