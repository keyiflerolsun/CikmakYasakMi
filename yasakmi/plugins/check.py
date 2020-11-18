from functools import partial
from pyrogram import Client, filters
from pyrogram.types import Message
from yasakmi.BotConfig import YasakMi
from yasakmi.utils.utils import canGoOut
import logging

command = partial(filters.command, prefixes=["!", "/", "."])


@YasakMi.on_message(command("yasakmi"))
async def yasakmi(client: Client, message: Message) -> None:
    if len(message.command) > 2 or len(message.command) == 1:
        await message.reply_text(
            text="`Komuttan hemen sonra yaşınızı giriniz..`\n`Örnek: /yasakmi 34`",
            quote=True,
        )
        return

    age_input: str = message.command[1]

    if age_input.isdigit():
        age: int = int(age_input)

    else:
        return

    logging.basicConfig(
        filename="app.log", format="%(asctime)s - %(message)s", level=logging.INFO
    )

    if message.from_user.username:
        logging.info(
            f"ID: {message.from_user.id} | UserName: {message.from_user.username} | Name: {message.from_user.first_name}"
        )

    else:
        logging.info(
            f"ID: {message.from_user.id} | UserName: {None} | Name: {message.from_user.first_name}"
        )
    if age < 5:
        await message.reply_text(
            text="Velet daha yolda yürüyemiyorsun ne dışarı çıkması 😂", quote=True
        )

    elif age > 90:
        await message.reply_text(text="Mezardan mı kalkacaksın? ⚰️", quote=True)

    elif canGoOut(age):
        await message.reply_text(text="Evet şuanda dışarı çıkabilirsin 😍", quote=True)

    else:
        await message.reply_text(
            text="Maalesef bu saatte dışarı çıkamazsın 😔", quote=True
        )
