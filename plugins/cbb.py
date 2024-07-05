from pyrogram import __version__
from bot import Bot
import random
from config import *
from pyrogram import Client, filters, enums
from plugins.fsub import Force_Sub
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InputMediaPhoto

contact_button = InlineKeyboardButton("⚡ ᴄᴏɴᴛᴀᴄᴛ ʜᴇʀᴇ ⚡", url="https://t.me/+whP0B-ffw2hkZDU1")
keyboard = InlineKeyboardMarkup([[contact_button]])

from database.database import *
from database.fsub_db import Fsub_DB
fsub_db = Fsub_DB()

REQUEST_CHANNELS = [REQUEST_CHANNEL, REQUEST_CHANNEL2]

ABOUT_TXT = """╔════════════⦿
├⋗ ᴄʀᴇᴀᴛᴏʀ : <a href=https://t.me/Titan_Cinemas_Support_bot>ᴛɪᴛᴀɴ 💞</a>
├⋗ ʟᴀɴɢᴜᴀɢᴇ : <a href=https://python.org/>ᴘʏᴛʜᴏɴ3</a>
├⋗ ʟɪʙʀᴀʀʏ :  <a href=https://docs.pyrogram.org/>ᴘʏʀᴏɢʀᴀᴍ ᴀsʏɴᴄɪᴏ 2.0.106</a>
├⋗ ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : <a href=https://github.com/SirishChowdary/Titan_File_Store/Paid_File_Store>ᴍᴏᴠɪᴇs ᴡᴇʙsᴇʀɪᴇs ʙᴏᴛ</a>
├⋗ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/+4db4vuYykAw3YmE1>ɢʀ ʜᴀᴄᴋᴇʀ</a>
├⋗ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ : <a href=https://t.me/+whP0B-ffw2hkZDU1>ɢʀ ʜᴀᴄᴋᴇʀ sᴜᴘᴘᴏʀᴛᴇᴅ</a>
╚═════════════════⦿ """

@Bot.on_callback_query()
async def cb_handler_func(client, query: CallbackQuery):
    data = query.data

    if data == "about":
        await query.message.edit_text(
            text=ABOUT_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="start"),
                        InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="close")
                    ]
                ]
            ),
        )
    elif data == "help":
        buttons = [
            [
                InlineKeyboardButton("ᴄᴏɴᴛᴀᴄᴛ ʜᴇʀᴇ", url="https://t.me/+whP0B-ffw2hkZDU1")
            ],
            [
                InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="about"),
                InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs", url="https://t.me/+4db4vuYykAw3YmE1")
            ]   
        ]
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        await query.message.edit_text(
            text=HELP_MSG.format(
                first_name=query.from_user.first_name,
                last_name=query.from_user.last_name or "Not Available",
                user_id=query.from_user.id, 
                username=None if not query.from_user.username else '@' + query.from_user.username or "Not Available",
            ),
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    elif data == "start":
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ɢʀ ʜᴀᴄᴋᴇʀ ᴄᴏᴍᴍᴜɴɪᴛʏ", url="https://t.me/+whP0B-ffw2hkZDU1")
                ],
                [
                    InlineKeyboardButton("ʜᴇʟᴘ", callback_data="help"),
                    InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="about")
                ],
                [
                    InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ", url="https://t.me/+4db4vuYykAw3YmE1")
                ]
            ]
        )
        await client.edit_message_media(
                query.message.chat.id, 
                query.message.id, 
                InputMediaPhoto(random.choice(PICS))   
        )
        await query.message.edit_text(
            text=START_MSG.format(first=query.from_user.first_name),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )

    elif data == "checksub":
        msg = query.message
        await query.answer('Checking.......')
        is_req = await Force_Sub(client, msg, query=True)
        print("Query response :- " + is_req)
        if not is_req:
            await query.answer("Thanks for subscribing, Now you can use me!", show_alert=True)          
        elif is_req:
            await query.answer("First join both of the channels then click here!", show_alert=True)
           
            
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
