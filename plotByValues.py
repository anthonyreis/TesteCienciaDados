import matplotlib.pyplot as plt

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
    
    plt.savefig(xLabel + '.png')