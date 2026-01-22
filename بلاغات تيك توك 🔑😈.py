# ===============================
# IMPORTS
# ===============================
import time
import os
from fake_useragent import UserAgent
import re,requests
import time
from os import system
import re
import sys
from user_agent import generate_user_agent
import pyfiglet
import time
from termcolor import colored
import random
import time
import requests


o = requests.get("https://github.com/PSSSps/-1/raw/refs/heads/main/protection").text

if 'PS_oxas_ps' in o:
    pass
else:
    # طباعة الرسالة باللون الأحمر
    print("\033[31mانتهت المدة المجاني اذا تحب تشترك تواصل مع المطور PS>> @v77v6<<\033[0m")
    exit()
	
	

rrep='"status_code":0,"status_msg":"Thanks for your feedback"'
# ===============================
# COLORS & BG
# ===============================
BG = '\033[48;5;52m'       # Soft blood red background
RST = '\033[0m'            # Reset
LINE_COLOR = '\033[1;35m'  # Bold Magenta for lines
DESC_COLOR = '\033[1;31m'  # Red for descriptions
BULLET_COLOR = '\033[1;33m' # Yellow for bullets •
CHECK_COLOR = '\033[1;32m'  # Green for √
OPTION_COLOR = '\033[1;33m' # Yellow for menu options
NUM_COLOR = '\033[1;36m'    # Cyan for numbers
WOCO_COLOR = '\033[1;31m'   # Red color for woco lines
BG = '\033[48;5;52m'
RST = '\033[0m'

LINE = "━━━━━━━━━━━━━━━━━━━━"

# ===============================
# CLEAR SCREEN
# ===============================
def clear():
    os.system('cls' if os.name=='nt' else 'clear')
    print(BG, end='')

# ===============================
# TYPE SLOWLY LINE BY LINE
# ===============================
def type_slow_line(text, delay=0.003):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# ===============================
# DESCRIPTIONS
# ===============================
descriptions = [
    f"{BULLET_COLOR}• {DESC_COLOR}The Ultimate Report Tool V.1.0. 😈 {CHECK_COLOR}√{RST}{BG}",
    f"{BULLET_COLOR}• {DESC_COLOR}Advanced Anti-Detection System  {CHECK_COLOR}√{RST}{BG}",
    f"{BULLET_COLOR}• {DESC_COLOR}Proxy Integration  {CHECK_COLOR}√{RST}{BG}",
    f"{BULLET_COLOR}• {DESC_COLOR}Session Management  {CHECK_COLOR}√{RST}{BG}",
    f"{BULLET_COLOR}• {DESC_COLOR}Multiple Report Types {CHECK_COLOR}√{RST}{BG}",
    f"{BULLET_COLOR}• {DESC_COLOR}Auto Logging of Reports {CHECK_COLOR}√{RST}{BG}",
    f"{BULLET_COLOR}• {DESC_COLOR}User-Friendly Interface {CHECK_COLOR}√{RST}{BG}",
    f"{BULLET_COLOR}• {DESC_COLOR}Fast & Secure Automation {CHECK_COLOR}√{RST}{BG}",
    f"{BULLET_COLOR}• {DESC_COLOR}Supports Parallel Sessions {CHECK_COLOR}√{RST}{BG}",
    f"{BULLET_COLOR}• {DESC_COLOR}Optimized for Efficiency {CHECK_COLOR}√{RST}{BG}"
]


o = requests.get("https://github.com/PSSSps/-1/raw/refs/heads/main/protection").text

if 'PS_oxas_ps' in o:
    pass
else:
    # طباعة الرسالة باللون الأحمر
    print("\033[31mانتهت المدة المجاني اذا تحب تشترك تواصل مع المطور PS>> @v77v6<<\033[0m")
    exit()
