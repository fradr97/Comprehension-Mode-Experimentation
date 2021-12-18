import csv
import dateTime as dt

def globalBandsAndAU(frequencyAndAUFilePath, outputFilePath):
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

    outputFile = open(outputFilePath, 'w', newline='')
    writer = csv.writer(outputFile)
    
    header = ["AU01", "AU02", "AU04", "AU05", "AU06", "AU07", "AU09",
        "AU10", "AU12", "AU14", "AU15", "AU17", "AU20", "AU23", "AU25", "AU26", "AU45",
        "Alpha", "Beta", "Engagement", "Concentration", "Workload"]

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
    alpha = 0
    beta = 0
    engagement = 0
    concentration = 0
    workload = 0

    
    START = 1 # first row is the header
    for indexOf, dataListRow in enumerate(dataList[START:], START):
        AU01_MEAN += float(dataListRow[AU_01])
        AU02_MEAN += float(dataListRow[AU_02])
        AU04_MEAN += float(dataListRow[AU_04])
        AU05_MEAN += float(dataListRow[AU_05])
        AU06_MEAN += float(dataListRow[AU_06])
        AU07_MEAN += float(dataListRow[AU_07])
        AU09_MEAN += float(dataListRow[AU_09])
        AU10_MEAN += float(dataListRow[AU_10])
        AU12_MEAN += float(dataListRow[AU_12])
        AU14_MEAN += float(dataListRow[AU_14])
        AU15_MEAN += float(dataListRow[AU_15])
        AU17_MEAN += float(dataListRow[AU_17])
        AU20_MEAN += float(dataListRow[AU_20])
        AU23_MEAN += float(dataListRow[AU_23])
        AU25_MEAN += float(dataListRow[AU_25])
        AU26_MEAN += float(dataListRow[AU_26])
        AU45_MEAN += float(dataListRow[AU_45])
        alpha += float(dataListRow[ALPHA])
        beta += float(dataListRow[BETA])
        engagement += float(dataListRow[ENGAGEMENT])
        concentration += float(dataListRow[CONCENTRATION])
        workload += float(dataListRow[WORKLOAD])
        occ += 1

    print('OCC: ' + str(occ))
    writer.writerow([AU01_MEAN / occ, AU02_MEAN / occ, AU04_MEAN / occ, AU05_MEAN / occ, AU06_MEAN / occ, 
        AU07_MEAN / occ, AU09_MEAN / occ, AU10_MEAN / occ, AU12_MEAN / occ, AU14_MEAN / occ, AU15_MEAN / occ, AU17_MEAN / occ,
        AU20_MEAN / occ, AU23_MEAN / occ, AU25_MEAN / occ, AU26_MEAN / occ, AU45_MEAN / occ,
        alpha / occ, beta / occ, engagement / occ, concentration / occ, workload / occ])

    outputFile.close()