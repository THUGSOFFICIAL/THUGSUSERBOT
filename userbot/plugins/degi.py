"""Fun pligon...for DC
\nCode by DC , ©[Kraken_The_Badass](https://t.me/kraken_the_badass)
type `.degi` and `.nehi` to see the fun.
"""
import random, re
from uniborg.util import admin_cmd
import asyncio
from telethon import events

@borg.on(admin_cmd(pattern="degi ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("**Khud**")
        await asyncio.sleep(0.9)
        await event.edit("**ka**")
        await asyncio.sleep(1)
        await event.edit("**Land**")
        await asyncio.sleep(0.9)
        await event.edit("**hai**")
        await asyncio.sleep(0.9)
        await event.edit("**kala phir**")
        await asyncio.sleep(1)
        await event.edit("**bhi gulabhi ch_t** ")
        await asyncio.sleep(0.8)
        await event.edit("**maangta hai**")
        await asyncio.sleep(0.7)
        await event.edit("**Bossdiwala**")
        await asyncio.sleep(1)
        await event.edit("**Khud ka Land hai kaala phir bhi gulabi chu_ maangta bossdiwala**")

@borg.on(events.NewMessage(pattern=r"\.nehi", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("**Try kar kya pata de hi dede 🤨**")
    await asyncio.sleep(999)
