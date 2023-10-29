from selenium.webdriver.common.by import By


class PracticPageLocators:
    first_name = (By.ID, "firstName")
    last_name = (By.XPATH, '//input[@id="lastName"]')
    email = (By.XPATH, '//input[@id="userEmail"]')
    gender_male = (By.XPATH, '//label[text()="Male"]')
    mobile = (By.XPATH, '//input[@id="userNumber"]')
    hobbies_music = (By.XPATH, '//label[text()="Music"]')
    current_address = (By.XPATH, '//textarea[@id="currentAddress"]')
    submit_btn = (By.XPATH, '//button[@id="submit"] ')


class StudentPageLocators:
    student_name = (By.XPATH, '//td[text()="Student Name"]/following-sibling::td')
    student_email = (By.XPATH, '//td[text()="Student Email"]/following-sibling::td')
    student_gender = (By.XPATH, '//td[text()="Gender"]/following-sibling::td')
    student_mobile = (By.XPATH, '//td[text()="Mobile"]/following-sibling::td')
    student_hobbies = (By.XPATH, '//td[text()="Hobbies"]/following-sibling::td')
    student_address = (By.XPATH, '//td[text()="Address"]/following-sibling::td')


class WebtablesPageLocators:
    add_button = (By.ID, "addNewRecordButton")
    search_field = (By.ID, "searchBox")
    first_name = (By.ID, "firstName")
    last_name = (By.ID, 'lastName')
    user_email = (By.ID, "userEmail")
    age = (By.ID, "age")
    salary = (By.ID, "salary")
    department = (By.ID, "department")
    submit_button = (By.ID, "submit")
    check_entry = (By.XPATH, "//div[@role='gridcell' and text()='544t']")
    edit_button = (By.XPATH, '//span[@class="mr-2"]')
    delete_button = (By.XPATH, '//span[@id="delete-record-1"]')
    no_data_element = (By.XPATH, '//div[@class="rt-noData"]')
