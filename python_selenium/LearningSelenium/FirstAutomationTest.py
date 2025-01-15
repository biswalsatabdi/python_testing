import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture
def setup_chrome():
    """Fixture to initialize Chrome WebDriver."""
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


@pytest.fixture
def setup_edge():
    """Fixture to initialize Edge WebDriver."""
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    yield driver
    driver.quit()


def test_open_in_chrome(setup_chrome):
    """Test to open a URL in Chrome."""
    url = "https://www.flipkart.com/"
    setup_chrome.get(url)
    print("Opened in Chrome")


def test_open_in_edge(setup_edge):
    """Test to open a URL in Edge."""
    url = "https://www.flipkart.com/"
    setup_edge.get(url)
    print("Opened in Edge")
