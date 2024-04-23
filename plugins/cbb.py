from pyrogram import __version__
from bot import Bot
import random
from config import OWNER_ID, START_MSG, PICS
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

contact_button = InlineKeyboardButton("⚡ ᴄᴏɴᴛᴀᴄᴛ ʜᴇʀᴇ ⚡", url="https://t.me/Titan_Cinemas_Support_bot")
keyboard = InlineKeyboardMarkup([[contact_button]])

@Bot.on_callback_query()
async def cb_handler_func(client, query: CallbackQuery):
    data = query.data

    if data == "about":
        await query.message.edit_text(
            text=(
                f"<b>──────[ 🚀 ᴛɪᴛᴀɴ ᴄɪɴᴇᴍᴀs 🚀 ]───────────\n"
                f"├🌟 ᴍʏ ɴᴀᴍᴇ : <a href=https://t.me/Titan_Link_Store_Bot>ᴛɪᴛᴀɴ ʟɪɴᴋ ᴘʀᴏᴠɪᴅᴇʀ</a>\n"
                f"├💻 ʟᴀɴɢᴜᴀɢᴇ: <a href=https://aka.ms/vs/17/release/vc_redist.x64.exe>ᴄ++ & ᴊᴀᴠᴀ</a>\n"
                f"├🌐 ʜᴏsᴛᴇᴅ ᴏɴ: <a href=www.hostinger.in>ʜᴏsᴛɪɴɢᴇʀ ᴠᴘs</a>\n"
                f"├👨‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ: <a href=https://t.me/Titan_Cinemas_Support_bot>ᴛɪᴛᴀɴ ᴏᴡɴᴇʀ</a>\n"
                f"├🛠️ ʙᴏᴛ sᴜᴘᴘᴏʀᴛ: <a href=https://t.me/Titan_Cinemas_Support_bot>ᴛɪᴛᴀɴ sᴜᴘᴘᴏʀᴛ</a>\n"
                f"├📢 ʙᴏᴛ ᴜᴘᴅᴀᴛᴇs: <a href=https://t.me/Titan_Bots_India>ʙᴏᴛ ᴜᴘᴅᴀᴛᴇs</a>\n"
                f"╰──────[ 🇮🇳 ᴛɪᴛᴀɴ ᴄᴏᴍᴍᴜɴɪᴛʏ 🇮🇳 ]───────────</b>"
            ),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("📝 ʙᴀᴄᴋ", callback_data="start")],
                    [InlineKeyboardButton("🎉 ᴄʟᴏsᴇ", callback_data="close")]
                ]
            ),
        )
    elif data == "help":
        buttons = [
            [
                InlineKeyboardButton("⚡ ᴄᴏɴᴛᴀᴄᴛ ʜᴇʀᴇ ⚡", url="https://t.me/Titan_Cinemas_Support_bot")
            ],
            [
                InlineKeyboardButton("🚀 ᴀʙᴏᴜᴛ", callback_data="about"),
                InlineKeyboardButton("📝 ᴄᴏᴘɪʀɪɢʜᴛs", callback_data="button2")
            ],
            [
                InlineKeyboardButton("📝 ᴛɪᴛᴀɴ ᴘʀᴇᴍɪᴜᴍ", callback_data="premium"),
                InlineKeyboardButton("🌟 ʟɪɴᴋ ʙʟᴏᴄᴋᴇᴅ?", url="https://t.me/Titan_Association_bot")
            ],
            [
                InlineKeyboardButton("🔥 ʜᴏᴡ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ 🔥", callback_data="tutorial")
            ]   
        ]

        await query.message.edit_text(
            text="ᴛʜɪs ɪs ᴀ ɴᴇᴡ ᴏᴘᴛɪᴏɴ! ᴄʟɪᴄᴋ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ.",
            reply_markup=InlineKeyboardMarkup(buttons)
        )
        await query.message.reply_photo(
            photo=random.choice(PICS),
            caption="🆘 ʜᴇʟᴘ ? ʏᴇᴀʜ ᴡᴇ ᴀʀᴇ ʜᴇʀᴇ ᴛᴏ ʜᴇʟᴘ  🆘\n"
                    "sᴏ ᴄʟɪᴄᴋ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ᴍᴏsᴛ ᴀsᴋᴇᴅ ǫᴜᴇsᴛɪᴏɴs.\n\n"
                    "sᴛɪʟʟ sᴏʟᴠᴇ ɴᴇʜɪ ʜᴜᴀ ɴᴏ ᴘʀᴏʙʟᴇᴍ ᴄᴏɴᴛᴀᴄᴛ ʙᴜᴛᴛᴏɴ ᴘᴇ ᴄʟɪᴄᴋ ᴋᴀʀᴏ ✅",
            reply_markup=reply_markup,
        )
    elif data == "start":
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⚡ ᴛɪᴛᴀɴ ᴄɪɴᴇᴍᴀs ⚡", url="https://t.me/Titan_CInemas")
                ],
                [
                    InlineKeyboardButton("🧿 ʜᴇʟᴘ", callback_data="help"),
                    InlineKeyboardButton("🔥 ᴀʙᴏᴜᴛ", callback_data="about")
                ],
                [
                    InlineKeyboardButton("🚀 ʙᴜʏ ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ : ʀᴇᴍᴏᴠᴇ ᴀᴅꜱ 🚀", url="https://t.me/titan_cinemas")
                ]
            ]
        )
        await query.message.edit_text(
            text=START_MSG.format(
                first=query.from_user.first_name,
                last=query.from_user.last_name,
                username=None if not query.from_user.username else '@' + query.from_user.username,
                mention=query.from_user.mention,
                id=query.from_user.id
            ),
            reply_markup=reply_markup
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
