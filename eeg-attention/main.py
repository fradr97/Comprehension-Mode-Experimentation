import datetime
import computeFrequency as cf

def main():
    dateTimeCreationFile = datetime.datetime(2021,11,25,15,40,48,0)
    inputFilePath = 'C:\\Users\\Francesco\\Desktop\\caschetto.csv'
    outputFilePath = 'C:\\Users\\Francesco\\Desktop\\output.csv'
    cf.compute(dateTimeCreationFile, inputFilePath, outputFilePath)


"""
    a = datetime.datetime(100,1,1,11,34,59)
    b = a + datetime.timedelta(0,1093.1283) # days, seconds, then other fields.
    print(a.time())
    print(b.time())"""


if __name__ == '__main__':
    main()

