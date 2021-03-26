# Transforma os dados em listas

def transformList(listaLetra, df_list_letra, listaArtista, df_list_artista):
    i = 0
    j = 0

    for item in df_list_letra:
        listaLetra[i] = str(item[0])
        i += 1

    for item in df_list_artista:
        listaArtista[j] = str(item[0])
        j += 1

    return [listaLetra, listaArtista]