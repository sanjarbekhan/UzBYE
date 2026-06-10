import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from flask import Flask
from threading import Thread
import io  # Uzun matnlarni aqlli ravishda faylga aylantirish uchun kerak

# Bot tokenini kiriting
TOKEN = '8915114593:AAFalFfZssCdMdVD0P3NdjrX2qsmffWCeJs'
bot = telebot.TeleBot(TOKEN, parse_mode='HTML')

# Admin ID raqami
ADMIN_ID = 6755433894  

# Foydalanuvchilar ma'lumotlarini vaqtinchalik saqlash uchun lug'at
user_data = {}

class UserForm:
    def __init__(self):
        self.ism = None
        self.familiya = None
        self.ota_ismi = None
        self.tg_user = None
        self.telefon = None
        self.user_id = None
        self.answers = None
        self.photo_file_id = None
        self.file_type = None
        self.instagram = None

# Asosiy menyu tugmalari
def main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = KeyboardButton('📝 Ariza qoldirish')
    btn2 = KeyboardButton('🌐 Ijtimoiy tarmoqlarimiz')
    btn3 = KeyboardButton('ℹ️ Biz haqimizda')
    markup.add(btn1)
    markup.add(btn2, btn3)
    return markup

# --- FLASK SERVER (RENDER/UPTIMEROBOT UCHUN) ---
app = Flask('')

@app.route('/')
def home():
    return "Bot ishlayapti!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
# ---------------------------------------------

@bot.message_handler(commands=['start'])
def send_welcome(message):
    first_name = message.from_user.first_name
    text = f"Assalomu alaykum <b>{first_name}</b>, \"Oʻzbekiston Bunyodkor Yoshlari ensiklopediyasi\" telegram botiga xush kelibsiz!\n\nIltimos Kerakli boʻlimni tanlang."
    bot.send_message(message.chat.id, text, reply_markup=main_menu())

@bot.message_handler(func=lambda message: message.text == 'ℹ️ Biz haqimizda')
def about_us(message):
    about_text = (
        "<b>O'zbekiston Bunyodkor Yoshlari ensiklopediyasi har qanday sohada faoliyat olib borayotgan, o'z ustida ishlayotgan intiluvchan yoshlarni ommaga tanitish va hujjatlashtirishni maqsad qilgan respublika miqyosidagi ulkan loyihalardir.\n\n"
        "Ensiklopediyaga istalgan sohada faoliyat yuritayotgan, o‘z ustida ishlayotgan yoshlar qabul qilinadi!</b>\n\n"
        "Ushbu ma'lumotda ensiklopediyamizga kirishning afzalliklari keltirib o'tilgan:\n\n"
        "✅ <b>Qidiruv tizimlarida ko‘rinish:</b>\n"
        "Siz haqingizdagi maqola Google, Yandex, Bing kabi qidiruv tizimlarida chiqadi. Bu sizni istagan odam — hamkor, ish beruvchi yoki jurnalist — osongina topishi mumkinligini anglatadi.\n\n"
        "✅ <b>Sun’iy intellekt platformalarida tanilish:</b>\n"
        "ChatGPT, Copilot, Gemini kabi sun’iy intellekt tizimlari endilikda siz haqingizda aniq manbasiz ma’lumot bera olmaydi. Bu onlayn obro‘yingizni mustahkamlovchi kuchli vosita.\n\n"
        "✅ <b>Kelajakdagi Wikipedia sahifangiz uchun asos:</b>\n"
        "Bugun e’lon qilinadigan maqola — ertaga siz haqingizda yoziladigan Wikipedia sahifasi uchun tayyor ishonchli manba bo‘lishi mumkin.\n\n"
        "✅ <b>Ijtimoiy tarmoqlarda tasdiq belgisi olish imkoniyati:</b>\n"
        "Instagram, Facebook, TikTok, YouTube kabi platformalarda ko‘k nishon olish uchun siz haqingizda onlayn nashrlar zarur. Ushbu maqola bu yo‘lda ishonchli hujjat bo‘lib xizmat qiladi.\n\n"
        "✅ <b>Rezumega qo‘shiladigan rasmiy havola:</b>\n"
        "Ish qidirishda, grantga hujjat topshirishda yoki xalqaro loyihalarda qatnashishda ushbu maqola — sizning shaxsiy brendingizni isbotlovchi kuchli hujjat bo‘ladi.\n\n"
        "✅ <b>Bunyodkor yoshlar online jurnalida yoritilish:</b>\n"
        "Biografik maqolasi bor yoshlar Bunyodkor yoshlar online jurnalida muntazam yoritiladi. Ularning hayotida yuz bergan muhim voqea, ularning loyihalari va tashabburlari keng targ'ib qilinadi.\n\n"
        "✅ <b>Ommaviy axborot vositalari e’tiboriga tushasiz:</b>\n"
        "Jurnalistlar, blogerlar, televideniye va radio uchun maqolaviy manba sifatida sizga murojaatlar ko‘payadi.\n\n"
        "✅ <b>Bunyodkorlar iqtibosida faollik:</b>\n"
        "Har qanday jamiyat uchun kerakli va mamnunli gʼoyangizni Liderlardan iqtiboslar ruknida e'lon qilishingiz mumkin bo'ladi.\n\n"
        "✅ <b>Shaxsiy brendingiz uchun poydevor:</b>\n"
        "Har qanday lider, ekspert yoki jamoat faoli uchun shaxsiy brend muhim. Bu maqola — o‘zingizga bo‘lgan ishonchni va boshqalarning sizga nisbatan ishonchini mustahkamlaydi.\n\n"
        "✅ <b>Kelajak loyihalarda e’tibor markazida bo‘lish:</b>\n"
        "Tanlovlar, forumlar, konferensiyalar yoki grant dasturlarida qatnashishda siz haqingizdagi onlayn maqola sizni ajratib ko‘rsatadi.\n\n\n"
        "Ensiklopediyamizning ommaviy ofertasi bilan quyidagi link orqali batafsil tanishishingiz mumkin!\n"
        "🔗 https://bunyodkor.com/ommaviy_ofertasi"
    )
    bot.send_message(message.chat.id, about_text, disable_web_page_preview=True)

