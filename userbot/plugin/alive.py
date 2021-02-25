"""Check if userbot alive. If you change these, you become the gayest gay🤤🤤 such that even the gay world will disown you."""
#IMG CREDITS: @arcuseop ❤👀
import asyncio
from telethon import events
from uniborg.util import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "𝙏𝙀𝙉𝙕𝙊𝙄𝘿×"
PM_IMG = "https://telegra.ph/file/484659c6617acbebc31b0.jpg"
pm_caption = "**𝙏𝙀𝙉𝙕𝙊𝙄𝘿**\n\n"
pm_caption += "**HELLO THERE IM ALIVE 👀❤ ALL MY FUNCTION ARE WORKING FINEE DONT WORRY*\n\n"
pm_caption += "ABOUT MAH SYSTEM 😌 ×͜×\n\n"
pm_caption += "➾ **Telethon Version** : 6.0.9\n➾ **Python** : 3.7.4\n"
pm_caption += "➾ **DataBase** : Functioning\n"
pm_caption += "➾ **Bot owner* : [ARCUSE]()\n"
pm_caption += "➾ *TENZOID VERSION* : 2.0\n\n"
pm_caption += f"➾ **Mah Master😌** : {DEFAULTUSER}\n"
#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()
