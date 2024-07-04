import re
import os
import logging
from os import getenv, environ
from logging.handlers import RotatingFileHandler

shortner_url = os.environ.get("SHORTENER_SITE", "easysky.in")
shortner_api = os.environ.get("SHORTENER_API", "e122c6f2d28d6e79ac214cb118700a2619131c39")

# Get This Details From My telegram.org And From The @BotFather
APP_ID = int(os.environ.get("APP_ID", "21821499"))
API_HASH = os.environ.get("API_HASH", "31eda964c848701b76931b1a5446f301")
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7147069232:AAGqijmAeCxionrLzaCMS3WJhrWrKU0eKqY")

# channels infomation
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002181649999"))
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002248503876"))
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002017829366"))
REQUEST_CHANNEL = int(os.environ.get("REQUEST_CHANNEL", "-1002165483636"))
REQUEST_CHANNEL2 = int(os.environ.get("REQUEST_CHANNEL2", "-1002171731524"))

# The Users Id Whoe Control Your Bot And Manage It For Further
OWNER_ID = int(os.environ.get("OWNER_ID", "5333053497"))
ADMINS = int(os.environ.get("ADMINS", "5333053497"))

# This Is Where It Controls All Here You Can Add The Database Url And Name At The Same Time
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://titanfilter1:titan@cluster0.obul3jl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_URI2 = os.environ.get("DATABASE_URL2", "mongodb+srv://titanfilter1:titan@cluster0.jk3vouh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
tempDict = {'indexDB': DB_URI2}
COLLECTION_NAME = 'filestore_ind'
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

# kind of important
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "📌 ᴍᴀɴᴛᴀɪɴᴇᴅ ʙʏ : @Titan_CInemas")
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", "False") == 'True'
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
PICS = os.environ.get('PICS', 'https://telegra.ph/file/c8fe690794fa983af828c.jpg').split() #
RSTART = os.environ.get('RSTART', 'https://te.legra.ph/file/d301eb1eac43a66390f91.jpg')
BOT_USERS = os.environ.get('BOT_USERS', 'https://te.legra.ph/file/81bd8053e505e45bdfe8f.jpg')
PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "500"))

INCOMING_TXT = os.environ.get("INCOMING_TXT", """ʜᴇʏ ʙʜᴀɪ {first} 💞

<blockquote> ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴ ʀᴇǫᴜᴇsᴛ ᴜsᴇ ᴛʜᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴊᴏɪɴ ᴛʜᴇ ᴄʜᴀᴛ ᴀɴᴅ sᴇɴᴅ ᴛʜᴇ ɴᴀᴍᴇ ʙᴜᴛ ᴜsᴇ ᴀ ғᴏʀᴍᴀᴛᴇ</blockquote>

<code>/request Your_movie_name/series_name</code>""")

# start Message And Texts
START_MSG = os.environ.get("START_MESSAGE", """🚀 ʜᴇʟʟᴏ ʙʜᴀɪ!!! {first}

💞 ɪ ᴀᴍ ᴀ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ ᴡʜᴏ ᴄᴀɴ sᴛᴏʀᴇ ғɪʟᴇs ᴀɴᴅ ɢɪᴠᴇ ᴄᴜsᴛᴏᴍ ʟɪɴᴋs ᴏɴʟʏ ᴀᴅᴍɪɴs ᴏғ ᴛʜᴇ ʙᴏᴛ ᴄᴀɴ ᴜsᴇ ʙᴇ sᴏ ᴅᴏɴᴛ sᴘᴀᴍ ;)""")

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", """
<b>ʜᴇʟʟᴏ ʙʜᴀɪ {first} 💞</b>

