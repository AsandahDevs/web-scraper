#This script automates the searching of vehicles on the AutoTrader website
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# TODO: search_vw_gtis_that_have_mileage_less_than_100000_km # type: ignore

class AutoTrader(webdriver.Chrome):
    def open_autotrader_site(self):
        browser = webdriver.Chrome()
        browser.get('https://www.autotrader.co.za/')
        browser.fullscreen_window()
        browser.refresh()
        browser.implicitly_wait(15)
        browser.quit()

