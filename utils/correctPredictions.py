# Retorna quantas predições foram feitas corretamente

def prediction(dataFrame1, dataFrame2):
    qtdAcertos = 0

    for row in dataFrame1.T.iteritems():
        if(row[1][0] == dataFrame2.iat[row[0], 0]):
            qtdAcertos += 1

    return qtdAcertos