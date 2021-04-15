import telebot
import sqlite3

list_hello = ("Привет", "Здравствуй", "Hello")

bot = telebot.TeleBot("1629080631:AAGJUScNV0kLMcLoges2Frj1xJRhSG6pHzk", parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXIST users(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        id INTEGER,
        first_name VARCHAR(20),
        last_name VARCHAR(20),
        )''')
    
    connect.commit()
    # check id in fields
    people_id = message.chat.id
    cursor.execute(f'SELECT id FROM users WHERE id = {people_id}')
    data = cursor.fetchone()
    if data is None:
        # add values in field
        users_list = [message.chat.id]
        cursor.execute('INSERT INTO users VALUES(?);', user_list)
        connect.commit()
        bot.reply_to(message, "Я пока ничего не умею?")
    else:
        bot_send.message(message.chat.id, 'This user was added')
@bot.message_handler(func=lambda message: True)
def answer_to_message(message):
    print(message.from_user.id)
    if message.text in list_hello:
        bot.send_message(message.from_user.id, "И тебе привет!")
bot.polling()
