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

from pyrogram import filters
from pyrogram.types import Message

from KanhaMusic import app
from KanhaMusic.core.call import Anu
from KanhaMusic.misc import db
from KanhaMusic.utils.database import get_loop, is_active_chat
from KanhaMusic.utils.decorators import AdminRightsCheck
from KanhaMusic.utils.decorators.language import language
from KanhaMusic.utils.inline import close_markup
from KanhaMusic.utils.stream.autoclear import auto_clean
from config import BANNED_USERS

# Import the shared skip/replay helper from callback.py
from KanhaMusic.plugins.admins.callback import _do_skip_or_replay


@app.on_message(
    filters.command(["skip", "cskip", "next", "cnext"]) & filters.group & ~BANNED_USERS
)
@AdminRightsCheck
async def skip_command(cli, message: Message, _, chat_id):
    if not await is_active_chat(chat_id):
        return await message.reply_text(_["general_5"])

    # ── skip N tracks ─────────────────────────────────────────────────────
    if len(message.command) >= 2:
        loop = await get_loop(chat_id)
        if loop != 0:
            return await message.reply_text(_["admin_8"])

        state = message.text.split(None, 1)[1].strip()
        if not state.isnumeric():
            return await message.reply_text(_["admin_9"])

        state = int(state)
        check = db.get(chat_id)
        if not check:
            return await message.reply_text(_["queue_2"])

        count = len(check)
        if count <= 2:
            return await message.reply_text(_["admin_10"])

        max_skip = count - 1
        if not (1 <= state <= max_skip):
            return await message.reply_text(_["admin_11"].format(max_skip))

        mention = message.from_user.mention
        for _ in range(state):
            popped = None
            try:
                popped = check.pop(0)
            except Exception:
                return await message.reply_text(_["admin_12"])
            if popped:
                await auto_clean(popped)
            if not check:
                try:
                    await message.reply_text(
                        text=_["admin_6"].format(mention, message.chat.title),
                        reply_markup=close_markup(_),
                    )
                    await Anu.stop_stream(chat_id)
                except Exception:
                    pass
                return
        # after popping N, fall through to play what's now at position 0

    # ── skip 1 (or play position 0 after N-skip above) ───────────────────
    await _do_skip_or_replay(message, chat_id, _, is_replay=False)
