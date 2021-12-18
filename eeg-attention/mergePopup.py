import csv
import dateTime as dt

def merge(bandsAUFilePath, popupFilePath, outputFilePath):
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

    POPUP_QUESTION = 1
    POPUP_ANSWER = 2
    
    question = ''
    answer = ''
    

    with open(bandsAUFilePath, 'r') as file:
        bandsAUDataList = list(csv.reader(file))

    with open(popupFilePath, 'r') as file:
        popupDataList = list(csv.reader(file))

    outputFile = open(outputFilePath, 'w', newline='')
    writer = csv.writer(outputFile)
    
    header = ['Timestamp', 'AU_01', 'AU_02', 'AU_04', 'AU_05', 'AU_06',
    'AU_07', 'AU_09', 'AU_10', 'AU_12', 'AU_14', 'AU_15', 'AU_17',
    'AU_20', 'AU_23', 'AU_25', 'AU_26', 'AU_45',
    'Alpha', 'Beta', 'Engagement', 'Concentration', 'Workload',
    'Question', 'Answer', 'Score']
    writer.writerow(header)

    START_BANDS_AU = 1 # first row is the header
    for indexOf, bandsAUrow in enumerate(bandsAUDataList[START_BANDS_AU:], START_BANDS_AU):
        bandsAUDate = str(dt.getDateFromString(bandsAUrow[TIMESTAMP]))
        
        for popupRow in popupDataList:
            popupDate = str(dt.getDateFromString(popupRow[TIMESTAMP].replace('+01:00', '')))
            sameDates = dt.checkSameDates(bandsAUDate, popupDate)

            if sameDates and popupDate <= bandsAUDate:
                question = popupRow[POPUP_QUESTION]
                answer = popupRow[POPUP_ANSWER]
            
        writer.writerow([
        bandsAUrow[TIMESTAMP],
        bandsAUrow[AU_01],
        bandsAUrow[AU_02],
        bandsAUrow[AU_04],
        bandsAUrow[AU_05],
        bandsAUrow[AU_06],
        bandsAUrow[AU_07],
        bandsAUrow[AU_09],
        bandsAUrow[AU_10],
        bandsAUrow[AU_12],
        bandsAUrow[AU_14],
        bandsAUrow[AU_15],
        bandsAUrow[AU_17],
        bandsAUrow[AU_20],
        bandsAUrow[AU_23],
        bandsAUrow[AU_25],
        bandsAUrow[AU_26],
        bandsAUrow[AU_45],
        bandsAUrow[ALPHA],
        bandsAUrow[BETA],
        bandsAUrow[ENGAGEMENT],
        bandsAUrow[CONCENTRATION],
        bandsAUrow[WORKLOAD],
        question,
        answer,
        ''])

        question = ''
        answer = ''
            
    outputFile.close()
    