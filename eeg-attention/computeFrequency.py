import numpy as np
import csv
import dateTime as dt

"""
Valore di onde frequenziali al secondo 4: secondi valutati [0,4] valori da [0 a 300*4]
Al secondo 5: secondi valutati [1,5] valori da [300 a 300*5]
Al secondo 6: sec valutati [2,6] valori da [300*2 a 300*6]
"""

#Header: Time,LE,F4,C4,P4,P3,C3,F3,Trigger,Time_Offset,ADC_Status,ADC_Sequence,Event,Comments

def compute(dateTimeCreationFile, inputFilePath, outputFilePath):
    TIMELAPSE = 0

    LE = 1
    F4 = 2
    C4 = 3
    P4 = 4
    P3 = 5
    C3 = 6
    F3 = 7

    sec = 4
    fs = 300 

    LEArray = []
    F4Array = []
    C4Array = []
    P4Array = []
    P3Array = []
    C3Array = []
    F3Array = []
    absoluteArray = []
    computeBand = dict()

    outputFile = open(outputFilePath, 'w')
    writer = csv.writer(outputFile)
    
    header = ['Timestamp', 'Delta_LE', 'Theta_LE', 'Alpha_LE', 'Beta_LE', 'Gamma_LE',
    'Delta_F4', 'Theta_F4', 'Alpha_F4', 'Beta_F4', 'Gamma_F4',
    'Delta_C4', 'Theta_C4', 'Alpha_C4', 'Beta_C4', 'Gamma_C4',
    'Delta_P4', 'Theta_P4', 'Alpha_P4', 'Beta_P4', 'Gamma_P4',
    'Delta_P3', 'Theta_P3', 'Alpha_P3', 'Beta_P3', 'Gamma_P3',
    'Delta_C3', 'Theta_C3', 'Alpha_C3', 'Beta_C3', 'Gamma_C3',
    'Delta_F3', 'Theta_F3', 'Alpha_F3', 'Beta_F3', 'Gamma_F3',
    'Delta_ABS', 'Theta_ABS', 'Alpha_ABS', 'Beta_ABS', 'Gamma_ABS']
    writer.writerow(header)

    with open(inputFilePath, 'r') as file:
        dataList = list(csv.reader(file))
        index = 0
        indexFrom = (index * fs)

        while indexFrom < len(dataList):
            indexTo = fs * (sec + index)

            if indexTo >= len(dataList):
                indexTo = len(dataList) - 1

            # print('Secondi valutati: [' + str(index) + ',' + str(index + sec) + '], valori da: ' + str(indexFrom) + ' a ' + str(indexTo))

            while indexFrom <= indexTo:
                LEArray.append(float(dataList[indexFrom][LE]))
                F4Array.append(float(dataList[indexFrom][F4]))
                C4Array.append(float(dataList[indexFrom][C4]))
                P4Array.append(float(dataList[indexFrom][P4]))
                P3Array.append(float(dataList[indexFrom][P3]))
                C3Array.append(float(dataList[indexFrom][C3]))
                F3Array.append(float(dataList[indexFrom][F3]))

                absoluteArray.append(float(dataList[indexFrom][LE]))
                absoluteArray.append(float(dataList[indexFrom][F4]))
                absoluteArray.append(float(dataList[indexFrom][C4]))
                absoluteArray.append(float(dataList[indexFrom][P4]))
                absoluteArray.append(float(dataList[indexFrom][P3]))
                absoluteArray.append(float(dataList[indexFrom][C3]))
                absoluteArray.append(float(dataList[indexFrom][F3]))
                indexFrom += 1
            
            row = []

            """ Band calculation on single sensors """
            computeBand = computeBands(LEArray)
            dateTime = dt.dataCreationAddedToTimeLaps(dateTimeCreationFile, float(dataList[indexTo][TIMELAPSE]))
            row.append(dateTime)
            row.append(str(computeBand['Delta']))
            row.append(str(computeBand['Theta']))
            row.append(str(computeBand['Alpha']))
            row.append(str(computeBand['Beta']))
            row.append(str(computeBand['Gamma']))

            computeBand = computeBands(F4Array)
            row.append(str(computeBand['Delta']))
            row.append(str(computeBand['Theta']))
            row.append(str(computeBand['Alpha']))
            row.append(str(computeBand['Beta']))
            row.append(str(computeBand['Gamma']))

            computeBand = computeBands(C4Array)
            row.append(str(computeBand['Delta']))
            row.append(str(computeBand['Theta']))
            row.append(str(computeBand['Alpha']))
            row.append(str(computeBand['Beta']))
            row.append(str(computeBand['Gamma']))

            computeBand = computeBands(P4Array)
            row.append(str(computeBand['Delta']))
            row.append(str(computeBand['Theta']))
            row.append(str(computeBand['Alpha']))
            row.append(str(computeBand['Beta']))
            row.append(str(computeBand['Gamma']))

            computeBand = computeBands(P3Array)
            row.append(str(computeBand['Delta']))
            row.append(str(computeBand['Theta']))
            row.append(str(computeBand['Alpha']))
            row.append(str(computeBand['Beta']))
            row.append(str(computeBand['Gamma']))

            computeBand = computeBands(C3Array)
            row.append(str(computeBand['Delta']))
            row.append(str(computeBand['Theta']))
            row.append(str(computeBand['Alpha']))
            row.append(str(computeBand['Beta']))
            row.append(str(computeBand['Gamma']))

            computeBand = computeBands(F3Array)
            row.append(str(computeBand['Delta']))
            row.append(str(computeBand['Theta']))
            row.append(str(computeBand['Alpha']))
            row.append(str(computeBand['Beta']))
            row.append(str(computeBand['Gamma']))

            """ Band calculation on all sensors """
            computeBand = computeBands(absoluteArray)
            row.append(str(computeBand['Delta']))
            row.append(str(computeBand['Theta']))
            row.append(str(computeBand['Alpha']))
            row.append(str(computeBand['Beta']))
            row.append(str(computeBand['Gamma']))

            writer.writerow(row)
            LEArray.clear()
            F4Array.clear()
            C4Array.clear()
            P4Array.clear()
            P3Array.clear()
            C3Array.clear()
            F3Array.clear()
            absoluteArray.clear()
            
            index += 1
            indexFrom = (index * fs)
    outputFile.close()


