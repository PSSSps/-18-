import requests, SignerPy
from colorama import Fore, Style, init

# تهيئة الألوان
init(autoreset=True)

# ====================
# شاشة شرح الأداة عند التشغيل
# ====================
print(Fore.MAGENTA + Style.BRIGHT + "━━━━━━━━━━━━━━━━━━━━")
print(Fore.CYAN + Style.BRIGHT + "📘 شرح تشغيل أداة حظر تيك توك")
print(Fore.MAGENTA + Style.BRIGHT + "━━━━━━━━━━━━━━━━━━━━")

print(Fore.YELLOW + Style.BRIGHT + """
1️⃣ أدخل اسم المستخدم (username) للحساب الذي تريد حظره.
2️⃣ الأداة ستتحقق إذا كان الحساب موجودًا أم لا.
3️⃣ سيتم استخراج معلومات الحساب: id و sec_user_id تلقائيًا.
4️⃣ بعد ذلك، سيُطلب منك إدخال sessionid صالح.
5️⃣ الأداة سترسل طلب الحظر إلى TikTok.
6️⃣ ستظهر لك نتيجة الحظر أو سبب الخطأ بطريقة واضحة.
""")

print(Fore.MAGENTA + Style.BRIGHT + "━━━━━━━━━━━━━━━━━━━━")
print(Fore.GREEN + Style.BRIGHT + "▶️ يمكنك الآن البدء باستخدام الأداة\n")

# ====================
# إدخال اسم المستخدم والتحقق
# ====================
username = input(Fore.GREEN + Style.BRIGHT + " - أدخل username : " + Style.RESET_ALL)
url_user = f'https://www.tiktok.com/@{username}'

headers_user = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'Accept-Language': 'ar-EG,ar;q=0.9,en;q=0.8'
}

response = requests.get(url_user, headers=headers_user)

print(Fore.MAGENTA + Style.BRIGHT + "\n━━━━━━━━━━━━━━━━━━━━")
if '"userInfo":{' not in response.text:
    print(Fore.RED + Style.BRIGHT + "❌ ما يوجد حساب بهذا اليوزر أو الحساب محمي")
    exit()
else:
    print(Fore.CYAN + Style.BRIGHT + "✅ تم العثور على الحساب بنجاح")
print(Fore.MAGENTA + Style.BRIGHT + "━━━━━━━━━━━━━━━━━━━━\n")

# ====================
# استخراج معلومات الحساب
# ====================
user_info = response.text.split('"userInfo":{')[1].split(',"challengeStatus"')[0]
try:
    id = user_info.split('"id":"')[1].split('"')[0]
    use = user_info.split('"uniqueId":"')[1].split('"')[0]
    sec_user_id = None
    if '"secUid":"' in user_info:
        sec_user_id = user_info.split('"secUid":"')[1].split('"')[0]

    print(Fore.YELLOW + Style.BRIGHT + f"🔹 id : {id}")
    print(Fore.YELLOW + Style.BRIGHT + f"🔹 user : {use}")
    if sec_user_id:
        print(Fore.YELLOW + Style.BRIGHT + f"🔹 sec_user_id : {sec_user_id}")
    else:
        print(Fore.RED + Style.BRIGHT + "⚠ sec_user_id غير موجود، قد لا يعمل الحظر")
except:
    print(Fore.RED + Style.BRIGHT + "❌ خطأ أثناء استخراج معلومات الحساب")
    exit()

# ====================
# إدخال sessionid
# ====================
sessionid = input(Fore.GREEN + Style.BRIGHT + "\nأدخل sessionid : " + Style.RESET_ALL)

# ====================
# إعداد طلب الحظر
# ====================
url_block = "https://api16-normal-c-alisg.tiktokv.com/lite/v2/relation/block/"
cookies = {  
  "install_id": "7574913218801157889",
  "ttreq": "1$dummy",
  "sessionid": sessionid,
}
params = {
    "lite_flow_schedule": "new",
    "user_id": id,
    "sec_user_id": sec_user_id,
    "block_type": "1",
    "source": "0",
    "manifest_version_code": "350302",
    "_rticket": "1766175391771",
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
    "ts": "1766175186",
    "app_version": "37.8.5"
}
payload = {'body': 'null'}

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
  'x-tt-store-region': "iq",
  'x-tt-store-region-src': "uid",
  'user-agent': "com.zhiliaoapp.musically.go/350302 (Linux; U; Android 13; ar_EG; Infinix X6837; Build/TP1A.220624.014;tt-ok/3.12.13.21-ul)",
  'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
  'x-ladon': m['x-ladon'],
  'x-khronos': m['x-khronos'],
  'x-argus': m['x-argus'],
  'x-gorgon': m['x-gorgon'],
  'Cookie': f"sessionid={sessionid}"
}

# ====================
# إرسال طلب الحظر وطباعة الاستجابة بشكل شاعرية
# ====================
response = requests.post(url_block, data=payload, headers=headers, params=params)

print(Fore.MAGENTA + Style.BRIGHT + "\n━━━━━━━━━━━━━━━━━━━━")
print(Fore.CYAN + Style.BRIGHT + "📬 استجابة الحظر:")
print(Fore.MAGENTA + Style.BRIGHT + "━━━━━━━━━━━━━━━━━━━━")

try:
    resp_json = response.json()
    for key, value in resp_json.items():
        print(Fore.YELLOW + Style.BRIGHT + f"{key} : {value}")
except:
    print(Fore.RED + Style.BRIGHT + response.text)

print(Fore.MAGENTA + Style.BRIGHT + "━━━━━━━━━━━━━━━━━━━━")
print(Fore.GREEN + Style.BRIGHT + "✅ انتهى تنفيذ الحظر (أو عرض الخطأ إذا حصل)!")