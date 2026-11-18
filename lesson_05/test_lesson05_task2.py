from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")

    name_field = driver.find_element(By.NAME, "custname")
    name_field.send_keys("Руслан Каримов")

    sleep(3)

    submit_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Submit']")
    submit_btn.click()

    sleep(3)

    assert driver.current_url == "https://httpbin.qa-territory.online/forms/post"

    driver.quit()
