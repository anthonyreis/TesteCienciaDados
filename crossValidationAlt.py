from sklearn.datasets import load_boston
from sklearn.linear_model import RidgeCV
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

def crossValidationKFold(dataExpected, dataPredicted):

    #data_features = pd.DataFrame(data, columns=feature_names)
    expectedFrame = pd.DataFrame.from_dict(dataExpected, orient='index')
    predictedFrame = pd.DataFrame.from_dict(dataPredicted, orient='index')

    x = expectedFrame

    y = dataPredicted

    train_X, test_X, train_y, test_y = train_test_split(x, y, test_size=0.2, random_state=0)

    regressor = RidgeCV(alphas=[1, 1e3, 1e6], store_cv_values=True)
    regressor.fit(train_X, train_y)
    cv_mse = np.mean(regressor.cv_values_, axis=0)

    # Best alpha
    print(regressor.alpha_)
    print(cv_mse)

    plt.figure(figsize=(15, 6))

    predict_y = regressor.predict(test_X)

    print(predict_y)

def getByColumns(dataFrame, valueExpected, valuePredicted):
    dataExpected = {}
    dataPredicted = {}
    i = 0

    for row in dataFrame.T.iteritems():
        if(row[1][0] == 'revision'):
            dataExpected[i] = valueExpected.iat[row[0], 0]
            dataPredicted[i] = valuePredicted.iat[row[0], 0]
            i += 1
            
    crossValidationKFold(dataExpected, dataPredicted)
    