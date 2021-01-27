import time, math
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    going = browser.find_element_by_tag_name("button")
    going.click()

    new_windows = browser.window_handles[1]
    browser.switch_to.window(new_windows)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    option2 = browser.find_element_by_xpath("//button[text()='Submit']")
    option2.click()


finally:
    time.sleep(5)

    browser.quit()
