# from selenium.webdriver.firefox.webdriver import WebDriver - заменяем
from selenium import webdriver

from fixture.contact import ContactHelper
from fixture.group import GroupHelper
from fixture.session import SessionHelper


class Application:

    def __init__(self, browser, base_url):
        # self.wd = WebDriver()
        if browser == 'firefox':
            self.wd = webdriver.Firefox()
        elif browser == 'chrome':
            self.wd = webdriver.Chrome()
        else:
            raise ValueError(f'Unrecognized browser {browser}')
        self.wd.implicitly_wait(3)  # в нашем случае это не лишнее
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        """Открыть форму авторизации приложения."""
        wd = self.wd
        # open home page
        # wd.get("http://localhost/addressbook/") - убрали в JSON
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()