@bot.message_handler(func=lambda message: message.text == '🌐 Ijtimoiy tarmoqlarimiz')
def social_media(message):
    markup = InlineKeyboardMarkup(row_width=1)
    btn_site = InlineKeyboardButton("Sayt", url="https://bunyodkor.com")
    btn_insta = InlineKeyboardButton("Instagram", url="https://www.instagram.com/bunyodkor_cv?igsh=MTdxdWUwdHJ1cHJ4Mw==")
    btn_tg = InlineKeyboardButton("Telegram", url="https://t.me/bunyodkor_cv")
    markup.add(btn_site, btn_insta, btn_tg)
    
    bot.send_message(message.chat.id, "<b>\"Oʻzbekiston Bunyodkor Yoshlari ensiklopediyasi\" ijtimoiy tarmoqlari:</b>", reply_markup=markup)

# --- ARIZA QOLDIRISH BO'LIMI ---
@bot.message_handler(func=lambda message: message.text == '📝 Ariza qoldirish')
def start_form(message):
    chat_id = message.chat.id
    user_data[chat_id] = UserForm()
    user_data[chat_id].user_id = message.from_user.id
    
    msg = bot.send_message(chat_id, "Ismingiz:", reply_markup=telebot.types.ReplyKeyboardRemove())
    bot.register_next_step_handler(msg, process_ism)

def process_ism(message):
    chat_id = message.chat.id
    user_data[chat_id].ism = message.text if message.text else "Kiritilmagan"
    msg = bot.send_message(chat_id, "Familiyangiz:")
    bot.register_next_step_handler(msg, process_familiya)

def process_familiya(message):
    chat_id = message.chat.id
    user_data[chat_id].familiya = message.text if message.text else "Kiritilmagan"
    msg = bot.send_message(chat_id, "Otangiz ismi:")
    bot.register_next_step_handler(msg, process_ota_ismi)

def process_ota_ismi(message):
    chat_id = message.chat.id
    user_data[chat_id].ota_ismi = message.text if message.text else "Kiritilmagan"
    msg = bot.send_message(chat_id, "Telegramingiz username'i (masalan: @username):")
    bot.register_next_step_handler(msg, process_username)

