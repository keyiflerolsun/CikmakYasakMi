from datetime import datetime


def isWeekend() -> bool:
    day = int(datetime.now().strftime("%w"))
    if day in range(1, 5):
        return False

    else:
        return True


def canGoOut(age: int) -> bool:
    hour = datetime.now().hour

    if age < 25 or age > 65:
        if hour < 10 or hour > 16:
            return False

        else:
            return True

    else:
        if isWeekend() and (hour < 10 or hour > 20):
            return False
        else:
            return True