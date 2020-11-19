from functools import partial
from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery
from yasakmi.BotConfig import YasakMi
from yasakmi.utils.helpers import canGoOut
from yasakmi.utils.queries import History
from datetime import datetime
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardRemove,
)
import logging

command = partial(filters.command, prefixes=["!", "/", "."])
history = History()
logging.basicConfig(
    filename="app.log", format="%(asctime)s - %(message)s", level=logging.INFO
)

ageButton = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="20'den Küçük", callback_data="kid")],
        [InlineKeyboardButton(text="20 ile 65 Arası", callback_data="adult")],
        [InlineKeyboardButton(text="65'ten Büyük", callback_data="old")],
    ]
)

workButton = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="Çalışıyorum", callback_data="yes")],
        [InlineKeyboardButton(text="Çalışmıyorum", callback_data="no")],
    ]
)

ageFilter = filters.create(lambda _, __, query: query.data in ["kid", "adult", "old"])
workFilter = filters.create(lambda _, __, query: query.data in ["yes", "no"])


@YasakMi.on_message(command("start"))
async def start(client: Client, message: Message) -> None:
    history.add_user(message.from_user.id)
    await message.reply(
        text=f"Merhaba {message.from_user.first_name}, şuan dışarı çıkabiliyor musun öğrenmek için yaş aralığını seçerek başlayabilirsin 😬",
        reply_markup=ageButton,
    )


@YasakMi.on_callback_query(ageFilter)
async def askWork(client: Client, callback: CallbackQuery) -> None:
    history.add_data(callback.from_user.id, callback.data)
    await callback.edit_message_text(
        text=f"Peki çalışıyor musun?", reply_markup=workButton
    )


@YasakMi.on_callback_query(workFilter)
async def yasakmi(client: Client, callback: CallbackQuery) -> None:
    history.add_data(callback.from_user.id, callback.data)

    age, work = history.get_data(callback.from_user.id)

    if age == "kid":
        age = 7
    elif age == "adult":
        age = 25
    else:
        age = 70

    work = True if work == "yes" else False
    if canGoOut(datetime.now(), work, age):
        text = f"Evet dışarı çıkabilirsin 😍🏃‍♂️"
    else:
        text = f"Hayır dışarı çıkamazsın ama @koyumuhendis grubuna gelebilirsin 😇"

    try:
        uname = callback.from_user.username

    except NameError:
        uname = None

    logging.info(
        f"ID: {callback.from_user.id} | UserName: {uname} | Name: {callback.from_user.first_name}"
    )
    await callback.edit_message_text(text=text, reply_markup=ReplyKeyboardRemove())
