import os
import pytz
import logging
import random
import asyncio
from bot import Bot
from config import *
import datetime, time
from datetime import timedelta
from pyrogram import Client, filters, enums
from pyrogram.errors.exceptions.bad_request_400 import MessageTooLong
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, InputMediaPhoto
from database.database import *
from database.premium_db import db1

async def get_seconds(time_string):
    def extract_value_and_unit(ts):
        value = ""
        unit = ""

        index = 0
        while index < len(ts) and ts[index].isdigit():
            value += ts[index]
            index += 1

        unit = ts[index:].lstrip()

        if value:
            value = int(value)

        return value, unit

    value, unit = extract_value_and_unit(time_string)

    if unit == 's':
        return value
    elif unit == 'min':
        return value * 60
    elif unit == 'hour':
        return value * 3600
    elif unit == 'day':
        return value * 86400
    elif unit == 'month':
        return value * 86400 * 30
    elif unit == 'year':
        return value * 86400 * 365
    else:
        return 0

PREPREMIUM = """
ᴏᴏᴏᴏ ᴛʜᴀɴᴋs ғᴏʀ ᴍᴀᴋɪɴɢ ʏᴏᴜʀ ᴄʜᴏɪᴄᴇ ᴛᴏ ʙᴇ ᴡɪᴛʜ ᴜs ᴀɴᴅ ᴛʜᴀɴᴋs ғᴏʀ sᴜᴘᴘᴏʀᴛɪɴɢ

🎖️ <u>ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀɴs</u>

● <code>10₹</code> ➛ <u>ʙʀᴏɴᴢᴇ ᴘʟᴀɴ</u> » <code>7 ᴅᴀʏꜱ</code>
● <code>29₹</code> ➛ <u>ꜱɪʟᴠᴇʀ ᴘʟᴀɴ</u> » <code>30 ᴅᴀʏꜱ</code>
● <code>129₹</code> ➛ <u>ɢᴏʟᴅ ᴘʟᴀɴ</u> » <code>90 ᴅᴀʏꜱ</code>
● <code>370₹</code> ➛ <u>ᴘʟᴀᴛɪɴᴜᴍ ᴘʟᴀɴ</u> » <code>180 ᴅᴀʏꜱ</code>
● <code>500₹</code> ➛ <u>ᴅɪᴀᴍᴏɴᴅ ᴘʟᴀɴ</u> » <code>365 ᴅᴀʏꜱ</code>

💵 ᴜᴘɪ ɪᴅ - <code>titanindia@ibl</code>
⚡ ǫʀ ᴄᴏᴅᴇ - <a href='https://te.legra.ph/file/c2aa509df2e82077c7a0d.jpg'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>

‼️ ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ.
<blockquote>⚡ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href='https://t.me/Titan_Cinemas_Support_bot'>⚡ ᴛɪᴛᴀɴ ɪɴᴅɪᴀ</a></blockquote>"""


@Bot.on_message(filters.command("plans") & filters.incoming)
async def plans(client, message):
    try:
        user_id = message.from_user.id 
        users = message.from_user.mention 
        btn = [[
            InlineKeyboardButton("📲 ꜱᴇɴᴅ ᴘᴀʏᴍᴇɴᴛ ꜱᴄʀᴇᴇɴꜱʜᴏᴛ ʜᴇʀᴇ", user_id=6953078181)],[InlineKeyboardButton("❌ ᴄʟᴏꜱᴇ ❌", callback_data="close_data")
        ]]
        await message.reply_photo(photo="https://te.legra.ph/file/c2aa509df2e82077c7a0d.jpg", caption=PREPREMIUM, reply_markup=InlineKeyboardMarkup(btn))
    except Exception as e:
        print(e)

@Bot.on_message(filters.command("remove_premium") & filters.user(ADMINS))
async def remove_premium(client, message):
    if len(message.command) == 2:
        user_id = int(message.command[1])  
        user = await client.get_users(user_id)
        if await db1.remove_premium_access(user_id):
            await message.reply_text("ᴜꜱᴇʀ ʀᴇᴍᴏᴠᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ !")
            await client.send_message(
                chat_id=user_id,
                text=f"<b>ʜᴇʏ {user.mention},\n\nʏᴏᴜʀ ᴘʀᴇᴍɪᴜᴍ ᴀᴄᴄᴇss ʜᴀs ʙᴇᴇɴ ʀᴇᴍᴏᴠᴇᴅ.\nᴛʜᴀɴᴋ ʏᴏᴜ ꜰᴏʀ ᴜsɪɴɢ ᴏᴜʀ sᴇʀᴠɪᴄᴇ 😊\nᴄʟɪᴄᴋ ᴏɴ /plan ᴛᴏ ᴄʜᴇᴄᴋ ᴏᴜᴛ ᴏᴛʜᴇʀ ᴘʟᴀɴꜱ.</b>"
            )
        else:
            await message.reply_text("ᴜɴᴀʙʟᴇ ᴛᴏ ʀᴇᴍᴏᴠᴇ ᴜꜱᴇᴅ !\nᴀʀᴇ ʏᴏᴜ ꜱᴜʀᴇ, ɪᴛ ᴡᴀꜱ ᴀ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀ ɪᴅ ?")
    else:
        await message.reply_text("ᴜꜱᴀɢᴇ : /remove_premium user_id")

