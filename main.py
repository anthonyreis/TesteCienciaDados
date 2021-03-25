import pandas as pd
import matplotlib.pyplot as plt
import crossValidation
import desempenho
import higherValue
import getDescritiveStatistics
import plotByValues
import replaceEmptyValues

def correctPrediction(dataFrame1, dataFrame2):
    qtdAcertos = 0

    for row in dataFrame1.T.iteritems():
        if(row[1][0] == dataFrame2.iat[row[0], 0]):
            qtdAcertos += 1

    return qtdAcertos

def getIntervalProb(dataFrame, probValue):
    qtd = 0

    for row in dataFrame.T.iteritems():
        if(row[1][0] >= probValue):
            qtd += 1

    return qtd

def plotGraphByFrame(dataFrame, ticks, ylabel):
    dataFrame.plot.bar()
    plt.xticks(ticks=ticks, rotation=360)
    plt.xlabel("X")
    plt.ylabel(ylabel)
    plt.savefig(ylabel + '.png')

def displayOutput(data, columnName):
    print(f"Média da coluna {columnName}: {data['mean']:.2f}")
    print(f"Desvio Padrão da coluna {columnName}: {data['std_deviation']:.2f}")
    print(f"Valor mais comum da coluna {columnName}: {data['most_common']:.2f}")
    print(f"Variância da coluna {columnName}: {data['variance']:.2f}")
    print('\n')

def main():

    # Extrai os dados da planilha, de acordo com a aba especificada

    data = pd.read_excel (r'/home/anthonyreis/Área de Trabalho/teste_ml/teste_smarkio_Lbs.xls', sheet_name='Análise_ML')
    
    # Distribui dados da planilha, atribuindo cada coluna a uma variável

    dfPred = pd.DataFrame(data, columns= ['Pred_class'])
    dfProb = pd.DataFrame(data, columns= ['probabilidade'])
    dfTrueClass = pd.DataFrame(data, columns= ['True_class'])
    dfStatus = pd.DataFrame(data, columns= ['status'])

    # Extrai informações relevantes dos dados, como média, variância desvio padrão e valor mais comum

    resultPredClass = getDescritiveStatistics.getStatistics(dfPred['Pred_class'])
    resultProb = getDescritiveStatistics.getStatistics(dfProb['probabilidade'])
    resultTrueClass = getDescritiveStatistics.getStatistics(dfTrueClass['True_class'])

    # Substitui os valores nulos da coluna de Predição pelos da coluna de valores esperados

    dfReplace = replaceEmptyValues.replaceValues(dfTrueClass, dfPred)
    resultReplace = getDescritiveStatistics.getStatistics(dfReplace[0])

    # Retorna a quantidade de predições correta, antes e após a substituição dos valores nulos

    resultPredictionsOrig = correctPrediction(dfPred, dfTrueClass)
    resultPredictionsReplace = correctPrediction(dfPred, dfReplace)

    # 

    countPredicted = higherValue.higherPredictedValues(dfPred, dfReplace)

    print(f'Valor que houve mais predições corretas: {countPredicted[0][0][0]}, sendo {countPredicted[0][0][1]} vez(es)')
    print(f'Valor que houve menos predições corretas: {countPredicted[0][1][0]}, sendo {countPredicted[0][1][1]} vez(es)')
    print('\n')

    print(f'Valor que houve mais predições incorretas: {countPredicted[1][0][0]}, sendo {countPredicted[1][0][1]} vez(es)')
    print(f'Valor que houve menos predições incorretas: {countPredicted[1][1][0]}, sendo {countPredicted[1][1][1]} vez(es)')
    print('\n')

    print("Predições corretas feitas pelo modelo original: ", resultPredictionsOrig)
    print('\n')

    print("Predições corretas feitas pelo modelo após substituição dos valores nulos: ", resultPredictionsReplace)
    print('\n')

    displayOutput(resultPredClass, 'Pred_class')
    displayOutput(resultProb, 'probabilidade')
    displayOutput(resultTrueClass, 'True_class')
    displayOutput(resultReplace, 'True_class após substituição dos valores nulos')

    higher = [0] * 5
    higher[0] = getIntervalProb(dfProb, 0.5)
    higher[1] = getIntervalProb(dfProb, 0.6)
    higher[2] = getIntervalProb(dfProb, 0.7)
    higher[3] = getIntervalProb(dfProb, 0.8)
    higher[4] = getIntervalProb(dfProb, 0.9)

    crossValidation.getByColumns(dfStatus, dfPred, dfReplace)

    accuracy = desempenho.calcDesempenho(dfPred, dfReplace)
    print(f"\nDesempenho do modelo por acurácia: {accuracy*100:.2f}%")

    meanAbsoluteError = desempenho.meanAbsoluteError (dfPred, dfReplace)
    print(f"\nDesempenho do modelo por Mean Absolute Error: {100 - meanAbsoluteError:.2f}%")

    plotByValues.plotGraph([countPredicted[0][1][0], countPredicted[0][1][1]], [str(countPredicted[0][0][0]), str(countPredicted[0][1][0])], 'Valor', 'Vezes', 'Valores de maior e menor predição', 'green', True, False)
    plotByValues.plotGraph([countPredicted[1][0][1], countPredicted[1][1][1]], [str(countPredicted[1][0][0]), str(countPredicted[1][1][0])], 'Valor', 'Vezes', 'Valores de maior e menor predição', 'red', True, False)
    plotByValues.plotGraph(higher, ['50%', '60%', '70%', '80%', '90%'], 'Porcentagem', 'Quantidade de acertos', 'Variação da Probabilidade de Acerto', 'blue', False, True)
    plotByValues.plotGraph([countPredicted[2], countPredicted[3]], ['Acertos', 'Erros'], 'Acertos e Erros', 'Quantidade', 'Comparativo entre Acertos e Erros', 'blue', True, True)

    #plotGraphByFrame(dfPred, [0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650])
    
if __name__ == "__main__":
    main()