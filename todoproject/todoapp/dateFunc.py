
from datetime import datetime

def getDate():
    hour = datetime.now().hour
    minute = datetime.now().minute
    day = datetime.now().day
    month = datetime.now().month
    year = datetime.now().year
    date = str(hour) + ":" + str(minute) + " " + str(day) + "/" + str(month) + "/" + str(year)
    return date
