import requests
import datetime
from colorama import Fore, Style, init

# تهيئة الألوان
init(autoreset=True)

# دالة تحويل التوقيت
def conv(ts):
    return datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

# دالة الحصول على معلومات الحساب
def generalinfo(session):
    url = "https://www.tiktok.com/passport/web/account/info/"
    headers = {
        "accept": "*/*",
        "cookie": f"sessionid={session}",
        "user-agent": "Mozilla/5.0"
    }
    r = requests.get(url, headers=headers)
    return r.json()

# دالة الحصول على الرصيد والعملات
def balance(session):
    url = "https://webcast.tiktok.com/webcast/wallet_api/fs/diamond_buy/permission_v2"
    params = {"aid": "1988"}
    headers = {
        "Cookie": f"sessionid={session}",
        "User-Agent": "Mozilla/5.0"
    }
    return requests.get(url, headers=headers, params=params)

# عرض الشرح عند تشغيل الأداة
def show_intro():
    print(Fore.CYAN + Style.BRIGHT + "\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(Fore.YELLOW + Style.BRIGHT + "           TIKTOK INFO TOOL")
    print(Fore.CYAN + Style.BRIGHT + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
    print(Fore.MAGENTA + "خطوات الاستخدام:\n")
    print(Fore.GREEN + "• أدخل sessionid صالح للحساب.")
    print("• سيقوم البرنامج بالتحقق من صلاحية sessionid.")
    print("• سيتم عرض بيانات الحساب والرصيد والخيارات المتاحة.\n")
    print(Fore.YELLOW + "ملاحظة: sessionid يجب أن يكون صالح وغير منتهي.\n")
    print(Fore.CYAN + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")

# الدالة الرئيسية
def main():
    show_intro()
    session = input(Fore.GREEN + Style.BRIGHT + "• أدخل sessionid: " + Fore.RESET).strip()
    print(Fore.BLUE + Style.BRIGHT + "\n• جاري جلب البيانات...\n")
    
    try:
        info = generalinfo(session)
        bal = balance(session)
        
        if info.get("message") != "success":
            print(Fore.RED + Style.BRIGHT + "• sessionid غير صالح أو منتهي الصلاحية")
            return

        karb2 = info.get("data", {})
        Karb1 = bal.json().get("data", {})

        created = karb2.get("create_time", 0)

        # عرض البيانات
        print(Fore.CYAN + Style.BRIGHT + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(Fore.YELLOW + Style.BRIGHT + "           بيانات الحساب\n")
        print(Fore.GREEN + f"• Username: {karb2.get('username')}")
        print(f"• User ID: {karb2.get('user_id')}")
        print(f"• Sec User ID: {karb2.get('sec_user_id')}")
        print(f"• Screen Name: {karb2.get('screen_name')}")
        print(f"• Avatar: {karb2.get('avatar_url')}")
        print(f"• Bio: {karb2.get('description')}")
        print(f"• Mobile: {karb2.get('mobile')}")
        print(f"• Email: {karb2.get('email')}")
        print(f"• Created At: {conv(created) if created else 'N/A'}\n")

        print(Fore.MAGENTA + Style.BRIGHT + "           الرصيد والعملات\n")
        print(Fore.GREEN + f"• Coins: {Karb1.get('coins')}")
        print(f"• Frozen Coins: {Karb1.get('frozen_coins')}")
        print(f"• Blocked: {Karb1.get('block_coin_page')}")
        print(f"• Allow Status: {Karb1.get('is_allow')}")
        print(f"• Email Confirmed: {Karb1.get('is_email_confirmed')}")
        print(f"• First Web Recharge: {Karb1.get('is_first_web_recharge')}")
        print(f"• Periodic Payout: {Karb1.get('is_periodic_payout')}")
        print(f"• Show Page: {Karb1.get('is_show')}")
        print(f"• PC Web Status: {Karb1.get('pc_web_recharge_status')}")
        print(f"• Quick Payment: {Karb1.get('quick_payment_available')}")

        print(Fore.CYAN + Style.BRIGHT + "\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(Fore.YELLOW + Style.BRIGHT + "• تم العرض بواسطة TIKTOK INFO TOOL")
        print(Fore.CYAN + Style.BRIGHT + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")

    except Exception as e:
        print(Fore.RED + Style.BRIGHT + f"• حدث خطأ:\n{e}")

# تشغيل البرنامج
if __name__ == "__main__":
    main()