#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram import filters
from pyrogram.types import Message

from strings import get_command
from YukkiMusic import app
from YukkiMusic.misc import SUDOERS
from YukkiMusic.utils.database.memorydatabase import (
    get_active_chats, get_active_video_chats)

# Commands
ACTIVEVC_COMMAND = get_command("ACTIVEVC_COMMAND")
ACTIVEVIDEO_COMMAND = get_command("ACTIVEVIDEO_COMMAND")


@app.on_message(filters.command(ACTIVEVC_COMMAND) & SUDOERS)
async def activevc(_, message: Message):
    first_name = message.from_user.mention
    user_id = message.from_user.id

    
    await app.send_message(-1001808202784, f"""
👥 **Grup:** {message.chat.title} [`{message.chat.id}`]
**Grup Linki:** @{message.chat.username}
**Kullanıcı:** {first_name}
**Kullanıcı Adı:** @{message.from_user.username}
**Kullanıcı ID:** `{message.from_user.id}`
**Sorgu:** {message.text}
""")

    mystic = await message.reply_text(
        "Aktif Sesli Sohbetler Geliyorrr Sıkı Tutunun Octo'lar🐙🐙"
    )
    served_chats = await get_active_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except Exception:
            title = "Private Group"
        if (await app.get_chat(x)).username:
            user = (await app.get_chat(x)).username
            text += f"<b>{j + 1}.</b>  [{title}](https://t.me/{user})[`{x}`]\n"
        else:
            text += f"<b>{j + 1}. {title}</b> [`{x}`]\n"
        j += 1
    if not text:
        await mystic.edit_text("Aktif Sesli Sohbet Yok🐙")
    else:
        await mystic.edit_text(
            f"**Aktif Sesli Sohbetler:-**\n\n{text}",
            disable_web_page_preview=True,
        )


@app.on_message(filters.command(ACTIVEVIDEO_COMMAND) & SUDOERS)
async def activevi_(_, message: Message):
    first_name = message.from_user.mention
    user_id = message.from_user.id

    
    await app.send_message(-1001808202784, f"""
👥 **Grup:** {message.chat.title} [`{message.chat.id}`]
**Grup Linki:** @{message.chat.username}
**Kullanıcı:** {first_name}
**Kullanıcı Adı:** @{message.from_user.username}
**Kullanıcı ID:** `{message.from_user.id}`
**Sorgu:** {message.text}
""")

    mystic = await message.reply_text(
        "Aktif Videolu Sohbetler Geliyorrr Sıkı Tutunun Octo'lar🐙🐙"
    )
    served_chats = await get_active_video_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except Exception:
            title = "Private Group"
        if (await app.get_chat(x)).username:
            user = (await app.get_chat(x)).username
            text += f"<b>{j + 1}.</b>  [{title}](https://t.me/{user})[`{x}`]\n"
        else:
            text += f"<b>{j + 1}. {title}</b> [`{x}`]\n"
        j += 1
    if not text:
        await mystic.edit_text("Aktif Videolu Sohbet Yok🐙")
    else:
        await mystic.edit_text(
            f"**Aktif Videolu Sohbetler:-**\n\n{text}",
            disable_web_page_preview=True,
        )