# ===============================
# WOCO OLD ASCII
# ===============================
woco = [
"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠈⠉⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿",
"⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿",
"⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿",
"⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⢀⣠⣤⣤⣤⣤⣄⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿",
"⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠾⣿⣿⣿⣿⠿⠛⠉⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿",
"⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⣤⣶⣤⣉⣿⣿⡯⣀⣴⣿⡗⠀⠀⠀⠀⣿⣿⣿⣿⣿",
"⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⡈⠀⠀⠉⣿⣿⣶⡉⠀⠀⣀⡀⠀⠀⠀⢻⣿⣿⣿⣿",
"⣿⣿⣿⣿⣿⣿⡇⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⢸⣿⣿⣿⣿",
"⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠉⢉⣽⣿⠿⣿⡿⢻⣯⡍⢁⠄⠀⠀⠀⣸⣿⣿⣿⣿",
"⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠐⡀⢉⠉⠀⠠⠀⢉⣉⠀⡜⠀⠀⠀⠀⣿⣿⣿⣿⣿",
"⣿⣿⣿⣿⣿⣿⠿⠁⠀⠀⠀⠘⣤⣭⣟⠛⠛⣉⣁⡜⠀⠀⠀⠀⠀⠛⠿⣿⣿⣿",
"⡿⠟⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⡀⠀⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉𝑷𝑺 @𝒗77𝒗6"
]
o = requests.get("https://github.com/PSSSps/-1/raw/refs/heads/main/protection").text

if 'PS_oxas_ps' in o:
    pass
else:
    # طباعة الرسالة باللون الأحمر
    print("\033[31mانتهت المدة المجاني اذا تحب تشترك تواصل مع المطور PS>> @v77v6<<\033[0m")
    exit()
# ===============================
# CLEAR SCREEN INITIALLY
# ===============================
clear()

# ===============================
# PRINT DESCRIPTIONS THEN HIDE AFTER 3 SEC
# ===============================
print(f"{LINE_COLOR}{LINE}{RST}{BG}")
for desc in descriptions:
    type_slow_line(desc, delay=0.003)
print(f"{LINE_COLOR}{LINE}{RST}{BG}")
time.sleep(3)
clear()  # مسح الوصف قبل عرض WOCO

# ===============================
# PRINT WOCO WITH COLOR
# ===============================
for line in woco:
    type_slow_line(f"{WOCO_COLOR}{line}{RST}{BG}", delay=0.002)

# ===============================
# PRINT SEPARATOR LINE BETWEEN WOCO AND OPTIONS
# ===============================
print(f"{LINE_COLOR}━━━━━━━━━━━━━━━━━━PS━━━━━━━━━━━━━━━━━━{RST}{BG}")

# ===============================
# MENU OPTIONS
# ===============================
options = [
    "[1] • REPORT CONTENT",
    "[2] • SPAM OR HARASSMENT",
    "[3] • UNDER AGE (13-)",
    "[4] • FAKE INFO / IMPERSONATION",
    "[5] • HATE SPEECH",
    "[6] • ADULT CONTENT",
    "[7] • TERRORIST ORGANIZATIONS",
    "[8] • SELF HARM",
    "[9] • BULLYING / HARASSMENT",
    "[10] • VIOLENCE"
]

o = requests.get("https://github.com/PSSSps/-1/raw/refs/heads/main/protection").text

if 'PS_oxas_ps' in o:
    pass
else:
    # طباعة الرسالة باللون الأحمر
    print("\033[31mانتهت المدة المجاني اذا تحب تشترك تواصل مع المطور PS>> @v77v6<<\033[0m")
    exit()
for opt in options:
    num = opt.split(']')[0] + ']'  # extract number
    text = opt.split(']')[1]       # extract text
    type_slow_line(f"{NUM_COLOR}{num} {OPTION_COLOR}{text.strip()}{RST}{BG}", delay=0.003)
    print(f"{LINE_COLOR}{LINE}{RST}{BG}")

# ===============================
# USER INPUT
# ===============================
kaito = int(input(f"{NUM_COLOR}[?] Select Report Type: {RST}{BG}"))
print(f"{LINE_COLOR}{LINE}{RST}{BG}")
session = input(f"{NUM_COLOR}[?] Enter Session ID: {RST}{BG}")
print(f"{LINE_COLOR}{LINE}{RST}{BG}")
user = input(f"{NUM_COLOR}[?] Enter Target Username: {RST}{BG}")
print(f"{LINE_COLOR}{LINE}{RST}{BG}")
sleep = int(input(f"{NUM_COLOR}[?] Sleep Time [5/10]: {RST}{BG}"))
print(f"{LINE_COLOR}{LINE}{RST}{BG}")

