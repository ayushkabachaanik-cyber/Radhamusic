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

import aiohttp
from io import BytesIO
from pyrogram import filters
from KanhaMusic import app 


async def make_carbon(code: str):
    url = "https://carbonara.solopov.dev/api/cook"

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json={"code": code}) as resp:
            if resp.status != 200:
                return None
            image = BytesIO(await resp.read())

    image.name = "carbon.png"
    return image


@app.on_message(filters.command("carbon"))
async def carbon_cmd(client, message):
    replied = message.reply_to_message

    if not replied or not (replied.text or replied.caption):
        return await message.reply_text(
            "**❌ Reply to a text message to generate carbon image.**"
        )

    status = await message.reply("⚡ Processing...")

    carbon = await make_carbon(replied.text or replied.caption)

    if not carbon:
        return await status.edit("❌ Failed to generate carbon image.")

    await status.edit("📤 Uploading...")

    await message.reply_photo(carbon)

    await status.delete()
    carbon.close()
