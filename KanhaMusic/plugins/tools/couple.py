# -----------------------------------------------
# 🔸 KanhaMusic Project
# 🔹 Developed & Maintained by: Anu Bots (https://github.com/TEAM-KANHA-OP)
# 📅 Copyright © 2025 – All Rights Reserved
#
# 📖 License:
# This source code is open for educational and non-commercial use ONLY.
# You are required to retain this credit in all copies or substantial portions of this file.
# Commercial use, redistribution, or removal of this notice is strictly prohibited
# without prior written permission from the author.
#
# ❤️ Made with dedication and love by TEAM-KANHA-OP
# -----------------------------------------------

import random
from datetime import datetime, timedelta

from pyrogram import errors, filters
from pyrogram.enums import ChatType
from pyrogram.types import Message

from KanhaMusic import app
from KanhaMusic.mongo.couples_db import get_couple, save_couple


# 🔥 YOUR CUSTOM IMAGE LINK HERE
COUPLE_IMG = "https://i.ibb.co/Mk5MnbRY/x.jpg"


def today() -> str:
    return datetime.now().strftime("%d/%m/%Y")


def tomorrow() -> str:
    return (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")


async def safe_get_user(uid: int):
    try:
        return await app.get_users(uid)
    except errors.PeerIdInvalid:
        return None


@app.on_message(filters.command("couple"))
async def couples_handler(_, message: Message):
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("**ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴡᴏʀᴋs ɪɴ ɢʀᴏᴜᴘs.**")

    wait = await message.reply("🦋")
    cid = message.chat.id
    date = today()

    record = await get_couple(cid, date)
    if record:
        uid1, uid2 = record["user1"], record["user2"]
        user1 = await safe_get_user(uid1)
        user2 = await safe_get_user(uid2)

        if not (user1 and user2):
            record = None

    if not record:
        members = [
            m.user.id async for m in app.get_chat_members(cid, limit=250)
            if not m.user.is_bot
        ]

        if len(members) < 2:
            await wait.edit("**ɴᴏᴛ ᴇɴᴏᴜɢʜ ᴜsᴇʀs ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ.**")
            return

        tries = 0
        while tries < 5:
            uid1, uid2 = random.sample(members, 2)
            user1 = await safe_get_user(uid1)
            user2 = await safe_get_user(uid2)
            if user1 and user2:
                break
            tries += 1
        else:
            await wait.edit("**ᴄᴏᴜʟᴅ ɴᴏᴛ ꜰɪɴᴅ ᴠᴀʟɪᴅ ᴍᴇᴍʙᴇʀꜱ.**")
            return

        await save_couple(cid, date, {"user1": uid1, "user2": uid2})

    caption = (
        "💌 **ᴄᴏᴜᴘʟᴇ ᴏꜰ ᴛʜᴇ ᴅᴀʏ!** 💗\n\n"
        "╔═══✿═══❀═══✿═══╗\n"
        f"💌 **ᴛᴏᴅᴀʏ'ꜱ ᴄᴏᴜᴘʟᴇ:**\n⤷ {user1.mention} 💞 {user2.mention}\n"
        "╚═══✿═══❀═══✿═══╝\n\n"
        f"📅 **ɴᴇxᴛ ꜱᴇʟᴇᴄᴛɪᴏɴ:** `{tomorrow()}`\n\n"
        "💗 **ᴛᴀɢ ʏᴏᴜʀ ᴄʀᴜꜱʜ — ʏᴏᴜ ᴍɪɢʜᴛ ʙᴇ ɴᴇxᴛ!** 😉"
    )

    await message.reply_photo(COUPLE_IMG, caption=caption)
    await wait.delete()
