# This script automates the searching of vehicles on the AutoTrader website
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class AutoTrader(webdriver.Chrome):

    def open_autotrader_site(self):
        browser = webdriver.Chrome()
        browser.get("https://www.autotrader.co.za/")
        browser.fullscreen_window()
        browser.refresh()
        browser.implicitly_wait(15)
        browser.quit()

    def view_gtis_from_year_2015_and_upwards(self):
        """
        this function will get vw golf gtis from the year 2015 and onwards
        """
        pass
