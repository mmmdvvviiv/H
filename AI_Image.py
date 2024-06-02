
import telebot,requests
from telebot import types
T = "7114224334:AAHSEBbKKhOvYE_DAYb6VfM8FboSy-6czrI"
B = telebot.TeleBot(T)
@B.message_handler(commands=['start'])
def s(m):
    pv = types.ReplyKeyboardMarkup(resize_keyboard=True)
    pv.add(types.KeyboardButton("✓ Create Image"))
    B.send_photo(m.chat.id, "", caption="""
| مرحبًا بك في AI Chat Bot!  | قم بإنشاء صور باستخدام الذكاء الاصطناعي من النص | اضغط على الزر أدناه للبدء:
""", reply_markup=pv)
@B.message_handler(func=lambda message: message.text == "✓ Create Image")
def i_c(message):
    B.send_photo(message.chat.id, "https://t.me/ifuwufuj/25", caption="""
| الرجاء إدخال وصف مختصر للصورة التي تريد إنشاءها، على سبيل المثال: (قطة) اللغة الإنجليزية مدعومة فقط!
""")
@B.message_handler(content_types=['text'])
def c_i(message):
    d = message.text
    api = f'https://aiimage.hellonepdevs.workers.dev/?prompt={d}'
    r = requests.get(api)
    if r.status_code == 200:
        i = r.content
        B.send_photo(message.chat.id, i , caption = """
✅ | Image created successfully!
🌹 | Request ID :- 1678292001
---------------------------
@lIIHII
""")
    else:
        B.send_message(message.chat.id, """
❌ | Error while creating the image. Please enter a clear and understandable description.
""")
B.infinity_polling()
"""

Ch :- @lIIHII
In :- 2024/5/26

"""