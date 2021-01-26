from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time

def summa(x, y):
    s = int(x)
    l = int(y)
    return str(s + l)

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

sum1 = browser.find_element_by_id("num1")
x = sum1.text
sum2 = browser.find_element_by_id("num2")
y = sum2.text
z = summa(x, y)

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(z)

push = browser.find_element_by_xpath("//button[text()='Submit']")
push.click()
time.sleep(5)

browser.quit()
