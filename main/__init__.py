#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 27533097
API_HASH = "cff830d74afa4220f22817cfd8ca1c84"
BOT_TOKEN = "8595460064:AAGnMQRy2yq50ADto5ZFvUaJhD0tw3Lf8Pc"
SESSION = "BQA-i3IAGH11_V7gZbotExywKvyU_iIXJKV2aI19lhkaHfCrKOjYmvV6OadIrvJphfXS7Bw4Lm7u_OjJ9xYHGz3CwEjxPOApYm8k23cc2XxUj2VBS52FYYGYTLegDbwxRRIT1NB8ScVfyO6HKUAZhoZNQ6HJzZADSCpOc8wm5cb90b_6UYiWz0Vrk7d0IUYHChdtb9o_NRCQJJq7Zk4S2kYPWILOwU9kb1jn4vFfoNlJGcjGkPRBMQ3CF1NbTIZvci4iYUU8mXwQ8Ing_kGc3cb2IUaU81x0MHZwrZ0kS5WkNtE-Z8j-X3CeOYp81J3SDn8IRQuYoT5qsQwZ5uZzHN_0zmdmOgAAAAHQSfNBAA"
FORCESUB = "Publicationo"
AUTH = 8189885323

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
