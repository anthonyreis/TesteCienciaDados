import pandas as pd
import argparse
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from utils import transformToList

def sentencePredict(model, sentence):
    result = model.predict(sentence)

    return result[0]

def setArgs():
    parser = argparse.ArgumentParser(description='Informe uma letra de música para classificá-la entre Beyoncé ou Rihanna')
    parser.add_argument('letra', help='Letra da música')
    args = parser.parse_args()

    return args.letra


def main():
    letra = setArgs()

    data = pd.read_excel (r'teste_smarkio_Lbs.xls', sheet_name='NLP')

    dfLetra = pd.DataFrame(data, columns= ['letra'])
    dfArtista = pd.DataFrame(data, columns= ['artista'])

    model = make_pipeline(TfidfVectorizer(), MultinomialNB())

    listaLetra = [0] * len(dfLetra)
    listaArtista = [0] * len(dfArtista)

    df_list_letra = dfLetra.values.tolist()
    df_list_artista = dfArtista.values.tolist()

    resultList = transformToList.transformList(listaLetra, df_list_letra, listaArtista, df_list_artista)

    model.fit(resultList[0], resultList[1])

    predicted = sentencePredict(model, [letra])

    print(predicted)
    

if __name__ == "__main__":
    main()