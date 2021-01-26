import math
import time
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)


x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)
input1 = browser.find_element_by_id("answer")
input1.send_keys(y)


option0 = browser.find_element_by_id('robotCheckbox')
option0.click()


option1 = browser.find_element_by_css_selector("[value='robots']")
option1.click()


option2 = browser.find_element_by_xpath("//button[text()='Submit']")
option2.click()

time.sleep(5)

browser.quit()




