from Page.main_page import MainPage

sLink = "https://www.airlines-inform.ru/about_airline/pobeda/"


def test_yes(browser):
    page = MainPage(browser, sLink)
    page.open()
    page.yes_click()
