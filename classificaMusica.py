import pandas as pd
import argparse
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

def SentencePredict(model, sentence):
    result = model.predict(sentence)

    return result[0]

def TransformToList(listaLetra, df_list_letra, listaArtista, df_list_artista):
    i = 0
    j = 0

    for item in df_list_letra:
        listaLetra[i] = str(item[0])
        i += 1

    for item in df_list_artista:
        listaArtista[j] = str(item[0])
        j += 1

    return [listaLetra, listaArtista]

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

    resultList = TransformToList(listaLetra, df_list_letra, listaArtista, df_list_artista)

    model.fit(resultList[0], resultList[1])

    predicted = SentencePredict(model, [letra])

    print(predicted)
    

if __name__ == "__main__":
    main()