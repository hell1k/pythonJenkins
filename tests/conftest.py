import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from selenium import webdriver


@pytest.fixture(scope="session")
def setup():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    # driver = webdriver.Chrome(executable_path="C:/Python310/chromedriver118.exe", options=options)
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

# def setup_browser():
#     options = webdriver.ChromeOptions()
#     options.add_argument("--no-sandbox")
#     options.add_argument("--disable-gpu")
#     # options.add_argument("--headless")
#     options.add_argument("--window-size=1920x1080")
#     options.add_argument("--disable-dev-shm-usage")
#     options.add_argument("--disable-notifications")
#     options.add_argument("--lang=en-US")
#     prefs = {"download.default_directory": f"{base_dir}/downloads"}
#     options.add_experimental_option("prefs", prefs)
#     driver = webdriver.Chrome(executable_path="C:/Python310/chromedriver.exe", options=options)
#     browser.set_driver(driver)
#     driver.maximize_window()
#     config.timeout = 10
#     BasePage.open_url(os.getenv("base_url"))
#     time.sleep(2)
#     #browser.find_element(By.XPATH, '//span[@class="btn btn-block btn-outline height40px"]').click() клик кнопки локали при запуске
#     return driver

# def pytest_exception_interact():
#     allure.attach(
#         name="Скринтшот",
#         body=browser.driver.get_screenshot_as_png(),
#         attachment_type=allure.attachment_type.PNG,
#     )
#     console_log = browser.driver.get_log("browser")
#     if not console_log:
#         pass
#     else:
#         try:
#             # attach a log file
#             allure.attach(json.dumps(console_log), name="Логи консоли", attachment_type=allure.attachment_type.JSON)
#         except:
#             pass
