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
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from KanhaMusic import app 


@app.on_message(filters.command(["github", "git"]))
async def github(_, message):
    if len(message.command) != 2:
        return await message.reply_text("❌ Usage: `/git username`", quote=True)

    username = message.text.split(None, 1)[1]
    url = f"https://api.github.com/users/{username}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as request:

            if request.status == 404:
                return await message.reply_text("❌ User not found.")

            data = await request.json()

    # ✅ Safe extraction (prevents crash if null)
    name = data.get("name") or "N/A"
    bio = data.get("bio") or "N/A"
    html_url = data.get("html_url") or "N/A"
    company = data.get("company") or "N/A"
    created_at = data.get("created_at") or "N/A"
    avatar_url = data.get("avatar_url")
    blog = data.get("blog") or "N/A"
    location = data.get("location") or "N/A"
    repos = data.get("public_repos", 0)
    followers = data.get("followers", 0)
    following = data.get("following", 0)

    caption = f"""🌐 **GitHub Info**

👤 **Name:** {name}
🔗 **Username:** `{username}`
📝 **Bio:** {bio}

🔗 **Profile:** [Click Here]({html_url})

🏢 **Company:** {company}
📅 **Created On:** {created_at}
📦 **Repositories:** {repos}

🌍 **Location:** {location}
👥 **Followers:** {followers}
➡️ **Following:** {following}

🔗 **Blog:** {blog}
"""

    # 🔘 Close button
    keyboard = InlineKeyboardMarkup(
        [[InlineKeyboardButton("❌ Close", callback_data="close")]]
    )

    await message.reply_photo(
        photo=avatar_url,
        caption=caption,
        reply_markup=keyboard
    )
