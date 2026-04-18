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

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ParseMode
import httpx
from KanhaMusic import app  # ✅ Updated here

TRUTH_API = "https://api.truthordarebot.xyz/v1/truth"
DARE_API = "https://api.truthordarebot.xyz/v1/dare"


async def fetch_question(url: str):
    try:
        async with httpx.AsyncClient(timeout=8.0) as http:
            res = await http.get(url)

        if res.status_code == 200:
            return res.json().get("question", "No question found.")
        else:
            return None

    except Exception as e:
        print(f"API Error: {e}")
        return None


@app.on_message(filters.command("truth"))
async def truth_cmd(client: Client, message: Message):
    question = await fetch_question(TRUTH_API)

    if question:
        await message.reply_text(
            f"🔎 **Truth Time!**\n\n{question}",
            parse_mode=ParseMode.MARKDOWN
        )
    else:
        await message.reply_text("❌ Couldn't fetch truth right now.")


@app.on_message(filters.command("dare"))
async def dare_cmd(client: Client, message: Message):
    question = await fetch_question(DARE_API)

    if question:
        await message.reply_text(
            f"🎯 **Dare Time!**\n\n{question}",
            parse_mode=ParseMode.MARKDOWN
        )
    else:
        await message.reply_text("❌ Couldn't fetch dare right now.")
