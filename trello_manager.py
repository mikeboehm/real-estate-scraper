# encoding: UTF-8

__author__ = 'mike'

from trello import TrelloApi, Boards, Members, Cards

from settings_manager import SettingsManager

settings_manager = SettingsManager()

settings = settings_manager.get_settings()

TRELLO_APP_KEY = settings['trello']['app_key']
TOKEN = settings['trello']['token']
USERNAME = settings['trello']['username']
BOARD_ID = settings['trello']['board_id']
LIST_ID = settings['trello']['list_id']

trello = TrelloApi(TRELLO_APP_KEY)


# List boards for member
# members = Members(TRELLO_APP_KEY, TOKEN)
# me = members.get(USERNAME)
#
# board_ids = me['idBoards']
# boards = Boards(TRELLO_APP_KEY, TOKEN)
# for board_id in board_ids:
#     # print BOARD_ID
#     board = boards.get(board_id)
#     print board['name'], board['id']

# List lists for board
# boards = Boards(TRELLO_APP_KEY, TOKEN)
# lists = boards.get_list(BOARD_ID)
# for list in lists:
#     print list['name'], list['id']

class TrelloManager(object):

    def __init__(self, settings_manager):
        all_settings = settings_manager.get_settings()

        self.TRELLO_APP_KEY = all_settings['trello']['app_key']
        self.TOKEN = all_settings['trello']['token']
        self.USERNAME = all_settings['trello']['username']
        self.BOARD_ID = all_settings['trello']['board_id']
        self.LIST_ID = all_settings['trello']['list_id']

        self.cards = Cards(self.TRELLO_APP_KEY, self.TOKEN)

    def upload_listings(self, listings):
        for listing in listings:
            self.upload_listing(listing)

    def upload_listing(self, listing):
        card = self.cards.new(listing.get_title(), self.LIST_ID, listing.get_description())

        # print card
        thumbnail = listing.get_thumbnail()
        if thumbnail:
            self.cards.new_attachment(card['id'], thumbnail, 'Thumbnail')