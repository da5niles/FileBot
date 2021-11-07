#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>Привет! \nЯ могу сохранять файлы и выдавать их по определенной ссылке. Могу использоваться как в личных целях, так и для каналов. \n\nМеня создал @dA5niles с помощью готового кода, переведя на русский язык. За помощью и тестированием обращайтесь к нему. \n\nИсходный код - https://github.com/CodeXBotz/File-Sharing-Bot/ \nКод под русский язык - https://github.com/da5niles/FileBot     \n\n  Тех.информация:\n ○ Creator : <a href='tg://user?id={OWNER_ID}'>This Person</a>\n○ Language : <code>Python3</code>\n○ Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n○ Source Code : <a href='https://github.com/CodeXBotz/File-Sharing-Bot'>Click here</a>\n○ Channel : @CodeXBotz\n○ Support Group : @CodeXBotzSupport</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