url = 'https://api16-normal-c-alisg.tiktokv.com/passport/account/info/v2/?scene=normal&multi_login=1&account_sdk_source=app&passport-sdk-version=19&os_api=25&device_type=A5010&ssmix=a&manifest_version_code=2018093009&dpi=191&carrier_region=JO&uoo=1&region=US&app_name=musical_ly&version_name=7.1.2&timezone_offset=28800&ts=1628767214&ab_version=7.1.2&residence=SA&cpu_support64=false&current_region=JO&ac2=wifi&ac=wifi&app_type=normal&host_abi=armeabi-v7a&channel=googleplay&update_version_code=2018093009&_rticket=1628767221573&device_platform=android&iid=7396386396296286392&build_number=7.1.2&locale=en&op_region=SA&version_code=200705&timezone_name=Asia%2FShanghai&cdid=f61ca549-c9ee-450b-90da-8854423b74e7&openudid=3e5afbd3f6dde322&sys_region=US&device_id=7296396296396396393&app_language=en&resolution=576*1024&device_brand=OnePlus&language=en&os_version=7.1.2&aid=1233&mcc_mnc=2947'

headers={'Host': 'api16-normal-c-alisg.tiktokv.com', 'Cookie': 'sessionid='+session,'Accept-Encoding': 'gzip, deflate',
'User-Agent': generate_user_agent()}
reu = requests.get(url,headers=headers)
if '"session expired, please sign in again"' in reu.text:
	print(Z+'[!] Invalid Session ID')
	exit(0)
elif 'user_id' in reu.text:
	useo = str(reu.json()['data']['user_id']) 
#i
#==========lol=============9
head={
'Host': 'www.tiktok.com',
'User-Agent': generate_user_agent(),
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
'Accept-Encoding': 'gzip, deflate',
'Upgrade-Insecure-Requests': '1',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'none',
'Sec-Fetch-User': '?1',
'Te': 'trailers',
'Connection': 'close',
}

req=requests.get(f'https://www.tiktok.com/@{user}?lang=en',headers=head)
try:
	ID=re.findall('''"user":{"id":"(.*?)"''',req.text)[0]
except:
	print(Z+'[!] Username Not Found or Banned')
	
if kaito==1:
	while True:
		time.sleep(sleep)
		url = f'https://www.tiktok.com/aweme/v1/aweme/feedback/?aid=1233&app_name=tiktok_web&device_platform=web_mobile&device_id=7008218736944907778&region=SA&priority_region=SA&os=ios&referer=https:%2F%2Fwww.tiktok.com%2Fsetting&root_referer=https:%2F%2Fwww.tiktok.com%2Fsetting&cookie_enabled=true&screen_width=375&screen_height=667&browser_language=en-US&browser_platform=iPhone&browser_name=Mozilla&browser_version=5.0+(iPhone%3B+CPU+iPhone+OS+15_0_1+like+Mac+OS+X)+AppleWebKit%2F605.1.15+(KHTML,+like+Gecko)+InspectBrowser&browser_online=true&verifyFp=verify_kvwdf2dq_xDfMDVTW_cgOV_4YKO_86hQ_Y9HBPRJGuNau&app_language=en&timezone_name=Asia%2FRiyadh&is_page_visible=true&focus_state=true&is_fullscreen=false&history_len=6&reason=399&report_type=user&object_id={ID}&owner_id={ID}&target={ID}&reporter_id=7024230440182809606&current_region=SA'
		hea_rep = {
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
			'Accept-Encoding':'gzip, deflate, br',
			'Accept-Language':'en-US,en;q=0.5',
			'Connection':'keep-alive',
			'Cookie':'sessionid='+session,
			'Host':'www.tiktok.com',
			'Sec-Fetch-Dest':'document',
			'Sec-Fetch-Mode': 'navigate',
			'Sec-Fetch-Site':'none',
			'Sec-Fetch-User':'?1',
			'Upgrade-Insecure-Requests':'1',
			'User-Agent':generate_user_agent()}
		data={
			"object_id":ID,
			"owner_id":ID,
			"report_type":"user",
			"target":ID}
		rept = requests.post(url,headers=hea_rep,data=data)
		if rrep in rept.text:
			print(R + "[!] Error Sending Report")
		else:
			print(BG + "[+] Report Sent Successfully")	
