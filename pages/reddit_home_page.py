from selenium.webdriver.common.by import By
from .base_page import BasePage

class RedditHomePage(BasePage):
    # Elementlərin locator-ları
    SEARCH_INPUT = (By.NAME, "q")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def search_for(self, query):
        self.enter_text(self.SEARCH_INPUT, query)
        self.find_element(self.SEARCH_INPUT).submit()
