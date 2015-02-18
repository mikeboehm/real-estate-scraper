__author__ = 'mike'
import md5

class Listing(object):
    title = None
    price = 0
    bedrooms = 0
    link = None
    thumbnail = None

    def __init__(self, title=None, price=None, bedrooms=None, link=None, thumbnail = None):
        self.title = title
        self.price = price
        self.bedrooms = bedrooms
        self.link = link
        self.thumbnail = thumbnail

    def get_title(self):
        return self.title + ' - ' + self.price

    def get_description(self):
        return hash(self.link)

    def get_thumbnail(self):
        return self.thumbnail