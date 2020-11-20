from datetime import datetime
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardRemove,
)
from pyrogram import filters


def isWeekend(date: datetime) -> bool:
    if int(date.strftime("%w")) in range(1, 6):
        return False

    else:
        return True


def canGoOut(time: datetime, work: bool, age: int) -> bool:

    if not isWeekend(time) and work:
        return True

    elif not isWeekend(time) and not work:
        if age < 20 and 13 <= time.hour < 16:
            return True

        elif age >= 65 and 10 <= time.hour < 13:
            return True

        elif 20 <= age < 65:
            return True

        else:
            return False

    elif isWeekend(time):
        if work:
            return True

        else:
            if 10 <= time.hour < 20:
                return True

            else:
                return False


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

contactButton = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="Mühendis Köyü 🏠", url="https://t.me/koyumuhendis")],
        [
            InlineKeyboardButton(
                text="Github 💻", url="https://github.com/ahmetveburak/CikmakYasakMi"
            )
        ],
    ]
)

ageFilter = filters.create(lambda _, __, query: query.data in ["kid", "adult", "old"])
workFilter = filters.create(lambda _, __, query: query.data in ["yes", "no"])
