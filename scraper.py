from bs4 import BeautifulSoup
import requests

from listing import Listing
from trello_manager import TrelloManager
from settings_manager import SettingsManager

html = requests.get('http://www.nelsonssales.com/search/index/expensive/false/search_sale_or_rent/2/search_max_price_rent/2/search_location/1')

soup = BeautifulSoup(html.text)

items = soup.find_all("div", class_="item")

listings = []
for item in items:

    title = item.find_all("h3", class_="property-title")[0].text
    bedrooms = item.find_all("span", class_="bedrooms")[0].text
    price = item.find_all("span", class_="price")[0].text
    link = item.find_all('a')[0].get('href')
    thumbnail = item.find_all('img')[0].get('src')

    listing = Listing(title, price, bedrooms, link, thumbnail)
    listings.append(listing)
    # print title, price, bedrooms, link, thumbnail

if listings:
    settings_manager = SettingsManager()
    trello = TrelloManager(settings_manager)
    trello.upload_listings(listings)

