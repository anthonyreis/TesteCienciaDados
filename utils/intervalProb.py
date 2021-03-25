# Retorna quantas predições tiveram uma probabilidade maior ou igual a passada para a função

def getIntervalProb(dataFrame, probValue):
    qtd = 0

    for row in dataFrame.T.iteritems():
        if(row[1][0] >= probValue):
            qtd += 1

    return qtd