elif kaito ==2:
	while True:
		time.sleep(sleep)
		url2=f'https://www.tiktok.com/aweme/v1/aweme/feedback/?aid=1233&app_name=tiktok_web&device_platform=web_mobile&device_id=7008218736944907778&region=SA&priority_region=SA&os=ios&referer=https:%2F%2Fwww.tiktok.com%2Fsetting&root_referer=https:%2F%2Fwww.tiktok.com%2F&cookie_enabled=true&screen_width=375&screen_height=667&browser_language=en-US&browser_platform=iPhone&browser_name=Mozilla&browser_version=5.0+(iPhone%3B+CPU+iPhone+OS+15_0_1+like+Mac+OS+X)+AppleWebKit%2F605.1.15+(KHTML,+like+Gecko)+InspectBrowser&browser_online=true&verifyFp=verify_kvxyp4rs_dANMHnrG_lvVu_4qPI_97cp_HhJjttqMJhNK&app_language=en&timezone_name=Asia%2FRiyadh&is_page_visible=true&focus_state=true&is_fullscreen=false&history_len=10&reason=310&report_type=user&object_id={ID}&owner_id={ID}&target={ID}&reporter_id=27568146&current_region=SA'
		hea_rep2 = {
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
			'Accept-Encoding':'gzip, deflate, br',
			'Accept-Language':'en-US,en;q=0.5',
			'Connection':'keep-alive',
			'Cookie':'sessionid='+session,
			'Host':'www.tiktok.com',
			'Sec-Fetch-Dest':'document',
			'Sec-Fetch-Mode': 'navigate',
			'Sec-Fetch-Site':'none',
			'Sec-Fetch-User':'?1',
			'Upgrade-Insecure-Requests':'1',
			'User-Agent':generate_user_agent()}
		data2={
			"object_id":ID,
			"owner_id":ID,
			"report_type":"user",
			"target":ID}
		rept2 = requests.post(url2,headers=hea_rep2,data=data2)
		if rrep in rept2.text:
			print(R + "[!] Error Sending Report")
		else:
			print(BG + "[+] Report Sent Successfully")	
elif kaito==3:
	while True:
		time.sleep(sleep)
		url3=f'https://www.tiktok.com/aweme/v1/aweme/feedback/?aid=1233&app_name=tiktok_web&device_platform=web_mobile&device_id=7008218736944907778&region=SA&priority_region=SA&os=ios&referer=https:%2F%2Fwww.tiktok.com%2Fsetting&root_referer=https:%2F%2Fwww.tiktok.com%2F&cookie_enabled=true&screen_width=375&screen_height=667&browser_language=en-US&browser_platform=iPhone&browser_name=Mozilla&browser_version=5.0+(iPhone%3B+CPU+iPhone+OS+15_0_1+like+Mac+OS+X)+AppleWebKit%2F605.1.15+(KHTML,+like+Gecko)+InspectBrowser&browser_online=true&verifyFp=verify_kvxyp4rs_dANMHnrG_lvVu_4qPI_97cp_HhJjttqMJhNK&app_language=en&timezone_name=Asia%2FRiyadh&is_page_visible=true&focus_state=true&is_fullscreen=false&history_len=10&reason=317&report_type=user&object_id={ID}&owner_id={ID}&target={ID}&reporter_id=27568146&current_region=SA'
		hea_rep3 = {
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
			'Accept-Encoding':'gzip, deflate, br',
			'Accept-Language':'en-US,en;q=0.5',
			'Connection':'keep-alive',
			'Cookie':'sessionid='+session,
			'Host':'www.tiktok.com',
			'Sec-Fetch-Dest':'document',
			'Sec-Fetch-Mode': 'navigate',
			'Sec-Fetch-Site':'none',
			'Sec-Fetch-User':'?1',
			'Upgrade-Insecure-Requests':'1',
			'User-Agent':generate_user_agent()}
		data3={
			"object_id":ID,
			"owner_id":ID,
			"report_type":"user",
			"target":ID}
		rept3 = requests.post(url3,headers=hea_rep3,data=data3)
		if rrep in rept3.text:
			print(R + "[!] Error Sending Report")
		else:
			print(BG + "[+] Report Sent Successfully")
