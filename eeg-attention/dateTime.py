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