# This file execustes our main python program
from automotive_scrapers.autotrader_scraper import AutoTrader

auto_trader_site = AutoTrader()
auto_trader_site.open_autotrader_site()