elif kaito==4:
	while True:
		time.sleep(sleep)
		url4=f'https://www.tiktok.com/aweme/v1/aweme/feedback/?aid=1233&app_name=tiktok_web&device_platform=web_mobile&device_id=7034110346035136001&region=SA&priority_region=SA&os=ios&referer=https:%2F%2Fwww.tiktok.com%2Fsetting&root_referer=https:%2F%2Fwww.tiktok.com%2Fsetting&cookie_enabled=true&screen_width=375&screen_height=667&browser_language=en-US&browser_platform=iPhone&browser_name=Mozilla&browser_version=5.0+(iPhone%3B+CPU+iPhone+OS+15_1+like+Mac+OS+X)+AppleWebKit%2F605.1.15+(KHTML,+like+Gecko)+InspectBrowser&browser_online=true&verifyFp=verify_kx800pjx_bJTxKplQ_YGw2_4nQz_9ti1_lo63INRiR3i0&app_language=ar&timezone_name=Asia%2FRiyadh&is_page_visible=true&focus_state=true&is_fullscreen=false&history_len=7&reason=3142&report_type=user&object_id={ID}&owner_id={ID}&target={ID}&reporter_id=6955107540677968897&current_region=SA'
		hea_rep4 = {
				'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
				'Accept-Encoding':'gzip, deflate, br',
				'Accept-Language':'en-US,en;q=0.5',
				'Connection':'keep-alive',
				'Cookie':'sessionid='+session,
				'Host':'www.tiktok.com',
				'Sec-Fetch-Dest':'document',
				'Sec-Fetch-Mode': 'navigate',
				'Sec-Fetch-Site':'none',
				'Sec-Fetch-User':'?1',
				'Upgrade-Insecure-Requests':'1',
				'User-Agent':generate_user_agent()}
		data4={
			"object_id":ID,
			"owner_id":ID,
			"report_type":"user",
			"target":ID}
		rept4 = requests.post(url4,headers=hea_rep4,data=data4)
		if rrep in rept4.text:
			print(R + "[!] Error Sending Report")
		else:
			print(BG + "[+] Report Sent Successfully")	
elif kaito==5:
	while True:
		time.sleep(sleep)
		url5=f'https://www.tiktok.com/aweme/v1/aweme/feedback/?aid=1233&app_name=tiktok_web&device_platform=web_mobile&device_id=7034110346035136001&region=SA&priority_region=SA&os=ios&referer=https:%2F%2Fwww.tiktok.com%2Fsetting&root_referer=https:%2F%2Fwww.tiktok.com%2Fsetting&cookie_enabled=true&screen_width=375&screen_height=667&browser_language=en-US&browser_platform=iPhone&browser_name=Mozilla&browser_version=5.0+(iPhone%3B+CPU+iPhone+OS+15_1+like+Mac+OS+X)+AppleWebKit%2F605.1.15+(KHTML,+like+Gecko)+InspectBrowser&browser_online=true&verifyFp=verify_kx800pjx_bJTxKplQ_YGw2_4nQz_9ti1_lo63INRiR3i0&app_language=ar&timezone_name=Asia%2FRiyadh&is_page_visible=true&focus_state=true&is_fullscreen=false&history_len=7&reason=306&report_type=user&object_id={ID}&owner_id={ID}&target={ID}&reporter_id=6955107540677968897&current_region=SA'
		hea_rep5 = {
				'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
				'Accept-Encoding':'gzip, deflate, br',
				'Accept-Language':'en-US,en;q=0.5',
				'Connection':'keep-alive',
				'Cookie':'sessionid='+session,
				'Host':'www.tiktok.com',
				'Sec-Fetch-Dest':'document',
				'Sec-Fetch-Mode': 'navigate',
				'Sec-Fetch-Site':'none',
				'Sec-Fetch-User':'?1',
				'Upgrade-Insecure-Requests':'1',
				'User-Agent':generate_user_agent()}
		data5={
			"object_id":ID,
			"owner_id":ID,
			"report_type":"user",
			"target":ID}
		rept5 = requests.post(url5,headers=hea_rep5,data=data5)
		if rrep in rept5.text:
			print(R + "[!] Error Sending Report")
		else:
			print(BG + "[+] Report Sent Successfully")