""" TODO: l'array alla fine non avrà mai 1200 valori, pertanto non riesce a calcolare la media!! Onda Alpha: NaN """
def computeBands(data):
    fs = 300

    # Sampling rate (300 Hz)
    # Get real amplitudes of FFT (only in postive frequencies)
    fft_vals = np.absolute(np.fft.rfft(data))

    # Get frequencies for amplitudes in Hz
    fft_freq = np.fft.rfftfreq(len(data), 1.0/fs)

    # Define EEG bands
    eeg_bands = {'Delta': (0, 4),
                'Theta': (4, 8),
                'Alpha': (8, 12),
                'Beta': (12, 30),
                'Gamma': (30, 45)}

    # Take the mean of the fft amplitude for each EEG band
    eeg_band_fft = dict()
    for band in eeg_bands:  
        freq_ix = np.where((fft_freq >= eeg_bands[band][0]) & 
                        (fft_freq <= eeg_bands[band][1]))[0]
        eeg_band_fft[band] = np.mean(fft_vals[freq_ix])

    return eeg_band_fft


"""
# Plot the data (using pandas here cause it's easy)
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(columns=['band', 'val'])
df['band'] = eeg_bands.keys()
df['val'] = [eeg_band_fft[band] for band in eeg_bands]
ax = df.plot.bar(x='band', y='val', legend=False)
ax.set_xlabel("EEG band")
ax.set_ylabel("Mean band Amplitude")"""