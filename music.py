from gmusicapi import Mobileclient
from getpass import getpass

username = raw_input('Username:')
password = getpass()

api = Mobileclient()
api.login(username, password, Mobileclient.FROM_MAC_ADDRESS)

library = api.get_all_songs()

albumIdList = []

for i in library:
	if 'albumId' in i.keys():
		albumIdList.append(i['albumId'])

albumIdList = list(set(albumIdList))

albumDataList = []

for albumId in albumIdList:
	try:
		albumData = api.get_album_info(albumId,include_tracks=False)
		albumDataList.append(albumData)
	except:
		pass

print len(albumDataList)