elif kaito==6:
	while True:
		time.sleep(sleep)
		url6=f'https://www.tiktok.com/aweme/v1/aweme/feedback/?aid=1233&app_name=tiktok_web&device_platform=web_mobile&device_id=7034110346035136001&region=SA&priority_region=SA&os=ios&referer=https:%2F%2Fwww.tiktok.com%2Flogin%2Fphone-or-email%3Fenter_method%3Denter_personal_homepage%26lang%3Den%26launch_type%3D0%26redirect_url%3Dhttps%25253A%25252F%25252Fwww.tiktok.com%25252Fprofile%25253Flang%25253Den%26enter_from%3Dpersonal_homepage&root_referer=https:%2F%2Fwww.tiktok.com%2Fsetting&cookie_enabled=true&screen_width=375&screen_height=667&browser_language=en-US&browser_platform=iPhone&browser_name=Mozilla&browser_version=5.0+(iPhone%3B+CPU+iPhone+OS+15_1+like+Mac+OS+X)+AppleWebKit%2F605.1.15+(KHTML,+like+Gecko)+InspectBrowser&browser_online=true&verifyFp=verify_kx800pjx_bJTxKplQ_YGw2_4nQz_9ti1_lo63INRiR3i0&app_language=ar&timezone_name=Asia%2FRiyadh&is_page_visible=true&focus_state=true&is_fullscreen=false&history_len=14&reason=308&report_type=user&object_id={ID}&owner_id={ID}&target={ID}&reporter_id=310430566162530304&current_region=SA'
		hea_rep6 = {
				'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
				'Accept-Encoding':'gzip, deflate, br',
				'Accept-Language':'en-US,en;q=0.5',
				'Connection':'keep-alive',
				'Cookie':'sessionid='+session,
				'Host':'www.tiktok.com',
				'Sec-Fetch-Dest':'document',
				'Sec-Fetch-Mode': 'navigate',
				'Sec-Fetch-Site':'none',
				'Sec-Fetch-User':'?1',
				'Upgrade-Insecure-Requests':'1',
				'User-Agent':generate_user_agent()}
		data6={
			"object_id":ID,
			"owner_id":ID,
			"report_type":"user",
			"target":ID}
		rept6 = requests.post(url6,headers=hea_rep6,data=data6)
		if rrep in rept6.text:
			print(R + "[!] Error Sending Report")
		else:
			print(BG + "[+] Report Sent Successfully")
elif kaito==7:
	while True:
		time.sleep(sleep)
		url7=f'https://www.tiktok.com/aweme/v1/aweme/feedback/?aid=1233&app_name=tiktok_web&device_platform=web_mobile&device_id=7034110346035136001&region=SA&priority_region=SA&os=ios&referer=https:%2F%2Fwww.tiktok.com%2Flogin%2Fphone-or-email%3Fenter_method%3Denter_personal_homepage%26lang%3Den%26launch_type%3D0%26redirect_url%3Dhttps%25253A%25252F%25252Fwww.tiktok.com%25252Fprofile%25253Flang%25253Den%26enter_from%3Dpersonal_homepage&root_referer=https:%2F%2Fwww.tiktok.com%2Fsetting&cookie_enabled=true&screen_width=375&screen_height=667&browser_language=en-US&browser_platform=iPhone&browser_name=Mozilla&browser_version=5.0+(iPhone%3B+CPU+iPhone+OS+15_1+like+Mac+OS+X)+AppleWebKit%2F605.1.15+(KHTML,+like+Gecko)+InspectBrowser&browser_online=true&verifyFp=verify_kx800pjx_bJTxKplQ_YGw2_4nQz_9ti1_lo63INRiR3i0&app_language=ar&timezone_name=Asia%2FRiyadh&is_page_visible=true&focus_state=true&is_fullscreen=false&history_len=14&reason=3011&report_type=user&object_id={ID}&owner_id={ID}&target={ID}&reporter_id=310430566162530304&current_region=SA'
		hea_rep7 = {
				'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
				'Accept-Encoding':'gzip, deflate, br',
				'Accept-Language':'en-US,en;q=0.5',
				'Connection':'keep-alive',
				'Cookie':'sessionid='+session,
				'Host':'www.tiktok.com',
				'Sec-Fetch-Dest':'document',
				'Sec-Fetch-Mode': 'navigate',
				'Sec-Fetch-Site':'none',
				'Sec-Fetch-User':'?1',
				'Upgrade-Insecure-Requests':'1',
				'User-Agent':generate_user_agent()}
		data7={
			"object_id":ID,
			"owner_id":ID,
			"report_type":"user",
			"target":ID}
		rept7 = requests.post(url7,headers=hea_rep7,data=data7)
		if rrep in rept7.text:
			print(R + "[!] Error Sending Report")
		else:
			print(BG + "[+] Report Sent Successfully")
