from Page.main_page import MainPage
from Page.login_page import LoginPage

sLink = "http://selenium1py.pythonanywhere.com/ru/"
loginLink = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, sLink)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, sLink)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, sLink)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_login_link(browser):
    page = LoginPage(browser, sLink)
    page.open()
    page.should_be_login_url()


def test_login_form(browser):
    page = LoginPage(browser, loginLink)
    page.open()

    page.should_be_login_form()


def test_reg_form(browser):
    page = LoginPage(browser, loginLink)
    page.open()
    page.should_be_register_form()
