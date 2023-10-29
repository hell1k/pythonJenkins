import time
from pages.practic_page import PracticPage, first_name, email
from pages.student_page import StudentPage
from pages.webtables_page import WebtablesPage


class TestWebTable:
    # вводим данные в полях и кликаем радиобаттоны
    def test_open(self, setup):
        page = WebtablesPage(setup)
        page.open_url("https://demoqa.com/webtables")
        page.add_new_entry()

    def test_search_cierra(self, setup):
        page = WebtablesPage(setup)
        page.open_url("https://demoqa.com/webtables")
        page.search_entry()
        page.edit_entry()


