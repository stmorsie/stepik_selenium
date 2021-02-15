import time
import math
import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('stepik_number', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_ufo_see(browser, stepik_number):
    link = f"https://stepik.org/lesson/{stepik_number}/step/1"
    browser.get(link)
    browser.implicitly_wait(5)
    answer = math.log(int(time.time()) + 2.2)
    inpunt_1 = browser.find_element_by_tag_name("textarea")
    x = str(answer)
    inpunt_1.send_keys(x)
    button = browser.find_element_by_xpath('//button[text()="Отправить"]')
    button.click()
    browser.implicitly_wait(5)
    ans = browser.find_element_by_class_name("smart-hints__hint")
    get_ans = ans.text
    assert get_ans == 'Correct!', get_ans