@Bot.on_message(filters.command("add_premium") & filters.user(ADMINS))
async def give_premium_cmd_handler(client, message):
    try:
        if len(message.command) == 4:
            time_zone = datetime.datetime.now(pytz.timezone("Asia/Kolkata"))
            current_time = time_zone.strftime("%d-%m-%Y\n⏱️ ᴊᴏɪɴɪɴɢ ᴛɪᴍᴇ : %I:%M:%S %p") 
            user_id = int(message.command[1])  
            user = await client.get_users(user_id)
            time = message.command[2]+" "+message.command[3]
            seconds = await get_seconds(time)
            if seconds > 0:
                expiry_time = datetime.datetime.now() + datetime.timedelta(seconds=seconds)
                user_data = {"id": user_id, "expiry_time": expiry_time}  # Using "id" instead of "user_id"  
                await db1.update_user(user_data)  # Use the update_user method to update or insert user data
                data = await db1.get_user(user_id)
                expiry = data.get("expiry_time")   
                expiry_str_in_ist = expiry.astimezone(pytz.timezone("Asia/Kolkata")).strftime("%d-%m-%Y\n⏱️ ᴇxᴘɪʀʏ ᴛɪᴍᴇ : %I:%M:%S %p")         
                await message.reply_text(f"ᴘʀᴇᴍɪᴜᴍ ᴀᴅᴅᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ✅\n\n👤 ᴜꜱᴇʀ : {user.mention}\n⚡ ᴜꜱᴇʀ ɪᴅ : <code>{user_id}</code>\n⏰ ᴘʀᴇᴍɪᴜᴍ ᴀᴄᴄᴇꜱꜱ : <code>{time}</code>\n\n⏳ ᴊᴏɪɴɪɴɢ ᴅᴀᴛᴇ : {current_time}\n\n⌛️ ᴇxᴘɪʀʏ ᴅᴀᴛᴇ : {expiry_str_in_ist} \n\n <blockquote>💞 ʙᴏᴛ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ <a href=https://t.me/Titan_Cinemas_Support_bot>⚡ᴛɪᴛᴀɴ ᴄɪɴᴇᴍᴀs</a></b></blockquote>", disable_web_page_preview=True)
                await client.send_message(
                    chat_id=user_id,
                    text=f"👋 ʜᴇʏ {user.mention},\nᴛʜᴀɴᴋ ʏᴏᴜ ꜰᴏʀ ᴘᴜʀᴄʜᴀꜱɪɴɢ ᴘʀᴇᴍɪᴜᴍ.\nᴇɴᴊᴏʏ !! ✨🎉\n\n⏰ ᴘʀᴇᴍɪᴜᴍ ᴀᴄᴄᴇꜱꜱ : <code>{time}</code>\n⏳ ᴊᴏɪɴɪɴɢ ᴅᴀᴛᴇ : {current_time}\n\n⌛️ ᴇxᴘɪʀʏ ᴅᴀᴛᴇ : {expiry_str_in_ist} \n\n <blockquote>💞 ʙᴏᴛ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ <a href=https://t.me/Titan_Cinemas_Support_bot>⚡ᴛɪᴛᴀɴ ᴄɪɴᴇᴍᴀs</a></b></blockquote>", disable_web_page_preview=True              
                )    
                await client.send_message(PREMIUM_LOGS, text=f"#Added_Premium\n\n👤 ᴜꜱᴇʀ : {user.mention}\n⚡ ᴜꜱᴇʀ ɪᴅ : <code>{user_id}</code>\n⏰ ᴘʀᴇᴍɪᴜᴍ ᴀᴄᴄᴇꜱꜱ : <code>{time}</code>\n\n⏳ ᴊᴏɪɴɪɴɢ ᴅᴀᴛᴇ : {current_time}\n\n⌛️ ᴇxᴘɪʀʏ ᴅᴀᴛᴇ : {expiry_str_in_ist} \n\n <blockquote>💞 ʙᴏᴛ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ <a href=https://t.me/Titan_Cinemas_Support_bot>⚡ᴛɪᴛᴀɴ ᴄɪɴᴇᴍᴀs</a></b></blockquote>", disable_web_page_preview=True)
                        
            else:
                await message.reply_text("Invalid time format. Please use '1 day for days', '1 hour for hours', or '1 min for minutes', or '1 month for months' or '1 year for year'")
        else:
            await message.reply_text("Usage : /add_premium user_id time (e.g., '1 day for days', '1 hour for hours', or '1 min for minutes', or '1 month for months' or '1 year for year')")

    except Exception as e:
        print(e)

