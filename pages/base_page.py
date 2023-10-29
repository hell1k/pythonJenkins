from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator))

    def click(self, locator):
        self.find_element(locator).click()

    def set_text(self, locator, text):
        self.find_element(locator).send_keys(text)

    def wait_invisibility(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.invisibility_of_element(locator))

    def return_text(self, locator):
        self.find_element(locator).text()
