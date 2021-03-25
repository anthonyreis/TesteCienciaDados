import pandas as pd
import math

def replaceValues(dataFrame1, dataFrame2):
    dataFrameCopy = {}
    i = 0

    for row in dataFrame1.T.iteritems():
        if (math.isnan(row[1][0])):
            dataFrameCopy[i] = dataFrame2.iat[row[0], 0]
        else:
            dataFrameCopy[i] = row[1][0]

        i += 1

    return pd.DataFrame.from_dict(dataFrameCopy, orient='index')