import datetime as dt
import datetime


def dataCreationAddedToTimeLaps(dateTimeCreationFile, timeLapse):
    """date = dateTimeCreationFile[0:10]
    time = dateTimeCreationFile[11:]
    timeLapse = timeLapseToTime(timeLapse)"""
    return str(sumTimes(dateTimeCreationFile, timeLapse))

    #return str(date) + " " + str(sumTimes(time, timeLapse))


def timeLapseToTime(timeLapse):
    timeLapse = timeLapse.strip().replace(".", ":")
    occ = countOccurrence(timeLapse, ":")

    if(occ == 1):  #sec, mill
        timeLapse = "00:00:" + timeLapse
    elif (occ == 2):   #min, sec, mill
        timeLapse = "00:" + timeLapse

    return timeLapse


def countOccurrence(string, type):
    occ = 0
    for i in string:
        if i == type:
            occ += 1
    return occ


def sumTimes(dateTimeCreationFile, timeLapse):
    """time = dt.datetime.strptime(time1, '%H:%M:%S:%f')
    timelapse = dt.datetime.strptime(time2, '%H:%M:%S:%f')   
    time_zero = dt.datetime.strptime('00:00:00:00', '%H:%M:%S:%f')"""
    
    return dateTimeCreationFile + datetime.timedelta(0, timeLapse)
    #return (time - time_zero + timelapse).time()


def getDateFromString(dateString):
    return datetime.datetime.fromisoformat(dateString)

# Checks if two dates are equal accepting a 1-second time difference margin */
def checkSameDates(dateString1, dateString2):
    date1 = datetime.datetime.fromisoformat(dateString1)
    date2 = datetime.datetime.fromisoformat(dateString2)
    
    diff = 0
    if(date1 >= date2):
        diff = date1 - date2
    else:
        diff = date2 - date1

    if(dateString1 == dateString2 or diff.total_seconds() <= 1.000):
        return True
    return False