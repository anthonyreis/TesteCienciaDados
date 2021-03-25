from sklearn.linear_model import RidgeCV
from sklearn.model_selection import train_test_split
import pandas as pd

# Aplica cross-validation K-fold, analisando a predição dos dados com a flag 'revision'

def crossValidationKFold(dataExpected, dataPredicted, dataFrame1, dataFrame2):

    expectedFrame = pd.DataFrame.from_dict(dataExpected, orient='index')
    #predictedFrame = pd.DataFrame.from_dict(dataPredicted, orient='index')

    x = dataFrame1

    y = dataFrame2

    train_X, test_X, train_y, test_y = train_test_split(x, y, test_size=0.2, random_state=0)

    regressor = RidgeCV(alphas=[1, 1e3, 1e6], store_cv_values=True)
    regressor.fit(train_X, train_y)

    predict_y = regressor.predict(expectedFrame)

    i = 0

    for row in expectedFrame.T.iteritems():
        print(f"Esperado: {row[1][0]} - Obtido: {predict_y[i][0]:.2f}")
        i +=1

# Separa os dados com a flag 'revision' dos demais

def getByColumns(dataFrame, valueExpected, valuePredicted):
    dataExpected = {}
    dataPredicted = {}
    i = 0

    for row in dataFrame.T.iteritems():
        if(row[1][0] == 'revision'):
            dataExpected[i] = valueExpected.iat[row[0], 0]
            dataPredicted[i] = valuePredicted.iat[row[0], 0]
            i += 1
            
    crossValidationKFold(dataExpected, dataPredicted, valueExpected, valuePredicted)