class SessionHelper:
    """Вспомогательный класс логин и логаут."""

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        """Авторизация в приложении."""
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath('//input[@value="Login"]').click()

    def _is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text('Logout')) > 0

    def _is_logged_in_as(self, username):
        wd = self.app.wd
        return (wd.find_element_by_xpath("//div/div[1]/form/b").text
                == "("+username+")")

    def logaut_website(self):
        """Выход из приложения."""
        wd = self.app.wd
        wd.find_element_by_link_text('Logout').click()
        wd.find_element_by_name("user")

    def ensure_logaut(self):
        """Выход из приложения с проверкой."""
        wd = self.app.wd
        if self._is_logged_in():
            self.logaut_website()

    def ensure_login(self, username, password):
        """Авторизация в приложении с проверкой."""
        wd = self.app.wd
        if self._is_logged_in():
            if self._is_logged_in_as(username):
                return
            else:
                self.logaut_website()
        self.login(username, password)
