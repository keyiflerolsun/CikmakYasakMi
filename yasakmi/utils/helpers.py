from datetime import datetime


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