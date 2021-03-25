import matplotlib.pyplot as plt
import os

# Salva uma figura do gráfico de acordo com os parâmetros fornecidos

def plotGraph(values, ticks, xLabel, yLabel, title, color, bar, new):

    if(new):
        plt.figure(figsize=(15, 6))

    if(bar):
        plt.bar(ticks, values, color=color)
    else:
        plt.plot(ticks, values, color=color)
    
    plt.xticks(rotation=360)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    file_name = xLabel + '.png'
    
    my_path = os.path.abspath('graficos/')
    
    plt.savefig(os.path.join(my_path, file_name))