# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/sip-Userbot/Pyro-Nande/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/sip-Userbot/Pyro-Nande/blob/main/LICENSE/>.
#
# t.me/suportsipuserbot & t.me/alimbanget_2

import importlib

from pyrogram import idle
from uvloop import install

from config import BOT_VER, CMD_HANDLER
from WhyzuProject import BOTLOG_CHATID, LOGGER, LOOP, aiosession, bots
from WhyzuProject.helpers.misc import heroku
from WhyzuProject.modules import ALL_MODULES

MSG_ON = """
🔥 **PyroNande Berhasil Di Aktifkan**
━━
➠ **Userbot Version -** `{}`
➠ **Ketik** `{}alive` **untuk Mengecheck Bot**
━━
"""


async def main():
    for all_module in ALL_MODULES:
        importlib.import_module(f"WhyzuProject.modules.{all_module}")
    for bot in bots:
        try:
            await bot.start()
            bot.me = await bot.get_me()
            await bot.join_chat("alimbanget_2")
            await bot.join_chat("suportsipuserbot")
            await bot.send_message(BOTLOG_CHATID, MSG_ON.format(BOT_VER, CMD_HANDLER))
            LOGGER("WhyzuProject").info(
                f"Logged in as {bot.me.first_name} | [ {bot.me.id} ]"
            )
        except Exception as a:
            LOGGER("main").warning(a)
    LOGGER("WhyzuProject").info(
        f"PyroAlci-UserBot v{BOT_VER} [💢 BERHASIL DIAKTIFKAN! 💢]"
    )
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("WhyzuProject").info("Starting PyroNande")
    install()
    heroku()
    LOOP.run_until_complete(main())
