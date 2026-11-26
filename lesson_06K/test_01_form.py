from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_01_form():
    driver = webdriver.Edge()
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name=first-name]")))

    first_name = driver.find_element(By.CSS_SELECTOR, "[name=first-name]")
    first_name.send_keys("Иван")

    last_name = driver.find_element(By.CSS_SELECTOR, "[name=last-name]")
    last_name.send_keys("Петров")

    address = driver.find_element(By.CSS_SELECTOR, "[name=address]")
    address.send_keys("Ленина, 55-3")

    e_mail = driver.find_element(By.CSS_SELECTOR, "[name=e-mail]")
    e_mail.send_keys("test@skypro.com")

    phone = driver.find_element(By.CSS_SELECTOR, "[name=phone]")
    phone.send_keys("+7985899998787")

    zip_code = driver.find_element(By.CSS_SELECTOR, "[name=zip-code]")
    zip_code.send_keys("")

    city = driver.find_element(By.CSS_SELECTOR, "[name=city]")
    city.send_keys("Москва")

    country = driver.find_element(By.CSS_SELECTOR, "[name=country]")
    country.send_keys("Россия")

    job_position = driver.find_element(By.CSS_SELECTOR, "[name=job-position]")
    job_position.send_keys("QA")

    company = driver.find_element(By.CSS_SELECTOR, "[name=company]")
    company.send_keys("SkyPro")

    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type = 'submit']")
    submit_button.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "zip-code"))
    )
    sleep(5)

    red_color = "rgba(248, 215, 218, 1)"
    zip_code_bg = driver.find_element(By.ID, "zip-code").value_of_css_property("background-color")
    assert zip_code_bg == red_color

    green_color = "rgba(209, 231, 221, 1)"
    green_fields = {
        "first-name": "First name",
        "last-name": "Last name",
        "address": "Address",
        "e-mail": "E-mail",
        "phone": "Phone number",
        "city": "City",
        "country": "Country",
        "job-position": "Job position",
        "company": "Company",
    }

    for field_id, field_label in green_fields.items():
        field_bg = driver.find_element(By.ID, field_id).value_of_css_property("background-color")
        assert field_bg == green_color

    driver.quit()
