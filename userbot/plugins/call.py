"""Emoji

Available Commands:

.emoji shrug

.emoji apple

.emoji :/

.emoji -_-"""

from telethon import events

import asyncio
from userbot.utils import admin_cmd




@borg.on(admin_cmd(pattern=r"call"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 18)

   # input_str = event.pattern_match.group(1)

   # if input_str == "call":

    await event.edit("Calling")

    animation_chars = [
        
            "`Connecting To Rashtrapati bhavan`",
            "`Call Connected.`",
            "`Bhawan: Hello This is Rashtrapati bhavan HQ . Who is this?`",
            "`Me: Yo this is` [THUG USER](t.me/THUGUSERBOT) ,`Please Connect me to MODI G`",
            "`User Authorised.`",
            "`Calling`  `At +916969696969`",
            "`Private  Call Connected...`",
            "`Me: Hello MODI G, Please Ban XNXX2.`",    
            "`MODI : May I Know Who Is This?`",
            "`Me: Yo I AM THUGBOT USER`  ",
            "`MODI: OMG!!! THUGBOT USER NYC TO MEET YOU I WILL MAKE SURE I BAN XNXX2.`",
            "`Me: Thanks, SEE YOU LATER.`",
            "`MODI: AARE THANKS KI ZARURAT NAHI HAI THUGSBOT WALE SABHI BHAI HAI MERE.`",
            "`Me: YEP TNX AGAIN  \nTC Bye Bye :)`",
            "`Private Call Disconnected`"
        ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 18])