elif kaito==8:
	while True:
		time.sleep(sleep)
		url8=f'https://www.tiktok.com/aweme/v1/aweme/feedback/?aid=1233&app_name=tiktok_web&device_platform=web_mobile&device_id=7034110346035136001&region=SA&priority_region=SA&os=ios&referer=https:%2F%2Fwww.tiktok.com%2Flogin%2Fphone-or-email%3Fenter_method%3Denter_personal_homepage%26lang%3Den%26launch_type%3D0%26redirect_url%3Dhttps%25253A%25252F%25252Fwww.tiktok.com%25252Fprofile%25253Flang%25253Den%26enter_from%3Dpersonal_homepage&root_referer=https:%2F%2Fwww.tiktok.com%2Fsetting&cookie_enabled=true&screen_width=375&screen_height=667&browser_language=en-US&browser_platform=iPhone&browser_name=Mozilla&browser_version=5.0+(iPhone%3B+CPU+iPhone+OS+15_1+like+Mac+OS+X)+AppleWebKit%2F605.1.15+(KHTML,+like+Gecko)+InspectBrowser&browser_online=true&verifyFp=verify_kx800pjx_bJTxKplQ_YGw2_4nQz_9ti1_lo63INRiR3i0&app_language=ar&timezone_name=Asia%2FRiyadh&is_page_visible=true&focus_state=true&is_fullscreen=false&history_len=14&reason=3052&report_type=user&object_id={ID}&owner_id={ID}&target={ID}&reporter_id=310430566162530304&current_region=SA'
		hea_rep8 = {
				'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
				'Accept-Encoding':'gzip, deflate, br',
				'Accept-Language':'en-US,en;q=0.5',
				'Connection':'keep-alive',
				'Cookie':'sessionid='+session,
				'Host':'www.tiktok.com',
				'Sec-Fetch-Dest':'document',
				'Sec-Fetch-Mode': 'navigate',
				'Sec-Fetch-Site':'none',
				'Sec-Fetch-User':'?1',
				'Upgrade-Insecure-Requests':'1',
				'User-Agent':generate_user_agent()}
		data8={
			"object_id":ID,
			"owner_id":ID,
			"report_type":"user",
			"target":ID}
		rept8 = requests.post(url8,headers=hea_rep8,data=data8)
		if rrep in rept8.text:
			print(R + "[!] Error Sending Report")
		else:
			print(BG + "[+] Report Sent Successfully")
