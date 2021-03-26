import pandas as pd
import matplotlib.pyplot as plt
from utils import crossValidation
from utils import desempenho
from utils import higherValue
from utils import getDescritiveStatistics
from utils import plotByValues
from utils import replaceEmptyValues
from utils import correctPredictions
from utils import intervalProb
from utils import createPDF

# Retorna fraseologia com os dados descritivos

def displayOutput(data, columnName):
    print(f"Média da coluna {columnName}: {data['mean']:.2f}")
    print(f"Desvio Padrão da coluna {columnName}: {data['std_deviation']:.2f}")
    print(f"Valor mais comum da coluna {columnName}: {data['most_common']:.2f}")
    print(f"Variância da coluna {columnName}: {data['variance']:.2f}")
    print('\n')


def main():

    # Extrai os dados da planilha, de acordo com a aba especificada

    data = pd.read_excel (r'teste_smarkio_Lbs.xls', sheet_name='Análise_ML')
    
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

    resultPredictionsOrig = correctPredictions.prediction(dfPred, dfTrueClass)
    resultPredictionsReplace = correctPredictions.prediction(dfPred, dfReplace)

    # Retorna o valor que houve maior e menor quantidade de predição 

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
    createPDF.createPDF( "Média da coluna Pred_class: " + str(resultPredClass['mean']))
    displayOutput(resultProb, 'probabilidade')
    displayOutput(resultTrueClass, 'True_class')
    displayOutput(resultReplace, 'True_class após substituição dos valores nulos')

    higher = [0] * 5
    higher[0] = intervalProb.getIntervalProb(dfProb, 0.5)
    higher[1] = intervalProb.getIntervalProb(dfProb, 0.6)
    higher[2] = intervalProb.getIntervalProb(dfProb, 0.7)
    higher[3] = intervalProb.getIntervalProb(dfProb, 0.8)
    higher[4] = intervalProb.getIntervalProb(dfProb, 0.9)

    # Analisa o modelo com cross-validation K-fold para verificar a corretude dos campos 'revision'

    crossValidation.getByColumns(dfStatus, dfPred, dfReplace)

    # Retorna a precisão do modelo original

    accuracy = desempenho.calcDesempenho(dfReplace, dfPred)
    print(f"\nPrecisão do modelo: {accuracy*100:.2f}%")

    # Retorna o Mean Absolute Error do modelo original

    meanAbsoluteError = desempenho.meanAbsoluteError (dfPred, dfReplace)
    print(f"\nDesempenho do modelo por Mean Absolute Error: {100 - meanAbsoluteError:.2f}%")

    # Retorna a acurácia do modelo

    accuracyScore = desempenho.accuracyScore(dfPred, dfReplace)
    print(f"\nDesempenho do modelo por Acurácia: {accuracyScore*100:.2f}%")

    # Plota gráficos de acordo com os valores passados

    plotByValues.plotGraph([countPredicted[0][1][0], countPredicted[0][1][1]], [str(countPredicted[0][0][0]), str(countPredicted[0][1][0])], 'Valor', 'Vezes', 'Valores de maior e menor predição', 'green', True, False)
    plotByValues.plotGraph([countPredicted[1][0][1], countPredicted[1][1][1]], [str(countPredicted[1][0][0]), str(countPredicted[1][1][0])], 'Valor', 'Vezes', 'Valores de maior e menor predição', 'red', True, False)
    plotByValues.plotGraph(higher, ['50%', '60%', '70%', '80%', '90%'], 'Porcentagem', 'Quantidade de acertos', 'Variação da Probabilidade de Acerto', 'blue', False, True)
    plotByValues.plotGraph([countPredicted[2], countPredicted[3]], ['Acertos', 'Erros'], 'Acertos e Erros', 'Quantidade', 'Comparativo entre Acertos e Erros', 'blue', True, True)
    
if __name__ == "__main__":
    main()