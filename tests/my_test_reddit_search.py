import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.reddit_home_page import RedditHomePage

@pytest.fixture
def driver():
    """
    Test başlamazdan əvvəl brauzeri hazırlayır,
    test bitdikdən sonra isə bağlayır.
    """
    # Chrome drayverini avtomatik quraşdırır və işə salır
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    driver.maximize_window()
    driver.implicitly_wait(10) # Elementlərin yüklənməsi üçün gözləmə müddəti
    
    yield driver
    
    driver.quit()

def test_reddit_search_functionality(driver):
    """
    Reddit ana səhifəsində axtarış funksiyasının 
    düzgün işlədiyini yoxlayan test ssenarisi.
    """
    # 1. Ana səhifə obyektini yaradırıq
    home_page = RedditHomePage(driver)
    
    # 2. Sayta daxil oluruq
    driver.get("https://www.reddit.com")
    
    # 3. Axtarış sözünü daxil edirik (Page Object Model metodundan istifadə edərək)
    search_query = "Python Automation"
    home_page.search_for(search_query)
    
    # 4. Yoxlama (Assertion): Axtarış nəticəsinin başlığında sözün olduğunu yoxlayırıq
    assert search_query in driver.title, f"Gözlənilən '{search_query}' başlığı tapılmadı!"
