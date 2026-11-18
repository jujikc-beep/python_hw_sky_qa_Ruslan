from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online")
    sleep(5)

    driver.find_element(
        By.XPATH, "//a[normalize-space()='HTML Form']").click()

    sleep(5)

    assert driver.current_url == "https://httpbin.qa-territory.online/forms/post"

    driver.back()

    sleep(5)

    assert driver.current_url == "https://httpbin.qa-territory.online/"

    driver.quit()
