from collections import Counter
import operator

# Retorna a quantidade de ocorrências cada valor

def countOccurrences(Dictvalues):
    counter = Counter(Dictvalues.values())
    
    maxValue = max(counter.items(), key=operator.itemgetter(1))[0]
    minValue = min(counter.items(), key=operator.itemgetter(1))[0]

    return [[maxValue, counter[maxValue]], [minValue, counter[minValue]]]

# Retorna quais valores obtiveram a melhor e pior taxa de acerto, e a melhor e pior taxa de erro na predição

def higherPredictedValues(dataFrame1, dataFrame2):
    valueRight = {}
    valueWrong = {}
    i = 0
    j = 0

    for row in dataFrame1.T.iteritems():
        if(row[1][0] == dataFrame2.iat[row[0], 0]):
            valueRight[i] = row[1][0]
            i += 1
        else:
            valueWrong[j] = row[1][0]
            j += 1

    valueRightCount = countOccurrences(valueRight)
    valueWrongCount = countOccurrences(valueWrong)

    return [valueRightCount, valueWrongCount, i, j]