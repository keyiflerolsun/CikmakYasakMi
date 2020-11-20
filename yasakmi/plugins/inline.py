# from functools import partial
# from pyrogram import Client, filters
# from pyrogram.types import Message, CallbackQuery
# from yasakmi.BotConfig import YasakMi
# from yasakmi.utils.helpers import (
#     canGoOut,
#     ageButton,
#     workButton,
#     contactButton,
#     ageFilter,
#     workFilter,
# )

# from yasakmi.utils.gifs import gifs
# from datetime import datetime

# import logging
# import random

# logging.basicConfig(filename="app.log", level=logging.WARNING)


# @YasakMi.on_inline_query()
# async def yasakmi(client: Client, callback: CallbackQuery) -> None:
#     #TODO
#     pass
# if age == "kid":
#     age = 7
# elif age == "adult":
#     age = 25
# else:
#     age = 70

# work = True if work == "yes" else False

# await client.delete_messages(
#     chat_id=callback.message.chat.id, message_ids=[callback.message.message_id]
# )

# if canGoOut(datetime.now(), work, age):
#     # text = f"Evet dışarı çıkabilirsin 😍🏃‍♂️"
#     gif = random.choice(gifs["yes"])

#     await client.send_animation(
#         chat_id=callback.message.chat.id,
#         animation=gif["gif"],
#         caption=f"{gif['text']}\n\nDışarı çıkabiliyorsun ama soruların olursa gruptan yazabilir veya daha sonra botun kaynak kodlarını inceleyebilirsin 😇",
#         reply_markup=contactButton,
#     )
# else:
#     # text = f"Hayır dışarı çıkamazsın ama @koyumuhendis grubuna gelebilirsin 😇"
#     gif = random.choice(gifs["no"])
#     await client.send_animation(
#         chat_id=callback.message.chat.id,
#         animation=gif["gif"],
#         caption=f"{gif['text']}\n\nEvde canın sıkılmasın. Soruların olursa gruptan yazabilir veya botun kaynak kodlarını inceleyebilirsin 😇",
#         reply_markup=contactButton,
#     )

# try:
#     uname = callback.from_user.username

# except NameError:
#     uname = None

# logging.warning(
#     f"ID: {callback.from_user.id} | UserName: {uname} | Name: {callback.from_user.first_name}"
# )
# # await callback.edit_message_text(text=text, reply_markup=ReplyKeyboardRemove())
