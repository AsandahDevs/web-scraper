# This script scrapes all liquor deals at Tops liquor stores (nation wide)
from selenium import webdriver
from selenium.webdriver.common.by import By

class Spar(webdriver.Chrome):
    def __init__(self):
        super().__init__()

    def open_spar_liquor_site(self):
        '''
        opens spar liquor site and views specials
        around Durban
        '''
        BROWSER_CLICK_EVENT = 'arguments[0].click();'

        self.get('https://www.topsatspar.co.za/Home#')
        self.implicitly_wait(30)
        verification_button = self.find_element(By.XPATH,value='//*[@id="AGModal"]/div/div/div/a[1]')
        self.execute_script(BROWSER_CLICK_EVENT, verification_button)
        self.implicitly_wait(30)
        specials_link = self.find_element(By.CSS_SELECTOR, "a.mega-menu[href='/Stores/Store-Finder?specials=1']")
        self.execute_script(BROWSER_CLICK_EVENT, specials_link)
        self.implicitly_wait(15)
        search_field = self.find_element(By.XPATH,value='//*[@id="searchTerm"]')
        self.execute_script(BROWSER_CLICK_EVENT, search_field)
        search_field.send_keys('toti')
        search_icon = self.find_element(By.XPATH,value='//*[@id="StoreFinderApp"]/div[2]/div[1]/div[1]/div[3]/a')
        self.execute_script(BROWSER_CLICK_EVENT, search_icon)
        self.implicitly_wait(30)
        toti_seadoone_area = self.find_element(By.XPATH,value='//*[@id="allStores"]/a[2]/div/div/a')
        self.execute_script(BROWSER_CLICK_EVENT, toti_seadoone_area)
        self.implicitly_wait(30)
        name_of_liquor_store = self.find_element(By.ID,value='storeName').text
        print(name_of_liquor_store)
        self.back()
        search_field = self.find_element(By.XPATH,value='//*[@id="searchTerm"]')
        self.execute_script(BROWSER_CLICK_EVENT, search_field)
        search_field.clear()
        search_field.send_keys('umlazi')
        search_icon = self.find_element(By.XPATH,value='//*[@id="StoreFinderApp"]/div[2]/div[1]/div[1]/div[3]/a')
        self.execute_script(BROWSER_CLICK_EVENT, search_icon)
        self.implicitly_wait(30)
        umlazi_mega_city = self.find_element(By.XPATH,value='//*[@id="allStores"]/a[1]/div/div/a')
        self.execute_script(BROWSER_CLICK_EVENT, umlazi_mega_city)
        self.implicitly_wait(30)
        name_of_liquor_store = self.find_element(By.ID,value='storeName').text
        print(name_of_liquor_store)
        self.close()