@Bot.on_message(filters.command("premium_users") & filters.user(ADMINS))
async def premium_user(client, message: Message):
    aa = await message.reply_text("<i>Fetching...</i>")
    new = "⚜️ Premium Users List:\n\n"
    user_count = 1
    try:
        user_ids = await full_userbase()
        for user_id in user_ids:
            data = await db1.get_user(user_id)
            if data and data.get("expiry_time"):
                expiry_time_utc = data["expiry_time"].astimezone(pytz.utc)  # Convert to UTC if not already
                expiry_time_ist = expiry_time_utc.astimezone(pytz.timezone("Asia/Kolkata"))
                
                current_time = datetime.datetime.now(pytz.timezone("Asia/Kolkata"))
                
                if expiry_time_ist > current_time:
                    time_left = expiry_time_ist - current_time
                    days = time_left.days
                    hours, remainder = divmod(time_left.seconds, 3600)
                    minutes, seconds = divmod(remainder, 60)
                    time_left_str = f"{days} days, {hours} hours, {minutes} minutes"
                else:
                    time_left_str = "Expired"
                
                user_mention = (await client.get_users(user_id)).mention
                new += (
                    f"{user_count}. {user_mention}\n"
                    f"👤 User ID: {user_id}\n"
                    f"⏳ Expiry Date: {expiry_time_ist.strftime('%d-%m-%Y %I:%M:%S %p')}\n"
                    f"⏰ Time Left: {time_left_str}\n\n"
                )
                user_count += 1
            else:
                pass
        
        await aa.edit_text(new)
    
    except MessageTooLong:
        with open('usersplan.txt', 'w+', encoding='utf-8') as outfile:
            outfile.write(new)
        await message.reply_document('usersplan.txt', caption="Paid Users:")

    except Exception as e:
        print(f"Error in premium_user command: {e}")
        await aa.edit_text("<i>Error fetching premium users list. Please try again later.</i>")

@Bot.on_message(filters.command("myplan"))
async def myplan(client, message):
    user = message.from_user.mention 
    user_id = message.from_user.id
    data = await db1.get_user(message.from_user.id)
    photo_url = random.choice(PICS)
    if data and data.get("expiry_time"):
        expiry = data.get("expiry_time") 
        expiry_ist = expiry.astimezone(pytz.timezone("Asia/Kolkata"))
        expiry_str_in_ist = expiry.astimezone(pytz.timezone("Asia/Kolkata")).strftime("%d-%m-%Y\n⏱️ ᴇxᴘɪʀʏ ᴛɪᴍᴇ : %I:%M:%S %p")            
        current_time = datetime.datetime.now(pytz.timezone("Asia/Kolkata"))
        time_left = expiry_ist - current_time   
        days = time_left.days
        hours, remainder = divmod(time_left.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        time_left_str = f"{days} ᴅᴀʏꜱ, {hours} ʜᴏᴜʀꜱ, {minutes} ᴍɪɴᴜᴛᴇꜱ"
        await message.reply_photo(photo_url, 
                                  caption=f"⚜️ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀ ᴅᴀᴛᴀ :\n\n👤 ᴜꜱᴇʀ : {user}\n⚡ ᴜꜱᴇʀ ɪᴅ : <code>{user_id}</code>\n⏰ ᴛɪᴍᴇ ʟᴇꜰᴛ : {time_left_str}\n⌛️ ᴇxᴘɪʀʏ ᴅᴀᴛᴇ : {expiry_str_in_ist} \n\n <blockquote>💞 ʙᴏᴛ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ <a href=https://t.me/Titan_Cinemas_Support_bot>⚡ᴛɪᴛᴀɴ ᴄɪɴᴇᴍᴀs</a></b></blockquote>",
                                  disable_web_page_preview=True)
    else:
        await message.reply_photo(photo_url,
                                  caption=f"ʜᴇʏ {user},\n\nʏᴏᴜ ᴅᴏ ɴᴏᴛ ʜᴀᴠᴇ ᴀɴʏ ᴀᴄᴛɪᴠᴇ ᴘʀᴇᴍɪᴜᴍ ᴘʟᴀɴꜱ, ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴛᴀᴋᴇ ᴘʀᴇᴍɪᴜᴍ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ 👇 \n\n <blockquote>💞 ʙᴏᴛ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ <a href=https://t.me/Titan_Cinemas_Support_bot>⚡ᴛɪᴛᴀɴ ᴄɪɴᴇᴍᴀs</a></b></blockquote>",
                                  reply_markup=types.InlineKeyboardMarkup([[types.InlineKeyboardButton("💫 ʙᴜʏ ᴘʀᴇᴍɪᴜᴍ 💫", callback_data='premium')]]))
