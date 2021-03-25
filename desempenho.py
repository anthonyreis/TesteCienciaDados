import pandas as pd
import statistics as st
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import log_loss

# Retorna a precisão do modelo

def calcDesempenho(dataFrame1, dataFrame2):
    qtdAcertos = 0
    qtdTotal = 0

    for row in dataFrame1.T.iteritems():
        if(row[1][0] == dataFrame2.iat[row[0], 0]):
            qtdAcertos += 1
        
        qtdTotal += 1

    return qtdAcertos/qtdTotal

# Retorna o Mean Absolute Error do modelo

def meanAbsoluteError(predicted, expected):
    meanAbsoluteError = mean_absolute_error(expected, predicted)

    return meanAbsoluteError

def logLoss(predicted, expected):
    print(predicted)
    log = log_loss(expected, predicted, eps=1e-15)

    return log