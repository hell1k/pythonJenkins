from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.locators import WebtablesPageLocators


class WebtablesPage(BasePage):
    webtable_locators = WebtablesPageLocators()

    def add_new_entry(self):
        name = "546456456546"
        self.click(self.webtable_locators.add_button)
        self.set_text(self.webtable_locators.first_name, name)
        self.set_text(self.webtable_locators.last_name, "122astname")
        self.set_text(self.webtable_locators.user_email, "343546@dom.com")
        self.set_text(self.webtable_locators.age, "23")
        self.set_text(self.webtable_locators.salary, "1000")
        self.set_text(self.webtable_locators.department, "AAAA")
        self.click(self.webtable_locators.submit_button)
        self.find_element(self.get_name(name))

    def get_name(self, name):
        return self.driver.find_element(By.XPATH, f"//div[@role='gridcell' and text()='{name}']")

    def search_entry(self):
        name = "Cierra"
        self.set_text(self.webtable_locators.search_field, name)
        self.find_element(self.get_name(name))

    def edit_entry(self):
        name = "CIERRAAA"
        self.click(self.webtable_locators.edit_button)
        self.find_element(self.webtable_locators.first_name).clear()
        self.set_text(self.webtable_locators.first_name, name)
        self.click(self.webtable_locators.submit_button)
        self.find_element(self.get_name(name))
        self.find_element(self.webtable_locators.search_field).clear()
        self.set_text(self.webtable_locators.search_field, name)
        self.find_element(self.get_name(name))
        self.click(self.webtable_locators.delete_button)
        self.find_element(self.webtable_locators.no_data_element)



