from selenium import webdriver
import math
import time
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

button = browser.find_element_by_xpath("//button[text()='Submit']")



input1 = browser.find_element_by_id("answer")
input1.send_keys(y)

option0 = browser.find_element_by_id('robotCheckbox')
option0.click()
browser.execute_script("return arguments[0].scrollIntoView(true);", button)

option1 = browser.find_element_by_css_selector("[value='robots']")
option1.click()



button.click()

time.sleep(5)

browser.quit()