import os, time
from selenium import webdriver

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'text.txt')
try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    input1 = browser.find_element_by_xpath("//input[@placeholder='Enter first name']")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath("//input[@placeholder='Enter last name']")
    input2.send_keys("Ivanov")
    input3 = browser.find_element_by_xpath("//input[@placeholder='Enter email']")
    input3.send_keys("lol@mail.ru")

    file = browser.find_element_by_id("file")
    file.send_keys(file_path)

    option2 = browser.find_element_by_xpath("//button[text()='Submit']")
    option2.click()


finally:
    time.sleep(5)

    browser.quit()
