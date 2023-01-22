from selenium.webdriver.firefox.webdriver import WebDriver

from fixture.contact import ContactHelper
from fixture.group import GroupHelper
from fixture.session import SessionHelper


class Application:
    def __init__(self):
        # self.wd = webdriver.Firefox()
        # self.wd.implicitly_wait(100)
        self.wd = WebDriver()
        # self.wd.implicitly_wait(5)  # в нашем случае это лишнее
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

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
        wd.get('http://localhost/addressbook/')

    def destroy(self):
        self.wd.quit()
