import asyncio
from telethon import events
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Hell User"
PM_IMG = "https://telegra.ph/file/4c7467a0f49659007c60d.mp4"
pm_caption = "🥰🥰**THUGBOT IS ONLINE DUDE** 🥰🥰\n\n"

pm_caption += f"💳💳 **MASTER**💳💳     :   {DEFAULTUSER}\n"

pm_caption += "🙏🙏**SUPPORT**🙏🙏      :   [JOIN](https://t.me/THUGUSERBOT)\n"

pm_caption += "🤖🤖**UPDATES**          :   SOON \n"

pm_caption += "👹👹**SPAM GRP**👹👹     :.  [SPAM](https://t.me/joinchat/UKclkxutUAu1SGLHZ9hdkw)
      
pm_caption += "🗽🗽**MY GOD**🗽🗽       :   [THUGS](https://t.me/THUGS_OFFICIAL)\n"

#@command(outgoing=True, pattern="^.online$")
@borg.on(admin_cmd(pattern=r"online"))
async def amireallyalive(online):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete() 
