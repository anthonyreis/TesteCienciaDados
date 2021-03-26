import matplotlib.pyplot as plt
import os

# Salva uma figura do gráfico de acordo com os parâmetros fornecidos

def plotGraph(values, ticks, xLabel, yLabel, title, color, bar, new):

    if(new):
        plt.figure(figsize=(15, 9))

    if(bar):
        plt.bar(ticks, values, color=color)
    else:
        plt.plot(ticks, values, color=color)
    
    font1 = {'family':'serif','color':'black','size':19}
    font2 = {'family':'serif','color':'black','size':15}

    plt.xticks(rotation=360)
    plt.xlabel(xLabel, fontdict=font2)
    plt.ylabel(yLabel, fontdict=font2)
    plt.title(title, fontdict=font1)
    file_name = xLabel + '.svg'
    
    my_path = os.path.abspath('graficos/')
    
    plt.savefig(os.path.join(my_path, file_name), dpi=800)