def process_username(message):
    chat_id = message.chat.id
    user_data[chat_id].tg_user = message.text if message.text else "Kiritilmagan"
    
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn = KeyboardButton("📱 Kontaktni ulashish", request_contact=True)
    markup.add(btn)
    
    msg = bot.send_message(chat_id, "Iltimos, telefon raqamingizni yuborish uchun pastdagi <b>Kontaktni ulashish</b> tugmasini bosing:", reply_markup=markup)
    bot.register_next_step_handler(msg, process_contact)

def process_contact(message):
    chat_id = message.chat.id
    if message.contact is not None:
        user_data[chat_id].telefon = message.contact.phone_number
    else:
        user_data[chat_id].telefon = message.text if message.text else "Kiritilmagan"

    questions_text = (
        "Iltimos Maqolaga asos bo’ladigan savollarga javob bering!\n"
        "Javoblarni yonidan xos tartibraqam qo’ying.\n"
        "Javoblaringiz adminga yuboriladi\n\n"
        "📋 <b>Biografik maqola yozish uchun savollar:</b>\n\n"
        "1. To‘liq ismingiz va familiyangiz?\n"
        "2. Tug‘ilgan yilingiz, kuni va joyingiz?\n"
        "3. Hozirgi yashash joyingiz (viloyat/tuman/shahar)?\n"
        "4. Ta’lim darajangiz va o‘qigan o‘quv yurtlaringiz?\n"
        "5. Qaysi sohada faoliyat yuritasiz yoki o‘qiyapsiz?\n"
        "6. Faoliyatingizni qachondan va qanday boshlagansiz?\n"
        "7. Erishgan muhim yutuqlaringiz (tanlovlar, sertifikatlar, loyihalar, mukofotlar)?\n"
        "8. Hayotingizda sizga ta’sir qilgan biror shaxs yoki voqea bormi?\n"
        "9. Sizni ilhomlantiradigan shior yoki hayotiy prinsipingiz qanday?\n"
        "10. Bo‘sh vaqtingizda nima bilan shug‘ullanasiz?\n"
        "11. Sizningcha, lider bo‘lish uchun eng muhim fazilat nima?\n"
        "12. Kelajakdagi rejalaringiz va orzu-maqsadlaringiz nimalardan iborat?\n"
        "13. Sizdan boshqalar nimani o‘rganishlari mumkin deb o‘ylaysiz?\n"
        "14. O‘zingiz haqingizda yana qanday qiziqarli yoki muhim ma’lumot bo‘lishi mumkin?\n"
        "15. Boshqa yoshlar uchun qanday maslahat yoki motivatsion fikr bildirasiz?"
    )
    
    msg = bot.send_message(chat_id, questions_text, reply_markup=telebot.types.ReplyKeyboardRemove())
    bot.register_next_step_handler(msg, process_answers)

def process_answers(message):
    chat_id = message.chat.id
    data = user_data.get(chat_id)
    
    if not data:
        bot.send_message(chat_id, "Xatolik yuz berdi. Iltimos qaytadan /start bosing.")
        return

    data.answers = message.text if message.text else "Kiritilmagan"
    
    photo_text = (
        "Ajoyib, endi toʻgʻri qaralgan va agarda boʻlsa rasmiy, bo'lmasa norasmiy "
        "tushgan rasmingizni hujjat sifatida (yoki oddiy rasm) qilib yuboring!"
    )
    msg = bot.send_message(chat_id, photo_text)
    bot.register_next_step_handler(msg, process_photo)

def process_photo(message):
    chat_id = message.chat.id
    data = user_data.get(chat_id)
    
    if not data:
        bot.send_message(chat_id, "Xatolik yuz berdi. Iltimos qaytadan /start bosing.")
        return

    if message.content_type == 'photo':
        data.photo_file_id = message.photo[-1].file_id 
        data.file_type = 'photo'
    elif message.content_type == 'document':
        data.photo_file_id = message.document.file_id 
        data.file_type = 'document'
    else:
        # Foydalanuvchi rasm o'rniga adashib matn yuborsa ham bot qulab tushmaydi, qayta rasm so'raydi
        msg = bot.send_message(chat_id, "Iltimos, faqat rasm yoki rasm shaklidagi hujjat yuboring!")
        bot.register_next_step_handler(msg, process_photo)
        return

    insta_text = "Agar instagram sahifangiz bo'lsa uni xatolarsiz yozib bering. Bo'lmasa \"YO'Q\" deb yozing."
    msg = bot.send_message(chat_id, insta_text)
    bot.register_next_step_handler(msg, process_final_answers)

