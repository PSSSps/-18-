import requests
import time, json, os
from urllib.parse import urlencode
from MedoSigner import Argus, Gorgon, md5, Ladon
from colorama import Fore, Style, init
init(autoreset=True)

# شعار الأداة - بنفسجي غامق Bold
logo = f"""
{Fore.MAGENTA}{Style.BRIGHT}
╭━━━┳━━━╮
┃╭━╮┃╭━╮┃
┃╰━╯┃╰━━╮
┃╭━━┻━━╮┃
┃┃╱╱┃╰━╯┃
╰╯╱╱╰━━━╯
 𝟑𝟏𝟑 𝑷𝑺 
{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}                       PS TOOL
{Fore.YELLOW}{Style.BRIGHT}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

print(logo)

# دالة التوقيع
def sign_tiktok(params, payload: str = None, cookie: str = None):
    unix = int(time.time())
    payload_str = ""
    if payload:
        if isinstance(payload, dict):
            payload_str = urlencode(payload)
        else:
            payload_str = str(payload)
    x_ss_stub = md5(payload_str.encode('utf-8')).hexdigest().upper() if payload_str else None
    signatures = Gorgon(params, unix, payload_str, cookie).get_value()
    signatures["x-ladon"] = Ladon.encrypt(unix, 1611921764, 1340)
    signatures["x-argus"] = Argus.get_sign(
        params,
        x_ss_stub,
        unix,
        platform=19,
        aid=1340,
        license_id=1611921764,
        sec_device_id="",
        sdk_version="2.3.1.i18n",
        sdk_version_int=2
    )
    if x_ss_stub:
        signatures["x-ss-stub"] = x_ss_stub
    return signatures

# اختيار العملية
print(f"{Fore.MAGENTA}{Style.BRIGHT}[ 1 ]{Fore.LIGHTMAGENTA_EX} - تغيير بايو الحساب 🔑")
print(f"{Fore.MAGENTA}{Style.BRIGHT}[ 2 ]{Fore.LIGHTRED_EX} - حذف الحساب 😈")
choice = input(f"{Fore.MAGENTA}{Style.BRIGHT}[#] {Fore.YELLOW}اختر رقم العملية: ").strip()

if choice == "1":
    bio = input(f"{Fore.LIGHTMAGENTA_EX}- اكتب البايو الجديد: {Fore.CYAN}").strip()
elif choice == "2":
    bio = "i,m 5"
else:
    print(Fore.RED + "❌ اختيار غير صحيح. الخروج...")
    exit()

# اختيار السيشنات
print(f"\n{Fore.YELLOW}{Style.BRIGHT}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print(f"{Fore.MAGENTA}{Style.BRIGHT}• طريقة معالجة السيشنات:")
print(f"{Fore.CYAN}{Style.BRIGHT}1) سيشن واحد")
print(f"{Fore.GREEN}{Style.BRIGHT}2) عدة سيشنات (كتابة مباشرة)")
print(f"{Fore.BLUE}{Style.BRIGHT}3) ملف يحتوي على السيشنات (واحد لكل سطر)")
print(f"{Fore.YELLOW}{Style.BRIGHT}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")

session_choice = input(f"{Fore.MAGENTA}{Style.BRIGHT}[#] {Fore.YELLOW}اختر خيار السيشن: ").strip()
sessions = []

if session_choice == "1":
    s = input(f"{Fore.CYAN}- أدخل السيشن: {Fore.GREEN}").strip()
    sessions.append(s)

elif session_choice == "2":
    raw = input(f"{Fore.CYAN}- أدخل السيشنات مفصولة بفواصل: {Fore.GREEN}").strip()
    sessions = [x.strip() for x in raw.split(",") if x.strip()]

elif session_choice == "3":
    filename = input(f"{Fore.CYAN}- أدخل المسار الكامل للملف: {Fore.GREEN}").strip()
    if not os.path.isfile(filename):
        print(Fore.RED + "❌ الملف غير موجود أو المسار غير صحيح!")
        exit()
    with open(filename, "r", encoding="utf-8") as f:
        sessions = [line.strip() for line in f if line.strip()]

else:
    print(Fore.RED + "❌ اختيار غير صالح. الخروج من الأداة...")
    exit()

# تنفيذ العملية لكل سيشن
for sessionid in sessions:
    payload = {'signature': bio}
    cookies = f'sessionid={sessionid}'
    params_str = urlencode({
        "device_platform": "android",
        "aid": "1340",
        "version_code": "350302",
        "version_name": "35.3.2",
        "device_id": "7427048691142395393"
    })
    hs = sign_tiktok(params=params_str, payload=payload, cookie=cookies)
    headers = {
        'Host': "api16-normal-c-alisg.tiktokv.com",
        'rpc-persist-pyxis-policy-v-tnc': "1",
        'x-ss-stub': hs['x-ss-stub'],
        'x-tt-req-timeout': "90000",
        'accept-encoding': "gzip",
        'sdk-version': "2",
        'passport-sdk-version': "30990",
        'x-tt-ultra-lite': "1",
        'x-vc-bdturing-sdk-version': "2.3.2.i18n",
        'x-tt-store-region': "iq",
        'x-tt-store-region-src': "uid",
        'user-agent': "com.zhiliaoapp.musically.go/350302 (Linux; U; Android 12; ar_EG; Infinix X6837; Build/TP1A.220624.014;tt-ok/3.12.13.21-ul)",
        'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
        'content-length': str(len(urlencode(payload))),
        'x-ladon': hs['x-ladon'],
        'x-khronos': hs['x-khronos'],
        'x-argus': hs['x-argus'],
        'x-gorgon': hs['x-gorgon'],
        'cookie': cookies,
    }
    url = f"https://api16-normal-c-alisg.tiktokv.com/aweme/v1/commit/user/?request_tag_from=h5&manifest_version_code=350302&_rticket={int(time.time()*1000)}"
    try:
        response = requests.post(url, data=payload, headers=headers, timeout=20)
        extra = response.json()
        user = extra.get('user', {}).get('nickname', 'N/A')
        if 'signature' in response.text:
            print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + f"✔ العملية تمت بنجاح للمستخدم: {user}")
        else:
            print(Fore.LIGHTRED_EX + Style.BRIGHT + f"❌ فشل العملية للمستخدم: {user}")
    except Exception as e:
        print(Fore.RED + Style.BRIGHT + f"❌ خطأ في السيشن: {sessionid} | {e}")

print(Fore.YELLOW + Style.BRIGHT + "\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print(Fore.MAGENTA + Style.BRIGHT + "تم إنهاء جميع العمليات | PS TOOL")