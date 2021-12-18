import csv
import dateTime as dt

def AUMeanHalfSecond(frequencyAndAUFilePath, outputFilePath):
    TIMESTAMP = 0
    AU_01 = 1
    AU_02 = 2
    AU_04 = 3
    AU_05 = 4
    AU_06 = 5
    AU_07 = 6
    AU_09 = 7
    AU_10 = 8
    AU_12 = 9
    AU_14 = 10
    AU_15 = 11
    AU_17 = 12
    AU_20 = 13
    AU_23 = 14
    AU_25 = 15
    AU_26 = 16
    AU_45 = 17

    ALPHA = 18
    BETA = 19
    ENGAGEMENT = 20
    CONCENTRATION = 21
    WORKLOAD = 22  

    index = 1
    SEC = 0.500

    outputFile = open(outputFilePath, 'w', newline='')
    writer = csv.writer(outputFile)
    
    header = ["Timestamp", "AU01", "AU02", "AU04", "AU05", "AU06", "AU07", "AU09",
        "AU10", "AU12", "AU14", "AU15", "AU17", "AU20", "AU23", "AU25", "AU26", "AU45",
        "Alpha", "Beta", "Engagement", "Concentration", "Workload", 'Question', 'Answer', 'Score']

    writer.writerow(header)

    with open(frequencyAndAUFilePath, 'r') as file:
        dataList = list(csv.reader(file))

    occ = 0

    AU01_MEAN = 0
    AU02_MEAN = 0
    AU04_MEAN = 0
    AU05_MEAN = 0
    AU06_MEAN = 0
    AU07_MEAN = 0
    AU09_MEAN = 0
    AU10_MEAN = 0
    AU12_MEAN = 0
    AU14_MEAN = 0
    AU15_MEAN = 0
    AU17_MEAN = 0
    AU20_MEAN = 0
    AU23_MEAN = 0
    AU25_MEAN = 0
    AU26_MEAN = 0
    AU45_MEAN = 0
    
    timestampFrom = dataList[index][TIMESTAMP]
    timestampTo = str(dt.sumTimes(dt.getDateFromString(timestampFrom), SEC))
    
    while index < len(dataList):
        if dt.getDateFromString(dataList[index][TIMESTAMP]) <= dt.getDateFromString(timestampTo):
            AU01_MEAN += float(dataList[index][AU_01])
            AU02_MEAN += float(dataList[index][AU_02])
            AU04_MEAN += float(dataList[index][AU_04])
            AU05_MEAN += float(dataList[index][AU_05])
            AU06_MEAN += float(dataList[index][AU_06])
            AU07_MEAN += float(dataList[index][AU_07])
            AU09_MEAN += float(dataList[index][AU_09])
            AU10_MEAN += float(dataList[index][AU_10])
            AU12_MEAN += float(dataList[index][AU_12])
            AU14_MEAN += float(dataList[index][AU_14])
            AU15_MEAN += float(dataList[index][AU_15])
            AU17_MEAN += float(dataList[index][AU_17])
            AU20_MEAN += float(dataList[index][AU_20])
            AU23_MEAN += float(dataList[index][AU_23])
            AU25_MEAN += float(dataList[index][AU_25])
            AU26_MEAN += float(dataList[index][AU_26])
            AU45_MEAN += float(dataList[index][AU_45])
            occ += 1
            index += 1
        else:
            timestamp = dataList[index -1][TIMESTAMP]
            alpha = dataList[index -1][ALPHA]
            beta = dataList[index -1][BETA]
            engagement = dataList[index -1][ENGAGEMENT]
            concentration = dataList[index -1][CONCENTRATION]
            workload = dataList[index -1][WORKLOAD]

            writer.writerow([timestamp, AU01_MEAN / occ, AU02_MEAN / occ, AU04_MEAN / occ, AU05_MEAN / occ, AU06_MEAN / occ, 
                AU07_MEAN / occ, AU09_MEAN / occ, AU10_MEAN / occ, AU12_MEAN / occ, AU14_MEAN / occ, AU15_MEAN / occ, AU17_MEAN / occ,
                AU20_MEAN / occ, AU23_MEAN / occ, AU25_MEAN / occ, AU26_MEAN / occ, AU45_MEAN / occ,
                alpha, beta, engagement, concentration, workload, '', '', ''])

            occ = 0
            AU01_MEAN = 0
            AU02_MEAN = 0
            AU04_MEAN = 0
            AU05_MEAN = 0
            AU06_MEAN = 0
            AU07_MEAN = 0
            AU09_MEAN = 0
            AU10_MEAN = 0
            AU12_MEAN = 0
            AU14_MEAN = 0
            AU15_MEAN = 0
            AU17_MEAN = 0
            AU20_MEAN = 0
            AU23_MEAN = 0
            AU25_MEAN = 0
            AU26_MEAN = 0
            AU45_MEAN = 0

            timestampTo = str(dt.sumTimes(dt.getDateFromString(dataList[index][TIMESTAMP]), SEC))
    outputFile.close()