import time
import math
import pytest
from selenium import webdriver


# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     browser.implicitly_wait(20)
#     yield browser
#     print("\nquit browser..")
#     browser.quit()

@pytest.mark.parametrize('stepik_number', ["236895", "236896", "236897",
                                           "236898", "236899", "236903",
                                           "236904", "236905"])
def test_ufo_see(browser, stepik_number):
    browser.get(f"https://stepik.org/lesson/{stepik_number}/step/1")
    answer = math.log(int(time.time()) + 2.2)
    browser.find_element_by_tag_name("textarea").send_keys(str(answer))
    browser.find_element_by_xpath('//button[text()="Отправить"]').click()
    ans = browser.find_element_by_class_name("smart-hints__hint").text

    assert ans == 'Correct!', ans

