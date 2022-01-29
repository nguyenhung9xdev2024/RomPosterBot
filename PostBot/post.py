import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import *

bot = telebot.TeleBot(BOT_TOKEN, parse_mode="HTML")

def send_post(chat_id, image, caption, button):
    if caption == "" or not caption or caption is None:
        return bot.send_photo(chat_id=chat_id, photo=image, reply_markup=button)
    else:
        return bot.send_photo(chat_id=chat_id, photo=image, caption=caption, reply_markup=button)

if WITH_BUTTONS == "True":
    def message_content():
        msg = ""
        msg += f"<b>{ROM_NAME} {BUILD_TYPE} for {BRAND} {DEVICE_NAME} ({CODENAME})</b>\n\n"
        msg += f"<b>Maintainer:</b> @{MAINTAINER_USERNAME}\n"
        msg += f"<b>Rom Version:</b> {ROM_VERSION} <b>|</b> Android {ANDROID_VERSION}\n"
        msg += f"<b>Build Date:</b> {BUILD_DATE}\n\n"
        msg += f"<b>Source Changelogs:</b> <a href='{SOURCE_CHANGELOG_URL}'>Here</a>\n\n"
        msg += f"<b>Device Changelogs:</b>\n{changelog()}\n"
        msg += f"<b>Notes:</b>\n{notes()}\n"
        msg += f"<b>MD5:</b> <code>{MD5}</code>\n\n"
        if CUSTOM_MESSAGE:
            msg += f"<b>{CUSTOM_MESSAGE}</b>\n\n"
        else:
            pass
        msg += f"{HASHTAGS}"
        return msg

    def button():
        buttons = InlineKeyboardMarkup()
        buttons.row_width = 2
        button1 = InlineKeyboardButton(text="XDA", url=f"{XDA_POST}")
        button2 = InlineKeyboardButton(text="Support Group", url=f"https://t.me/{SUPPORT_GROUP}")
        button3 = InlineKeyboardButton(text="Download", url=f"{DOWNLOAD_URL}")
        return buttons.add(button1, button2, button3)

    def tg_message():
        print(f"Posting rom in the following chats: {CHAT_ID}")
        for chats in CHAT_ID:
            if STICKER_ID:
                bot.send_sticker(chats, STICKER_ID)
                msg = send_post(chats, BANNER_URL, message_content(), button())
            else:
                msg = send_post(chats, BANNER_URL, message_content(), button())
            try:
                bot.pin_chat_message(chats, msg.message_id)
            except Exception:
                print(f"Not enough rights to pin message in the chat: {chats}")
        print("Success")

else:
    def send_post(chat_id, image, caption):
        if caption == "" or not caption or caption is None:
            return bot.send_photo(chat_id=chat_id, photo=image)
        else:
            return bot.send_photo(chat_id=chat_id, photo=image, caption=caption)

    def message_content():
        msg = ""
        msg += f"<b>{ROM_NAME} {BUILD_TYPE} for {BRAND} {DEVICE_NAME} ({CODENAME})</b>\n\n"
        msg += f"<b>Maintainer:</b> @{MAINTAINER_USERNAME}\n"
        msg += f"<b>Rom Version:</b> {ROM_VERSION} <b>|</b> Android {ANDROID_VERSION}\n"
        msg += f"<b>Build Date:</b> {BUILD_DATE}\n\n"
        msg += f"<b>Source Changelogs:</b> <a href='{SOURCE_CHANGELOG_URL}'>Here</a>\n\n"
        msg += f"<b>Device Changelogs:</b>\n{changelog()}\n"
        msg += f"<b>Notes:</b>\n{notes()}\n"
        msg += f"<b>XDA Thread:</b> <a href='{XDA_POST}'>Here</a>\n"
        msg += f"<b>Download:</b> <a href='{DOWNLOAD_URL}'>Here</a>\n"
        msg += f"<b>MD5:</b> <code>{MD5}</code>\n\n"
        msg += f"<b>Support Group:</b> @{SUPPORT_GROUP}\n\n"
        if CUSTOM_MESSAGE:
            msg += f"<b>{CUSTOM_MESSAGE}</b>"
            msg += f"{HASHTAGS}"
        else:
            msg += f"{HASHTAGS}"
        return msg

    def tg_message():
        print(f"Posting rom in the following chats: {CHAT_ID}")
        for chats in CHAT_ID:
            if STICKER_ID:
                bot.send_sticker(chats, STICKER_ID)
                msg = send_post(chats, BANNER_URL, message_content())
            else:
                msg = send_post(chats, BANNER_URL, message_content())
            try:
                bot.pin_chat_message(chats, msg.message_id)
            except Exception:
                print(f"Not enough rights to pin message in the chat: {chats}")
        print("Success")

tg_message()
