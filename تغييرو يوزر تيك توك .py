import requests, SignerPy
from colorama import Fore, Style, init

# تهيئة الألوان
init(autoreset=True)

# ====================
# الطباعة الشاعرية للمتطلبات
# ====================
requirements = [
    "إدخال sessionid الخاص بحسابك",
    "إدخال اسم المستخدم الجديد الذي تريد تغييره",
    "الاتصال بالإنترنت",
    "تثبيت مكتبات requests و SignerPy"
]

print(Fore.MAGENTA + Style.BRIGHT + "━━━━━━━━PS━━━━━━━━━━━━")
print(Fore.CYAN + Style.BRIGHT + "📌 المتطلبات الأساسية:")
print(Fore.MAGENTA + Style.BRIGHT + "━━━━━━━━PS━━━━━━━━━━━━")
for req in requirements:
    print(Fore.YELLOW + Style.BRIGHT + "✔ " + req)
print(Fore.MAGENTA + Style.BRIGHT + "━━━━━━━━━━PS━━━━━━━━━━\n")

# ====================
# إدخال البيانات
# ====================
sessionid = input(Fore.GREEN + Style.BRIGHT + "أدخل sessionid : " + Style.RESET_ALL)
user = input(Fore.GREEN + Style.BRIGHT + "أدخل اسم المستخدم الجديد : " + Style.RESET_ALL)

print(Fore.BLUE + Style.BRIGHT + f"\n🔹 تم إدخال sessionid: {sessionid}")
print(Fore.BLUE + Style.BRIGHT + f"🔹 تم إدخال اسم المستخدم الجديد: {user}")
print(Fore.MAGENTA + Style.BRIGHT + "━━━━━━━━━━PS━━━━━━━━━━\n")

# ====================
# إعداد الطلب للـ TikTok API
# ====================
url = "https://api16-normal-c-alisg.tiktokv.com/passport/login_name/update/"
cookies = {"sessionid": sessionid}

params = {
    "request_tag_from": "h5",
    "manifest_version_code": "350302",
    "_rticket": "1765551860037",
    "app_language": "ar",
    "app_type": "normal",
    "iid": "7574913218801157889",
    "channel": "googleplay",
    "device_type": "Infinix X6837",
    "language": "ar",
    "host_abi": "arm64-v8a",
    "locale": "ar",
    "resolution": "1080*2232",
    "openudid": "d57c5e5d1a33fb48",
    "update_version_code": "350302",
    "ac2": "wifi",
    "cdid": "ef3eaabc-6061-4f41-bcbc-eab63b265dce",
    "sys_region": "EG",
    "os_api": "33",
    "timezone_name": "Asia/Baghdad",
    "dpi": "480",
    "carrier_region": "IQ",
    "ac": "wifi",
    "device_id": "7427048691142395393",
    "os_version": "12",
    "timezone_offset": "10800",
    "version_code": "350302",
    "app_name": "musically_go",
    "ab_version": "35.3.2",
    "version_name": "35.3.2",
    "device_brand": "Infinix",
    "op_region": "IQ",
    "ssmix": "a",
    "device_platform": "android",
    "build_number": "35.3.2",
    "region": "EG",
    "aid": "1340",
    "ts": "1765551750",
    "okhttp_version": "4.1.103.57-ul",
    "use_store_region_cookie": "1",
    "app_version": "37.8.5"
}

payload = {
  'page_from': 'profile_edit',
  'login_name': user,
}

# توقيع البيانات
m = SignerPy.sign(params=params, cookie=cookies, payload=payload)

headers = {
  'Host': "api16-normal-c-alisg.tiktokv.com",
  'rpc-persist-pyxis-policy-v-tnc': "1",
  'x-ss-stub': m['x-ss-stub'],
  'x-tt-req-timeout': "90000",
  'accept-encoding': "gzip",
  'sdk-version': "2",
  'passport-sdk-version': "30990",
  'x-tt-ultra-lite': "1",
  'x-vc-bdturing-sdk-version': "2.3.2.i18n",
  'user-agent': "com.zhiliaoapp.musically.go/350302 (Linux; U; Android 13; ar_EG; Infinix X6837; Build/TP1A.220624.014;tt-ok/3.12.13.21-ul)",
  'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
  'x-ladon': m['x-ladon'],
  'x-khronos': m['x-khronos'],
  'x-argus': m['x-argus'],
  'x-gorgon': m['x-gorgon'],
  'Cookie': f"sessionid={sessionid}"
}

# ====================
# إرسال الطلب و طباعة الاستجابة بشكل شاعرية
# ====================
response = requests.post(url, data=payload, headers=headers, params=params)

print(Fore.MAGENTA + Style.BRIGHT + "\n━━━━━━━━━PS━━━━━━━━━━━")
print(Fore.CYAN + Style.BRIGHT + "📬 استجابة الخادم:")
print(Fore.MAGENTA + Style.BRIGHT + "━━━━━━━━━━━PS━━━━━━━━━")

try:
    resp_json = response.json()
    for key, value in resp_json.items():
        print(Fore.YELLOW + Style.BRIGHT + f"{key} : {value}")
except:
    # إذا لم يكن JSON
    print(Fore.RED + Style.BRIGHT + response.text)

print(Fore.MAGENTA + Style.BRIGHT + "━━━━━━━━━PS━━━━━━━━━━━\n")
print(Fore.GREEN + Style.BRIGHT + "✅ تم التنفيذ بنجاح (أو عرض الخطأ إذا حصل)!")