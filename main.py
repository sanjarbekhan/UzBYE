import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# Bot tokenini kiriting
TOKEN = '8915114593:AAF2Fu3TU-6IK0vITJ7xIyiSTmfs-0CMa70'
bot = telebot.TeleBot(TOKEN, parse_mode='HTML')

# Adminning telegram username'i (Sizning profilingiz)
# ESKI QISMI:
# ADMIN_USERNAME = '@x_sanjar'

# YANGI QISMI:
ADMIN_ID = 6755433894  # O'z ID raqamingizni shu yerga yozing

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

# Asosiy menyu tugmalari
def main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = KeyboardButton('📝 Ariza qoldirish')
    btn2 = KeyboardButton('🌐 Ijtimoiy tarmoqlarimiz')
    btn3 = KeyboardButton('ℹ️ Biz haqimizda')
    markup.add(btn1)
    markup.add(btn2, btn3)
    return markup

@bot.message_handler(commands=['start'])
def send_welcome(message):
    first_name = message.from_user.first_name
    text = f"Assalomu alaykum <b>{first_name}</b>, \"Oʻzbekiston Bunyodkor Yoshlari ensiklopediyasi\" telegram botiga xush kelibsiz!\n\nIltimos Kerakli boʻlimni tanlang."
    bot.send_message(message.chat.id, text, reply_markup=main_menu())