elif kaito==9:
	while True:
		time.sleep(sleep)
		url9=f'https://www.tiktok.com/aweme/v1/aweme/feedback/?aid=1233&app_name=tiktok_web&device_platform=web_mobile&device_id=7034110346035136001&region=SA&priority_region=SA&os=ios&referer=https:%2F%2Fwww.tiktok.com%2Flogin%2Fphone-or-email%3Fenter_method%3Denter_personal_homepage%26lang%3Den%26launch_type%3D0%26redirect_url%3Dhttps%25253A%25252F%25252Fwww.tiktok.com%25252Fprofile%25253Flang%25253Den%26enter_from%3Dpersonal_homepage&root_referer=https:%2F%2Fwww.tiktok.com%2Fsetting&cookie_enabled=true&screen_width=375&screen_height=667&browser_language=en-US&browser_platform=iPhone&browser_name=Mozilla&browser_version=5.0+(iPhone%3B+CPU+iPhone+OS+15_1+like+Mac+OS+X)+AppleWebKit%2F605.1.15+(KHTML,+like+Gecko)+InspectBrowser&browser_online=true&verifyFp=verify_kx800pjx_bJTxKplQ_YGw2_4nQz_9ti1_lo63INRiR3i0&app_language=ar&timezone_name=Asia%2FRiyadh&is_page_visible=true&focus_state=true&is_fullscreen=false&history_len=14&reason=3072&report_type=user&object_id={ID}&owner_id={ID}&target={ID}&reporter_id=310430566162530304&current_region=SA'
		hea_rep9 = {
				'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
				'Accept-Encoding':'gzip, deflate, br',
				'Accept-Language':'en-US,en;q=0.5',
				'Connection':'keep-alive',
				'Cookie':'sessionid='+session,
				'Host':'www.tiktok.com',
				'Sec-Fetch-Dest':'document',
				'Sec-Fetch-Mode': 'navigate',
				'Sec-Fetch-Site':'none',
				'Sec-Fetch-User':'?1',
				'Upgrade-Insecure-Requests':'1',
				'User-Agent':generate_user_agent()}
		data9={
			"object_id":ID,
			"owner_id":ID,
			"report_type":"user",
			"target":ID}
		rept9 = requests.post(url9,headers=hea_rep9,data=data9)
		if rrep in rept9.text:
			print(R + "[!] Error Sending Report")
		else:
			print(BG + "[+] Report Sent Successfully")
elif kaito==10:
	while True:
		time.sleep(sleep)
		url10=f'https://www.tiktok.com/aweme/v1/aweme/feedback/?aid=1233&app_name=tiktok_web&device_platform=web_mobile&device_id=7034110346035136001&region=SA&priority_region=SA&os=ios&referer=https:%2F%2Fwww.tiktok.com%2Flogin%2Fphone-or-email%3Fenter_method%3Denter_personal_homepage%26lang%3Den%26launch_type%3D0%26redirect_url%3Dhttps%25253A%25252F%25252Fwww.tiktok.com%25252Fprofile%25253Flang%25253Den%26enter_from%3Dpersonal_homepage&root_referer=https:%2F%2Fwww.tiktok.com%2Fsetting&cookie_enabled=true&screen_width=375&screen_height=667&browser_language=en-US&browser_platform=iPhone&browser_name=Mozilla&browser_version=5.0+(iPhone%3B+CPU+iPhone+OS+15_1+like+Mac+OS+X)+AppleWebKit%2F605.1.15+(KHTML,+like+Gecko)+InspectBrowser&browser_online=true&verifyFp=verify_kx800pjx_bJTxKplQ_YGw2_4nQz_9ti1_lo63INRiR3i0&app_language=ar&timezone_name=Asia%2FRiyadh&is_page_visible=true&focus_state=true&is_fullscreen=false&history_len=14&reason=303&report_type=user&object_id={ID}&owner_id={ID}&target={ID}&reporter_id=310430566162530304&current_region=SA'
	hea_rep10 = {
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
			'Accept-Encoding':'gzip, deflate, br',
			'Accept-Language':'en-US,en;q=0.5',
			'Connection':'keep-alive',
			'Cookie':'sessionid='+session,
			'Host':'www.tiktok.com',
			'Sec-Fetch-Dest':'document',
			'Sec-Fetch-Mode': 'navigate',
			'Sec-Fetch-Site':'none',
			'Sec-Fetch-User':'?1',
			'Upgrade-Insecure-Requests':'1',
			'User-Agent':generate_user_agent()}
	data10={
		"object_id":ID,
		"owner_id":ID,
		"report_type":"user",
		"target":ID}
	rept10 = requests.post(url10,headers=hea_rep10,data=data10)
	if rrep in rept10.text:
		print(R + "[!] Error Sending Report")
	else:
		print(F+'[+] Report Sent Successfully')
