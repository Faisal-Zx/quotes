#!/usr/bin/python2-gerak"
# GW KEBELET BOKER AJG

import os,sys
import json
try:
	import requests
except ImportError:
	os.system('reset')
	rqs = raw_input('\033[1;91m[+] \033[1;92mPerlu install requests \033[1;97m(y/t): ')
	if rqs =="":
		print "\033[1;91m[!] Jangan kosong"
		os.sys.exit()
	elif rqs =="y":
		os.system('pip2 install requests')
		exit()
	elif rqs =="Y":
		os.system('pip2 install requests')
		exit()
	elif rqs =="t":
		os.sys.exit()
	elif rqs =="T":
		os.sys.exit()
	else:
		print "\033[1;91m[!]\033[1;92m Pilih\033[1;93m (y/n)"
		time.sleep(1)
		os.sys.exit()
from requests.exceptions import ConnectionError

logo ="""\033[1;97m
      ______ ______
    _/      Y      \_
   // ~~ ~~ | ~~ ~  \\\\
  // ~ ~ ~~ | ~~~ ~~ \\\           "Quotes"
 //________.|.________\\\       Created by \033[1;96mZeDD\033[1;97m
`----------`-'----------' \033[1;92m\033[4mhttps://github.com/rezadkim\033[0m"""

def quotes():
	try:
		os.system("reset")
		print logo
		print 53*"\033[1;91m_"
		print "\033[1;93mCTRL+C+Enter \033[1;91mexit"
		r = requests.get("http://quotes.stormconsultancy.co.uk/random.json")
		q = json.loads(r.text)
		print "\033[1;97m"
		msg = q["quote"]
		auth = q["author"]
		link = q["permalink"]
		print msg
		print "\n\033[1;97m-\033[1;96m"+auth
		print "\033[1;97mSource : \033[1;92m"+link
		raw_input("\n\033[1;91mEnter to next \033[1;97m>>")
		quotes()
	except KeyboardInterrupt:
		print"\n\033[1;91mKeluar"
		exit()
	except requests.exceptions.ConnectionError:
		print"\n\033[1;91mTidak ada koneksi"
		exit()
		
quotes()