from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome(executable_path='D:\\Coding\\PyLerning\\venv\\chromedriver\\chromedriver.exe')
        self.wd.implicitly_wait(5)
        # при конструированни драйвера передаем ссылку на фикстуру
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url()
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def __del__(self):
        # Деструктор
        self.wd.quit()