<b>📌 ᴇɴɢʟɪsʜ :
ʙʜᴀɪ ʏᴏᴜʀ ɴᴇᴇᴅ ᴛᴏ ᴊᴏɪɴ this ᴄʜᴀɴɴᴇʟ ɪɴ ᴏʀᴅᴇʀ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ғɪʟᴇs/ʟɪɴᴋs ɪᴛs ɴᴇᴇᴅᴇᴅ sᴏ ᴘʟs ᴊᴏɪɴ !!</b>"

<b>📌 ʜɪɴᴅɪ : 
हम उन सभी लोगों के लिए हैं जो अपने जीवन में कई बार/सभी अवसरों पर एक दूसरे के पूरक हैं !!!</b>""")

HELP_MSG = os.environ.get("HELP_MSG", """
ʜᴇʟʟᴏ ʙʜᴀɪ 💞 {first_name}, ᴋɪsᴇ ʜᴏ

⚡ ʏᴏᴜʀ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ⚡

🚀 ғɪʀsᴛ ɴᴀᴍᴇ - <code>{first_name}</code>
🚀 ʟᴀsᴛ ɴᴀᴍᴇ - <code>{last_name}</code>
🚀 ʏᴏᴜʀ ɪᴅ - <code>{user_id}</code>
🚀 ᴜsᴇʀɴᴀᴍᴇ - <code>{username}</code>

sᴏʀʀʏ ᴛᴏ ʜᴇʀᴇ ʜᴀᴍᴀʀᴇ ʙᴏᴛ ᴘᴇ ᴀᴘᴘ ᴋᴏ ᴘʀᴏʙʟᴇᴍ ʜᴜᴀ ᴘʟs ɴᴇᴄʜᴇ ᴅɪʏᴀ ɢᴀʏᴇ ʙᴜᴛᴛᴏɴs ᴋᴏ ᴄʟɪᴄᴋ ᴋᴀʀᴏ ᴀɴᴅ ᴠɪᴅᴇᴏs ᴋᴏ ᴅᴇᴋᴋᴏ ᴀɢᴀʀ ᴘʀᴏʙʟᴇᴍ sᴏʟᴠᴇ ɴᴇʜɪ ʜᴜᴀ ᴛʜᴏ ᴘʟs ɴᴇᴇᴄʜᴇ ᴄᴏɴᴛᴀᴄᴛ ʙᴜᴛᴛᴏɴ ᴄʟɪᴄᴋ ᴋᴀʀ ᴋᴇ ᴍᴇssᴀɢᴇ ᴋᴀʀᴏ ʜᴀᴀᴍ ᴋᴏ ʜᴀᴀᴍ sʟᴏᴠᴇ ᴋᴀʀ ɴᴇ ᴋᴀ ᴛʀʏ ᴋᴀʀɢᴇᴇ

<blockquote>🎉 ɴᴏᴛᴇ - ʜᴀ ʙʜᴀɪ ᴘᴀᴛʜᴀ ʜᴀɪ ᴛᴜᴍ ᴋᴏ ᴅʀᴀᴍᴀ ᴅᴇᴋᴋ ɴᴇ ᴍᴀɪ ᴘʀᴏʙʟᴇᴍ ʜᴏ ʀᴀʜᴀ ʜᴀɪ ᴍᴇssᴀɢᴇ ᴋᴀʀᴏ ᴀɴᴅ ᴡᴀɪᴛ ғᴏʀ ʀᴇᴘʟʏ ᴅᴏɴᴛ sᴘᴀᴍ sᴘᴀᴍ ᴋɪʏᴀ ᴅᴍ ᴍᴀɪ ᴛʜᴏ ʙᴏʟ ʜᴏᴊᴀʏᴇɢᴀ ᴛʜᴜ ɪᴛs ʏᴏᴜʀ ᴡɪsʜ ᴀғᴛᴇᴛ ᴛʜᴀᴛ</blockquote>""")
disable_web_page_prewiew = True

try:
    ADMINS = []
    for x in (os.environ.get("ADMINS", "6405622540").split()):
        ADMINS.append(int(x))
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)

logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