@bot.message_handler(func=lambda message: message.text == 'ℹ️ Biz haqimizda')
def about_us(message):
    about_text = (
        "Ushbu xabarda sizga qo‘shimcha ma’lumotlarni taqdim etmoqdamiz.\n"
        "Ensiklopediyaga istalgan sohada faoliyat yuritayotgan, o‘z ustida ishlayotgan yoshlar qabul qilinadi.\n"
        "Bu loyiha yoshlarning yutuqlarini hujjatlashtirish, ularni ommaga tanitish va boshqalarga ilhom manbai bo‘lish maqsadida yaratilgan.\n\n"
        "✅ <b>Qidiruv tizimlarida ko‘rinish:</b>\n"
        "Siz haqingizdagi maqola Google, Yandex, Bing kabi qidiruv tizimlarida chiqadi. Bu sizni istagan odam — hamkor, ish beruvchi yoki jurnalist — osongina topishi mumkinligini anglatadi.\n\n"
        "✅ <b>Sun’iy intellekt platformalarida tanilish:</b>\n"
        "ChatGPT, Copilot, Gemini kabi sun’iy intellekt tizimlari endilikda siz haqingizda aniq manbalarga tayangan holda ma’lumot bera oladi. Bu sizning onlayn obro‘yingizni mustahkamlovchi kuchli vosita.\n\n"
        "✅ <b>Kelajakdagi Wikipedia sahifangiz uchun asos:</b>\n"
        "Bugun e’lon qilinadigan maqola — ertaga siz haqingizda yoziladigan Wikipedia sahifasi uchun tayyor ishonchli manba bo‘lishi mumkin.\n\n"
        "✅ <b>Ijtimoiy tarmoqlarda tasdiq belgisi olish imkoniyati:</b>\n"
        "Instagram, Facebook, TikTok, YouTube kabi platformalarda ko‘k nishon olish uchun siz haqingizda onlayn nashrlar zarur. Ushbu maqola bu yo‘lda ishonchli hujjat bo‘lib xizmat qiladi.\n\n"
        "✅ <b>Rezumega qo‘shiladigan rasmiy havola:</b>\n"
        "Ish qidirishda, grantga hujjat topshirishda yoki xalqaro loyihalarda qatnashishda ushbu maqola — sizning shaxsiy brendingizni isbotlovchi kuchli hujjat bo‘ladi.\n\n"
        "✅ <b>Bunyodkor yoshlar online jurnalida yoritilish</b>\n"
        "Biografik maqolasi bor yoshlar Bunyodkor yoshlar online jurnalida mumtazam yoritiladi. Ularning hayotida yuz bergan muhim voqea, ularning loyihalari va tashabburlari keng targ'ib qilinadi.\n\n"
        "✅ <b>Ommaviy axborot vositalari e’tiboriga tushasiz:</b>\n"
        "Jurnalistlar, blogerlar, televideniye va radio uchun maqolaviy manba sifatida sizga murojaatlar ko‘payadi.\n\n"
        "✅ <b>Bunyodkorlar iqtibosida faollik</b>\n"
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
    user_data[chat_id].ism = message.text
    msg = bot.send_message(chat_id, "Familiyangiz:")
    bot.register_next_step_handler(msg, process_familiya)

def process_familiya(message):
    chat_id = message.chat.id
    user_data[chat_id].familiya = message.text
    msg = bot.send_message(chat_id, "Otangiz ismi:")
    bot.register_next_step_handler(msg, process_ota_ismi)

def process_ota_ismi(message):
    chat_id = message.chat.id
    user_data[chat_id].ota_ismi = message.text
    msg = bot.send_message(chat_id, "Telegramingiz username'i (masalan: @username):")
    bot.register_next_step_handler(msg, process_username)

def process_username(message):
    chat_id = message.chat.id
    user_data[chat_id].tg_user = message.text
    
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn = KeyboardButton("📱 Kontaktni ulashish", request_contact=True)
    markup.add(btn)
    
    msg = bot.send_message(chat_id, "Iltimos, telefon raqamingizni yuborish uchun pastdagi <b>Kontaktni ulashish</b> tugmasini bosing:", reply_markup=markup)
    bot.register_next_step_handler(msg, process_contact)

def process_contact(message):
    chat_id = message.chat.id
    # Agar foydalanuvchi tugmani bosib yuborsa kontakt keladi, qo'lda yozsa text keladi
    if message.contact is not None:
        user_data[chat_id].telefon = message.contact.phone_number
    else:
        user_data[chat_id].telefon = message.text

    questions_text = (
        "Iltimos Maqolaga asos bo’ladigan savollarga javob bering!\n"
        "Javoblarni yonidan xos tartibraqam qo’ying.\n"
        "Maqola va brending ishlari uchun to’g’riga qaragan va agar boʻlsa rasmiy, boʻlmasa norasmiy kiyingan rasmingizni yuboring!\n\n"
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
    bot.register_next_step_handler(msg, process_final_answers)

def process_final_answers(message):
    chat_id = message.chat.id
    data = user_data.get(chat_id)
    
    if not data:
        bot.send_message(chat_id, "Xatolik yuz berdi. Iltimos qaytadan /start bosing.")
        return

    # Rasm bilan matn birga yuborilsa tutib olish uchun
    if message.content_type == 'photo':
        answers = message.caption if message.caption else "Faqat rasm yuborildi."
        photo_file_id = message.photo[-1].file_id
    else:
        answers = message.text
        photo_file_id = None

    # Adminga yuboriladigan xabar shabloni
    admin_text = (
        f"📩 <b>YANGI ARIZA KELIB TUSHDI!</b>\n\n"
        f"👤 <b>Ism:</b> {data.ism}\n"
        f"👥 <b>Familiya:</b> {data.familiya}\n"
        f"👨‍👦 <b>Ota ismi:</b> {data.ota_ismi}\n"
        f"📞 <b>Telefon:</b> {data.telefon}\n"
        f"🌐 <b>Username:</b> {data.tg_user}\n"
        f"🔗 <b>Foydalanuvchi profili:</b> <a href='tg://user?id={data.user_id}'>Profilga o'tish</a>\n\n"
        f"📝 <b>SAVOLLARGA JAVOBLAR:</b>\n{answers}"
    )

    try:
        if photo_file_id:
            bot.send_photo(ADMIN_ID, photo_file_id, caption=admin_text)
        else:
            bot.send_message(ADMIN_ID, admin_text)
            
        bot.send_message(chat_id, "✅ Ma'lumotlaringiz muvaffaqiyatli yuborildi! Adminlarimiz siz bilan bog'lanadi.")
        
    except Exception as e:
        # Xatolikni terminalda ko'rish
        print(f"DEBUG XATOLIK: {e}") 
        bot.send_message(chat_id, "Kechirasiz, texnik nosozlik yuz berdi. Iltimos, keyinroq urinib ko'ring.")
        
    except Exception as e:
        bot.send_message(chat_id, "Xatolik yuz berdi! Admin botni bloklagan bo'lishi mumkin. Lekin ma'lumotlaringiz qabul qilindi.", reply_markup=main_menu())
        print(f"Xatolik: {e}")

if __name__ == '__main__':
    print("Ensiklopediya boti ishga tushdi...")
    bot.remove_webhook()
    bot.infinity_polling(none_stop=True)
