import pytest

@pytest.fixture(scope="session")
def base_url():
    yield "https://testautomationpractice.blogspot.com/"