from gmusicapi import Mobileclient

print 'Enter username' 
username = raw_input()

print 'Enter password' 
password = raw_input()

api = Mobileclient()
api.login(username, password, Mobileclient.FROM_MAC_ADDRESS)