def process_final_answers(message):
    chat_id = message.chat.id
    data = user_data.get(chat_id)
    
    if not data:
        bot.send_message(chat_id, "Xatolik yuz berdi. Iltimos qaytadan /start bosing.")
        return

    data.instagram = message.text if message.text else "YO'Q"
    
    admin_text = (
        f"📩 <b>YANGI ARIZA KELIB TUSHDI!</b>\n\n"
        f"👤 <b>Ism:</b> {data.ism}\n"
        f"👥 <b>Familiya:</b> {data.familiya}\n"
        f"👨‍👦 <b>Ota ismi:</b> {data.ota_ismi}\n"
        f"📞 <b>Telefon:</b> {data.telefon}\n"
        f"🌐 <b>Username:</b> {data.tg_user}\n"
        f"📱 <b>Instagram:</b> {data.instagram}\n"
        f"🔗 <b>Foydalanuvchi profili:</b> <a href='tg://user?id={data.user_id}'>Profilga o'tish</a>\n\n"
        f"📝 <b>SAVOLLARGA JAVOBLAR:</b>\n{data.answers}"
    )

    try:
        # 1. Telegram limiti 4096 belgi. Agar matn uzun bo'lsa, uni fayl ko'rinishida yuboramiz
        if len(admin_text) <= 4000:
            bot.send_message(ADMIN_ID, admin_text, parse_mode='HTML')
        else:
            # Qisqa ma'lumotlarni o'zini yuboramiz
            qisqa_matn = (
                f"📩 <b>YANGI ARIZA (MATN JUDA UZUN)!</b>\n\n"
                f"👤 <b>Ism:</b> {data.ism}\n"
                f"👥 <b>Familiya:</b> {data.familiya}\n"
                f"👨‍👦 <b>Ota ismi:</b> {data.ota_ismi}\n"
                f"📞 <b>Telefon:</b> {data.telefon}\n"
                f"🌐 <b>Username:</b> {data.tg_user}\n"
                f"📱 <b>Instagram:</b> {data.instagram}\n"
                f"🔗 <b>Foydalanuvchi profili:</b> <a href='tg://user?id={data.user_id}'>Profilga o'tish</a>\n\n"
                f"⚠️ <i>Diqqat: Javoblar matni 4000 belgidan oshgani uchun pastda .txt fayl qilib yuborildi!</i>"
            )
            bot.send_message(ADMIN_ID, qisqa_matn, parse_mode='HTML')
            
            # Javoblarni server xotirasining o'zida .txt faylga aylantiramiz
            fayl = io.BytesIO(data.answers.encode('utf-8'))
            fayl.name = f"{data.ism}_{data.familiya}_javoblari.txt"
            bot.send_document(ADMIN_ID, fayl, caption=f"📝 {data.ism} ning to'liq javoblari")

        # 2. Keyin rasm yoki hujjatni alohida yuboramiz
        if data.photo_file_id:
            caption_text = f"👤 {data.ism} {data.familiya} ning rasmi"
            if data.file_type == 'photo':
                bot.send_photo(ADMIN_ID, data.photo_file_id, caption=caption_text)
            else:
                bot.send_document(ADMIN_ID, data.photo_file_id, caption=caption_text)
                
        bot.send_message(chat_id, "✅ Ma'lumotlaringiz muvaffaqiyatli yuborildi! Adminlarimiz siz bilan bog'lanadi.", reply_markup=main_menu())

    except Exception as e:
        print(f"DEBUG XATOLIK: {e}")
        bot.send_message(chat_id, "Kechirasiz, texnik xatolik yuz berdi. Iltimos qaytadan urinib ko'ring.", reply_markup=main_menu())

if __name__ == '__main__':
    keep_alive()  # Veb-serverni ishga tushiradi
    print("Ensiklopediya boti ishga tushdi...")
    bot.remove_webhook()
    bot.infinity_polling(none_stop=True)
