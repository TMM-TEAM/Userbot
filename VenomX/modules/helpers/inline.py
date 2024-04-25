import asyncio

from ... import *
from .buttons import *
from .wrapper import *
from pyrogram.types import *


async def help_menu_logo(answer):
    image = None
    if image:
        thumb_image = image
    else:
        thumb_image = "https://graph.org/file/b6d415deb9bd5be03d7cc.jpg"
    button = paginate_plugins(0, plugs, "help")
    answer.append(
        InlineQueryResultPhoto(
            photo_url=f"{thumb_image}",
            title="➻ ʜᴇʟᴘ ᴍᴇɴᴜ ✨",
            thumb_url=f"{thumb_image}",
            description=f"➻ ᴏᴘᴇɴ ʜᴇʟᴘ ᴍᴇɴᴜ ᴏғ ᴠᴇɴᴏᴍ ✘ ᴜsᴇʀʙᴏᴛ ✨...",
            caption=f"""
**➻ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ʜᴇʟᴘ ᴍᴇɴᴜ ᴏғ
ᴠᴇɴᴏᴍ ✘ ᴜsᴇʀʙᴏᴛ » {__version__} ✨...

➻ ᴄʟɪᴄᴋ ᴏɴ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴs ᴛᴏ
ɢᴇᴛ ᴜsᴇʀʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs.

➻ ᴜsᴇʀʙᴏᴛ ʙʏ : [ᴠᴇɴᴏᴍ ᴛᴇᴄʜ](https://t.me/tmm_heroku_world).**
            """,
            reply_markup=InlineKeyboardMarkup(button),
        )
    )
    return answer


async def help_menu_text(answer):
    from ... import __version__
    button = paginate_plugins(0, plugs, "help")
    answer.append(
        InlineQueryResultArticle(
            title="➻ ʜᴇʟᴘ ᴍᴇɴᴜ ✨",
            input_message_content=InputTextMessageContent(f"""
**➻ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ʜᴇʟᴘ ᴍᴇɴᴜ ᴏғ
ᴠᴇɴᴏᴍ ✘ ᴜsᴇʀʙᴏᴛ » {__version__} ✨...

➻ ᴄʟɪᴄᴋ ᴏɴ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴs ᴛᴏ
ɢᴇᴛ ᴜsᴇʀʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs.

➻ ᴜsᴇʀʙᴏᴛ ʙʏ : [ᴠᴇɴᴏᴍ ᴛᴇᴄʜ](https://t.me/tmm_heroku_world).**""",
            disable_web_page_preview=True
            ),
            reply_markup=InlineKeyboardMarkup(button),
        )
    )
    return answer


async def run_async_inline():
    @bot.on_inline_query()
    @inline_wrapper
    async def inline_query_handler(bot, query):
        text = query.query
        if text.startswith("help_menu_logo"):
            answer = []
            answer = await help_menu_logo(answer)
            try:
                await bot.answer_inline_query(
                    query.id, results=answer, cache_time=10
                )
            except Exception as e:
                print(str(e))
                return
        elif text.startswith("help_menu_text"):
            answer = []
            answer = await help_menu_text(answer)
            try:
                await bot.answer_inline_query(
                    query.id, results=answer, cache_time=10
                )
            except Exception as e:
                print(str(e))
                return
        else:
            return

