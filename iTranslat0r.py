#!/usr/bin/python
# -*- coding: utf-8 -*-
from requests_oauthlib import OAuth1 # https://github.com/requests/requests-oauthlib
import requests,platform,os
###############################################################################
# Keys: https://gist.github.com/shobotch/5160017
# APIs: https://seriot.ch/resources/abusing_twitter_api/twitter_api.pdf
###############################################################################
# I Love Lambda <3
login = lambda u,p: requests.post("https://api.twitter.com/auth/1/xauth_password.json",data={'x_auth_identifier':u,'x_auth_password':p},headers={'Authorization':'Bearer AAAAAAAAAAAAAAAAAAAAAFXzAwAAAAAAMHCxpeSDG1gLNLghVe8d74hl6k4%3DRUMF4xAQLsbeBhTSRrCiQpJtxoGWeyHrDb5te2jpGskWDFW82F','X-Guest-Token':requests.post("https://api.twitter.com/1.1/guest/activate.json",headers={"Authorization":"Bearer AAAAAAAAAAAAAAAAAAAAAFXzAwAAAAAAMHCxpeSDG1gLNLghVe8d74hl6k4%3DRUMF4xAQLsbeBhTSRrCiQpJtxoGWeyHrDb5te2jpGskWDFW82F"}).json()['guest_token']})
translate = lambda i,l,t,s: requests.get('https://api.twitter.com/1.1/translations/show.json?id='+str(i)+'&dest='+l,auth=OAuth1('3nVuSoBZnx6U4vzUxf5w','Bcs59EFbbsdF6Sl9Ng71smgStWEGwXXKSjYvPVt7qys',t,s,decoding=None)).json()
tweets = lambda us,t,s: requests.get('https://api.twitter.com/2/timeline/profile/'+requests.get('https://help.twitter.com/api/v1/username_lookups?username='+us).json()['user_id']+'.json?count=32767',auth=OAuth1('3nVuSoBZnx6U4vzUxf5w','Bcs59EFbbsdF6Sl9Ng71smgStWEGwXXKSjYvPVt7qys',t,s,decoding=None)).json()['globalObjects']['tweets']
ask = lambda m: raw_input(m) if platform.python_version().split(".")[0]=="2" else str(input(m))
###############################################################################
if __name__ == '__main__':
	os.system('cls||clear')
	print("+----------------------------------------------+\n|       CoDeD By 1337r00t (@0x1337r00t)        |\n|             Blackfox's Group ©               |\n|----------------------------------------------|\n|             iTranslat0r © 2019               |\n+----------------------------------------------+\n")
	loq = login(ask("Your Username => "),ask("Your Password => "))
	if loq.status_code != 200:
		print("Username/Password is incorrect or 2FA ur account is Enabled")
		exit()
	print("Logged")
	X_Token,X_Secret = loq.json()['oauth_token'],loq.json()['oauth_token_secret']
	user = ask("[Target] Username ==> ")
	lang = ask("Select the language short-lang you want to translate [ex: English, enter (en)]==> ")
	for id_tweet in tweets(user,X_Token,X_Secret):
		try: print(translate(id_tweet,lang,X_Token,X_Secret)['text'].encode("utf-8"))
		except: print("")
