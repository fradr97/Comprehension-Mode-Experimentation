import datetime
import computeFrequency as cf
import mergeDatasets as md

def main():
    """ Execute First: Calculates frequency bands from the output of the DSI-7 headset """
    """ Insert dateTime and remove (manually) details from caschetto csv file, then execute this commands """

    dateTime = '2021-12-06 17:06:50'.replace('/', '-')
    year = int(dateTime[0:4])
    month = int(dateTime[5:7])
    day = int(dateTime[8: 10])
    hour = int(dateTime[11:13])
    min = int(dateTime[14:16])
    sec = int(dateTime[17:19])

    basePath = 'C:\\Users\\Francesco\\Desktop\\Sperimentazione'
    user = '\\3. Albanese'
    task = '\\task6'
    finalFolder = '\\Final'

    dateTimeCreationFile = datetime.datetime(year, month, day, hour, min, sec, 0)
    inputFilePath = basePath + user + task + finalFolder + '\\jonathan6_filtered.csv'
    bandsFilePath = basePath + user + task + finalFolder + '\\andrea_filtered.csv'
    #cf.compute(dateTimeCreationFile, inputFilePath, bandsFilePath)


    """ *************************************************************** """
    """****** Execute Third: Merge OF output and output of the DSI-7 headset ******"""
    openFaceFilePath = basePath + user + task + finalFolder + '\\openface.csv'
    outputFilePath = basePath + user + task + finalFolder + '\\bandsOF.csv'

    #md.merge(openFaceFilePath, bandsFilePath, outputFilePath)

    import meanAUsHalfSecond as m
    output = basePath + user + task + finalFolder + '\\final.csv'

    #m.AUMeanHalfSecond(outputFilePath, output)
    
    """ """
    import mergePopup as mp
    popupFilePath = basePath + user + task + '\\Data\\Plugin\\comprehension-mode-attention.csv'
    finalOutput = basePath + user + task + finalFolder + '\\complete-dataset.csv'

    #mp.merge(output, popupFilePath, finalOutput)


    """ Mean of bands and Action Units """
    import meanBandsAndAUs as mba
    inputFilePath = basePath + user + task + finalFolder + '\\complete-dataset.csv'
    meanFileOutput = basePath + user + task + finalFolder + '\\mean-dataset.csv'

    #mba.globalBandsAndAU(inputFilePath, meanFileOutput)


if __name__ == '__main__':
    main()