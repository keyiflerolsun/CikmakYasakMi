from functools import partial
from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery
from yasakmi.BotConfig import YasakMi
from yasakmi.utils.helpers import (
    canGoOut,
    ageButton,
    workButton,
    contactButton,
    ageFilter,
    workFilter,
)
from yasakmi.utils.queries import History
from yasakmi.utils.gifs import gifs
from datetime import datetime

import logging
import random

command = partial(filters.command, prefixes=["!", "/", "."])
history = History()
logging.basicConfig(
    filename="info.log", format="%(asctime)s - %(message)s", level=logging.INFO
)

# logger = logging.basicConfig(filename="app.log", level=logging.WARNING)
log = logging.getLogger("WARNING")
log.setLevel(logging.WARNING)
fh = logging.FileHandler("app.log")
formatter = logging.Formatter("%(levelname)s - %(message)s")
fh.setFormatter(formatter)
log.addHandler(fh)


@YasakMi.on_message(command("start") and filters.private)
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

    await client.delete_messages(
        chat_id=callback.message.chat.id, message_ids=[callback.message.message_id]
    )

    if canGoOut(datetime.now(), work, age):
        # text = f"Evet dışarı çıkabilirsin 😍🏃‍♂️"
        gif = random.choice(gifs["yes"])

        await client.send_animation(
            chat_id=callback.message.chat.id,
            animation=gif["gif"],
            caption=f"{gif['text']}\n\nDışarı çıkabiliyorsun ama soruların olursa gruptan yazabilir veya daha sonra botun kaynak kodlarını inceleyebilirsin 😇",
            reply_markup=contactButton,
        )
    else:
        # text = f"Hayır dışarı çıkamazsın ama @koyumuhendis grubuna gelebilirsin 😇"
        gif = random.choice(gifs["no"])
        await client.send_animation(
            chat_id=callback.message.chat.id,
            animation=gif["gif"],
            caption=f"{gif['text']}\n\nEvde canın sıkılmasın. Soruların olursa gruptan yazabilir veya botun kaynak kodlarını inceleyebilirsin 😇",
            reply_markup=contactButton,
        )

    try:
        uname = callback.from_user.username

    except NameError:
        uname = None
    log.warning(
        f"ID: {callback.from_user.id} | UserName: {uname} | Name: {callback.from_user.first_name}"
    )
    # await callback.edit_message_text(text=text, reply_markup=ReplyKeyboardRemove())
