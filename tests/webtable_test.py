import time

import pytest

from pages.webtables_page import WebtablesPage


class TestWebTable:
    # вводим данные в полях и кликаем радиобаттоны
    @pytest.mark.test1
    def test_open(self, setup):
        page = WebtablesPage(setup)
        page.open_url("https://demoqa.com/webtables")
        page.add_new_entry()

    @pytest.mark.test1
    def test_search_cierra(self, setup):
        page = WebtablesPage(setup)
        page.open_url("https://demoqa.com/webtables")
        page.search_entry()
        page.edit_entry()


