from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display
import time


class Pinterest(object):
    def __init__(self, username, password):
        super(Pinterest, self).__init__()
        display = Display(visible=0, size=(800, 600))
        display.start()
        self.base_url = "https://www.pinterest.com"
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.set_window_position(0, 0)
        self.driver.get(self.base_url + '/login/?referrer=home_page')
        self.driver.set_page_load_timeout(30)
        time.sleep(3)
        # Begin login process
        email_elem = self.driver.find_element_by_name('id')
        email_elem.send_keys(username)
        password_elem = self.driver.find_element_by_name('password')
        password_elem.send_keys(password)
        password_elem.send_keys(Keys.RETURN)
        print("Logging in...")
        time.sleep(5)
        self.search_bar = self.driver.find_element_by_name('q')

    def get_urls(self, list_of_keywords):
        list_of_urls = []
        for keyword in list_of_keywords:
            self.search_bar.send_keys(keyword)
            self.search_bar.send_keys(Keys.RETURN)
            list_of_urls.append(self.driver.current_url)
            self.search_bar.clear()
        return list_of_urls

    def finish(self):
        # Exit gracefully
        self.driver.close()
        self.driver.quit()
        print("Connection closed")
