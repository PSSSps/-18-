import requests
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import Fore, Style, init
from time import sleep

# تهيئة الألوان
init(autoreset=True)

print(Fore.CYAN + Style.BRIGHT + "\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print(Fore.YELLOW + Style.BRIGHT + "       TIKTOK VIDEO DELETE TOOL")
print(Fore.CYAN + Style.BRIGHT + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
print(Fore.MAGENTA + "• خطوات الاستخدام:")
print(Fore.GREEN + "• أدخل sessionid صالح للحساب.")
print("• سيتم حذف جميع فيديوهات الحساب تلقائيًا.")
print("• عدد الفيديوهات التي تم حذفها سيظهر مباشرة.\n")
print(Fore.YELLOW + "ملاحظة: sessionid يجب أن يكون صالح وغير منتهي.\n")

# --- إدخال sessionid ---
sessionid = input(Fore.CYAN + "• أدخل sessionid الخاص بالحساب: " + Fore.RESET).strip()


# --- دوال الأداة ---
def fetch_aweme_ids(sessionid):
    """جلب جميع معرفات الفيديوهات الخاصة بالحساب"""
    cookies = {
        '_ttp': '2vgirjOnuSrSOnprbKT4f6H0h4U',
        'tt_chain_token': 'aI+tyWRBH/hxDwK2jQqVFg==',
        'tt_csrf_token': 'NOQuiujw-sNPdBALP2za-QfH0lOCBDpI23-I',
        'sid_tt': sessionid,
        'sessionid': sessionid,
        'sessionid_ss': sessionid,
        'sid_guard': f'{sessionid}%7C1749233656%7C15551995%7CWed%2C+03-Dec-2025+18%3A14%3A11+GMT'
    }
    headers = {
        'origin': 'https://www.tiktok.com',
        'tt-csrf-token': 'NOQuiujw-sNPdBALP2za-QfH0lOCBDpI23-I',
        'user-agent': 'Mozilla/5.0 (X11; Linux aarch64)'
    }

    try:
        resp = requests.get(
            'https://api16-normal-c-alisg.tiktokv.com/lite/v2/public/item/list/?max_cursor=0&count=100&manifest_version_code=370402&_rticket=1749232712799&app_language=ar&app_type=normal&iid=7508467361403537168&app_package=com.zhiliaoapp.musically.go&channel=googleplay&device_type=RMO-NX1&language=ar&host_abi=arm64-v8a&locale=ar&resolution=1080*2316&openudid=cdb37c989aff6fff&update_version_code=370402&ac2=wifi&cdid=cb9b5af7-4256-45ab-a24d-e471a7f46569&sys_region=IQ&os_api=33&timezone_name=Asia%2FBaghdad&dpi=480&carrier_region=IQ&ac=wifi&device_id=7384884129483900421&os_version=13&timezone_offset=10800&version_code=370402&app_name=musically_go&ab_version=37.4.2&version_name=37.4.2&device_brand=HONOR&op_region=IQ&ssmix=a&device_platform=android&build_number=37.4.2&region=IQ&aid=1340&ts=1749232659',
            headers=headers, cookies=cookies
        )
        html = resp.text
    except Exception as e:
        print(Fore.RED + f"• خطأ في جلب قائمة الفيديوهات: {e}")
        return set()

    aweme_ids = sorted(set(re.findall(r'"aweme_id"\s*:\s*"(\d+)"', html)))
    return aweme_ids


def delete_aweme(sessionid, aweme_id):
    """حذف فيديو بواسطة المعرف"""
    cookies = {
        '_ttp': '2vgirjOnuSrSOnprbKT4f6H0h4U',
        'tt_chain_token': 'aI+tyWRBH/hxDwK2jQqVFg==',
        'tt_csrf_token': 'NOQuiujw-sNPdBALP2za-QfH0lOCBDpI23-I',
        'sid_tt': sessionid,
        'sessionid': sessionid,
        'sessionid_ss': sessionid,
        'sid_guard': f'{sessionid}%7C1749233656%7C15551995%7CWed%2C+03-Dec-2025+18%3A14%3A11+GMT'
    }
    headers = {
        'origin': 'https://www.tiktok.com',
        'tt-csrf-token': 'NOQuiujw-sNPdBALP2za-QfH0lOCBDpI23-I',
        'user-agent': 'Mozilla/5.0 (X11; Linux aarch64)'
    }

    url = f'https://www.tiktok.com/api/aweme/delete/?aweme_id={aweme_id}&aid=1988'
    try:
        resp = requests.post(url, headers=headers, cookies=cookies, timeout=20)
        return resp.status_code == 200
    except Exception as e:
        print(Fore.RED + f"• خطأ في حذف الفيديو {aweme_id}: {e}")
        return False


# --- بدء الحذف ---
print(Fore.CYAN + Style.BRIGHT + "\n• بدء حذف الفيديوهات ...\n")
deleted_count = 0

while True:
    aweme_ids = fetch_aweme_ids(sessionid)
    if not aweme_ids:
        print(Fore.GREEN + "• تم حذف جميع الفيديوهات أو لم يتم العثور على فيديوهات.\n")
        break

    with ThreadPoolExecutor(max_workers=30) as executor:
        futures = [executor.submit(delete_aweme, sessionid, aweme_id) for aweme_id in aweme_ids]
        for future in as_completed(futures):
            if future.result():
                deleted_count += 1
                print(Fore.BLUE + f"• Number of deleted videos → [ {deleted_count} ]", end="\r")
    sleep(1)

print(Fore.YELLOW + Style.BRIGHT + f"\n\n• انتهى الحذف. إجمالي الفيديوهات المحذوفة: {deleted_count}\n")