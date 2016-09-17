from gmusicapi import Mobileclient
from getpass import getpass

username = raw_input('Username:')
password = getpass()

api = Mobileclient()
api.login(username, password, Mobileclient.FROM_MAC_ADDRESS)

library = api.get_all_songs()

albumIds = []

for i in library:
	if 'albumId' in i.keys():
		albumIds.append(i['albumId'])

albumIds = list(set(albumIds))
