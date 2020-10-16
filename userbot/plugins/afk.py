# by uniborg...Thanks @spechide 
# Now will be used in THUGBOT too....
"""Syntax: .afk REASON"""
import asyncio
import datetime
from datetime import datetime

from telethon import events
from telethon.tl import functions, types

from userbot import CMD_HELP
from userbot.utils import admin_cmd

global USER_AFK  # pylint:disable=E0602
global afk_time  # pylint:disable=E0602
global last_afk_message  # pylint:disable=E0602
global afk_start
global afk_end
USER_AFK = {}
afk_time = None
last_afk_message = {}
afk_start = {}


@borg.on(events.NewMessage(outgoing=True))  # pylint:disable=E0602
async def set_not_afk(event):
    global USER_AFK  # pylint:disable=E0602
    global afk_time  # pylint:disable=E0602
    global last_afk_message  # pylint:disable=E0602
    global afk_start
    global afk_end
    back_alive = datetime.now()
    afk_end = back_alive.replace(microsecond=0)
    if afk_start != {}:
        total_afk_time = str((afk_end - afk_start))
    current_message = event.message.message
    if ".afk" not in current_message and "yes" in USER_AFK:  # pylint:disable=E0602
        shite = await borg.send_message(
            event.chat_id,
            "__Back alive!__\n**No Longer afk.**\n `Was afk for:``"
            + total_afk_time
            + "`",
        )
        try:
            await borg.send_message(  # pylint:disable=E0602
                Config.PRIVATE_GROUP_BOT_API_ID,  # pylint:disable=E0602
                "#AFKFALSE \nSet AFK mode to False\n"
                + "__Back alive!__\n**No Longer afk.**\n `Was afk for:``"
                + total_afk_time
                + "`",
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            await borg.send_message(  # pylint:disable=E0602
                event.chat_id,
                "Please set `PRIVATE_GROUP_BOT_API_ID` "
                + "for the proper functioning of afk functionality "
                + "Ask In support grp 👉👉👉[SUPPORT](https://t.me//THUGUSERBOTHELPChat)👈👈👈 grp to get help..\n\n `{}`".format(str(e)),
                reply_to=event.message.id,
                silent=True,
            )
        await asyncio.sleep(5)
        await shite.delete()
        USER_AFK = {}  # pylint:disable=E0602
        afk_time = None  # pylint:disable=E0602


@borg.on(
    events.NewMessage(  # pylint:disable=E0602
        incoming=True, func=lambda e: bool(e.mentioned or e.is_private)
    )
)
async def on_afk(event):
    if event.fwd_from:
        return
    global USER_AFK  # pylint:disable=E0602
    global afk_time  # pylint:disable=E0602
    global last_afk_message  # pylint:disable=E0602
    global afk_start
    global afk_end
    back_alivee = datetime.now()
    afk_end = back_alivee.replace(microsecond=0)
    if afk_start != {}:
        total_afk_time = str((afk_end - afk_start))
    current_message_text = event.message.message.lower()
    if "afk" in current_message_text:
        # userbot's should not reply to other userbot's
        # https://core.telegram.org/bots/faq#why-doesn-39t-my-bot-see-messages-from-other-bots
        return False
    if USER_AFK and not (await event.get_sender()).bot:  # pylint:disable=E0602
        #   if afk_time:  # pylint:disable=E0602
        #      now = datetime.datetime.now()
        #     datime_since_afk = now - afk_time  # pylint:disable=E0602
        #    time = float(datime_since_afk.seconds)
        #   days = time // (24 * 3600)
        #  time = time % (24 * 3600)
        # hours = time // 3600
        # time %= 3600
        #            minutes = time // 60
        #           time %= 60
        #          seconds = time
        #         if days == 1:
        #            afk_since = "**Yesterday**"
        #       elif days > 1:
        #          if days > 6:
        #             date = now + \
        #                datetime.timedelta(
        #                   days=-days, hours=-hours, minutes=-minutes)
        #          afk_since = date.strftime("%A, %Y %B %m, %H:%I")
        #     else:
        #        wday = now + datetime.timedelta(days=-days)
        #       afk_since = wday.strftime('%A')
        #            elif hours > 1:
        #               afk_since = f"`{int(hours)}h{int(minutes)}m` **ago**"
        #          elif minutes > 0:
        #             afk_since = f"`{int(minutes)}m{int(seconds)}s` **ago**"
        #        else:
        #           afk_since = f"`{int(seconds)}s` **ago**"
        msg = None
        message_to_reply = (
            f"__My मास्टर तब से दूर है__ `{total_afk_time}`\nवह कहाँ है: मैं दोस्त नहीं जानता..वह एक व्यस्त व्यक्ति है "
            + f"\n\n__मैं आपको गारंटी नहीं दे सकता कि वह कब आएगा..__\n**ओह्ह !! उसने एक कारण छोड़ दिया**.🧐: {reason}"
            if reason
            else f"**नमस्ते!**\n__मैं वर्तमान में अनुपलब्ध हूं. कब से, तुम पूछते हो? {total_afk_time} मैं अनुमान.__\n\nमैं कब वापस आऊंगा? जल्द ही __जब भी मेरा मन करे वापस आने का. **नवरात्रि की हार्दिक शुभकामनाएँ**  "
        )
        msg = await event.reply(message_to_reply)
        await asyncio.sleep(5)
        if event.chat_id in last_afk_message:  # pylint:disable=E0602
            await last_afk_message[event.chat_id].delete()  # pylint:disable=E0602
        last_afk_message[event.chat_id] = msg  # pylint:disable=E0602


@borg.on(admin_cmd(pattern=r"अफ ह हू ?(.*)", outgoing=True))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    global USER_AFK  # pylint:disable=E0602
    global afk_time  # pylint:disable=E0602
    global last_afk_message  # pylint:disable=E0602
    global afk_start
    global afk_end
    global reason
    USER_AFK = {}
    afk_time = None
    last_afk_message = {}
    afk_end = {}
    start_1 = datetime.now()
    afk_start = start_1.replace(microsecond=0)
    reason = event.pattern_match.group(1)
    if not USER_AFK:  # pylint:disable=E0602
        last_seen_status = await borg(  # pylint:disable=E0602
            functions.account.GetPrivacyRequest(types.InputPrivacyKeyStatusTimestamp())
        )
        if isinstance(last_seen_status.rules, types.PrivacyValueAllowAll):
            afk_time = datetime.datetime.now()  # pylint:disable=E0602
        USER_AFK = f"yes: {reason}"  # pylint:disable=E0602
        if reason:
            await borg.send_message(
                event.chat_id, f"**I shall be Going afk!** __because ~ {reason}__"
            )
        else:
            await borg.send_message(event.chat_id, f"**I am Going afk!**")
        await asyncio.sleep(5)
        await event.delete()
        try:
            await borg.send_message(  # pylint:disable=E0602
                Config.PRIVATE_GROUP_BOT_API_ID,  # pylint:disable=E0602
                f"#AFKTRUE \nSet AFK mode to True, and Reason is {reason}",
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            logger.warn(str(e))  # pylint:disable=E0602


CMD_HELP.update(
    {
        "afk": "__**PLUGIN NAME :** Afk__\
\n\nðŸ“Œ** CMD âž¥** `.afk` [Optional Reason]\
\n**USAGE   âž¥  **Sets you as afk.\nReplies to anyone who tags/PM's \
you telling them that you are AFK(reason)\n\n__Switches off AFK when you type back anything, anywhere.__\
"
    }
)
