import csv
import dateTime as dt

def merge(openFaceAUsFilePath, attentionFilePath, outputFilePath):
    TIMESTAMP = 0
    ALPHA_GLOBAL = 38
    BETA_GLOBAL = 39
    ENGAGEMENT = 41
    CONCENTRATION = 42
    WORKLOAD = 43

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

    with open(openFaceAUsFilePath, 'r') as file:
        openFaceAUsDataList = list(csv.reader(file))

    with open(attentionFilePath, 'r') as file:
        attentionDataList = list(csv.reader(file))

    alpha = -1
    beta = -1
    engagement = -1
    concentration = -1
    workload = -1

    outputFile = open(outputFilePath, 'w', newline='')
    writer = csv.writer(outputFile)
    
    header = ['Timestamp', 'AU_01', 'AU_02', 'AU_04', 'AU_05', 'AU_06',
    'AU_07', 'AU_09', 'AU_10', 'AU_12', 'AU_14', 'AU_15', 'AU_17',
    'AU_20', 'AU_23', 'AU_25', 'AU_26', 'AU_45',
    'Alpha', 'Betha', 'Engagement', 'Concentration', 'Workload',
    'Question', 'Answer', 'Score']
    writer.writerow(header)

    START_OF = 1 # first row is the header
    for indexOf, openFaceRow in enumerate(openFaceAUsDataList[START_OF:], START_OF):
        ofDate = str(dt.getDateFromString(openFaceRow[TIMESTAMP]))
        
        START_ATT = 1
        for indexAtt, attentionRow in enumerate(attentionDataList[START_ATT:], START_ATT):
            attentionDate = str(dt.getDateFromString(attentionRow[TIMESTAMP]))
            sameDates = dt.checkSameDates(ofDate, attentionDate)

            if sameDates and attentionDate <= ofDate:
                alpha = attentionRow[ALPHA_GLOBAL]
                beta = attentionRow[BETA_GLOBAL]
                engagement = attentionRow[ENGAGEMENT]
                concentration = attentionRow[CONCENTRATION]
                workload = attentionRow[WORKLOAD]

        writer.writerow([
        openFaceRow[TIMESTAMP],
        openFaceRow[AU_01],
        openFaceRow[AU_02],
        openFaceRow[AU_04],
        openFaceRow[AU_05],
        openFaceRow[AU_06],
        openFaceRow[AU_07],
        openFaceRow[AU_09],
        openFaceRow[AU_10],
        openFaceRow[AU_12],
        openFaceRow[AU_14],
        openFaceRow[AU_15],
        openFaceRow[AU_17],
        openFaceRow[AU_20],
        openFaceRow[AU_23],
        openFaceRow[AU_25],
        openFaceRow[AU_26],
        openFaceRow[AU_45],
        alpha, beta, engagement, concentration, workload])
            
    outputFile.close()
    