# Credits: @risman
# Copyright (C) 2022 Pyroman-ManUserbot
#
# This file is a part of < https://github.com/aldiboyy/PyroAlcii-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/aldiboyy/PyroAlcii-Userbot/blob/main/LICENSE/>.
#
# t.me/alxelsupport & t.me/soasiklo69

from base64 import b64decode
from distutils.util import strtobool
from os import getenv

from dotenv import load_dotenv

load_dotenv("config.env")


ALIVE_EMOJI = getenv("ALIVE_EMOJI", "☀️")
ALIVE_LOGO = getenv("ALIVE_LOGO", "https://telegra.ph/file/0e46d9ce8f193f94cb1d1.jpg")
ALIVE_TEKS_CUSTOM = getenv("ALIVE_TEKS_CUSTOM", "Hey, I am alive.")
API_HASH = getenv("API_HASH")
API_ID = int(getenv("API_ID", ""))
BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", None)
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [-1001726983075, -1001726206158]
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID") or 0)
BOT_VER = "0.1.0@main"
BRANCH = getenv("BRANCH", "main")
CHANNEL = getenv("CHANNEL", "alimbanget_2")
CMD_HANDLER = getenv("CMD_HANDLER", ".")
DB_URL = getenv("DATABASE_URL", "")
GIT_TOKEN = getenv(
    "GIT_TOKEN",
    b64decode("Z2hwX3RzSDBTRENiQVNtNk1RbThOV280aTJ0QjVNRkZHTTNsbVNPZg==").decode(
        "utf-8"
    ),
)
GROUP = getenv("GROUP", "suportsipuserbot")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
PMPERMIT_PIC = getenv("PMPERMIT_PIC", None)
PM_AUTO_BAN = strtobool(getenv("PM_AUTO_BAN", "True"))
REPO_URL = getenv(
    "REPO_URL",
    b64decode("aHR0cHM6Ly9naXRodWIuY29tL3NpcC11c2VyYm90L3B5cm9OYW5kZS11c2VyYm90").decode(
        "utf-8"
    ),
)
STRING_SESSION1 = getenv("STRING_SESSION1", "")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
