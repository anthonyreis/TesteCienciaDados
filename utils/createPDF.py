from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import A4, landscape
from svglib.svglib import svg2rlg

from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm

def createPDF(trueClassOrig, trueClassRep, predClass, prob, countPredicted, resultPredictionsOrig, resultPredictionsReplace, accuracy, meanAbsoluteError, accuracyScore, resultValidation):

    doc = SimpleDocTemplate("pdf/Resultados_Automatico.pdf",pagesize=landscape(A4),
                            rightMargin=72,leftMargin=72,
                            topMargin=72,bottomMargin=18)

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER))

    Story=[]

    ptext = '''
    <strong><font size=15>Resultados</font></strong><br/><br/><br/><br/>
    <font size=14><seq>. </seq> Dados descritivos inferidos sobre cada coluna</font> <br/><br/><br/><br/>
    '''
    Story.append(Paragraph(ptext, styles["Normal"]))

    ptext='''
    <font size=13><bullet>&bull;</bullet>Coluna True_class (antes da substituição dos valores nulos)</font><br/>
    '''
    Story.append(Paragraph(ptext, styles["Bullet"]))

    ptext=(f"<bullet>&bull;</bullet>Média: {trueClassOrig['mean']:.2f}<br/>")
    Story.append(Paragraph(ptext, styles["Bullet"]))

    ptext= (f"<bullet>&bull;</bullet>Desvio Padrão: {trueClassOrig['std_deviation']:.2f}<br/>")
    Story.append(Paragraph(ptext, styles["Bullet"]))

    ptext = (f"<bullet>&bull;</bullet>Valor mais comum: {trueClassOrig['most_common']:.2f}<br/>")
    Story.append(Paragraph(ptext, styles["Bullet"]))

    ptext = (f"<bullet>&bull;</bullet>Variância: {trueClassOrig['variance']:.2f}<br/><br/><br/>")
    Story.append(Paragraph(ptext, styles["Bullet"]))


    ptext = '''
    <font size=13><bullet>&bull;</bullet>Coluna True_class (após a substituição dos valores nulos)</font><br/>
    '''
    Story.append(Paragraph(ptext, styles["Bullet"]))

    ptext=(f"<bullet>&bull;</bullet>Média: {trueClassRep['mean']:.2f}<br/>")
    Story.append(Paragraph(ptext, styles["Bullet"]))

    ptext= (f"<bullet>&bull;</bullet>Desvio Padrão: {trueClassRep['std_deviation']:.2f}<br/>")
    Story.append(Paragraph(ptext, styles["Bullet"]))

    ptext = (f"<bullet>&bull;</bullet>Valor mais comum: {trueClassRep['most_common']:.2f}<br/>")
    Story.append(Paragraph(ptext, styles["Bullet"]))

    ptext = (f"<bullet>&bull;</bullet>Variância: {trueClassRep['variance']:.2f}<br/><br/><br/>")
    Story.append(Paragraph(ptext, styles["Bullet"]))

    ptext = '''
    <font size=13><bullet>&bull;</bullet>Coluna Pred_class</font><br/>
    '''
    Story.append(Paragraph(ptext, styles["Bullet"]))
    
    ptext=(f"<bullet>&bull;</bullet>Média: {predClass['mean']:.2f}<br/>")
    Story.append(Paragraph(ptext, styles["Bullet"]))

    ptext= (f"<bullet>&bull;</bullet>Desvio Padrão: {predClass['std_deviation']:.2f}<br/>")
    Story.append(Paragraph(ptext, styles["Bullet"]))

    ptext = (f"<bullet>&bull;</bullet>Valor mais comum: {predClass['most_common']:.2f}<br/>")
    Story.append(Paragraph(ptext, styles["Bullet"]))

    ptext = (f"<bullet>&bull;</bullet>Variância: {predClass['variance']:.2f}<br/><br/><br/>")
    Story.append(Paragraph(ptext, styles["Bullet"]))


    ptext = '''
    <font size=13><bullet>&bull;</bullet>Coluna probabilidade</font><br/>
    '''
    Story.append(Paragraph(ptext, styles["Bullet"]))

    ptext=(f"<bullet>&bull;</bullet>Média: {prob['mean']:.2f}<br/>")
    Story.append(Paragraph(ptext, styles["Bullet"]))

    ptext= (f"<bullet>&bull;</bullet>Desvio Padrão: {prob['std_deviation']:.2f}<br/>")
    Story.append(Paragraph(ptext, styles["Bullet"]))

    ptext = (f"<bullet>&bull;</bullet>Valor mais comum: {prob['most_common']:.2f}<br/>")
    Story.append(Paragraph(ptext, styles["Bullet"]))

    ptext = (f"<bullet>&bull;</bullet>Variância: {prob['variance']:.2f}<br/><br/><br/>")
    Story.append(Paragraph(ptext, styles["Bullet"]))

    ptext = '''
    <font size=14><seq>. </seq> Dados descritivos inferidos sobre o modelo</font> <br/><br/><br/><br/>
    '''
    Story.append(Paragraph(ptext, styles["Bullet"]))

    ptext= (f'<bullet>&bull;</bullet>Valor que houve mais predições corretas: {countPredicted[0][0][0]} ({countPredicted[0][0][1]}x)<br/>')
    Story.append(Paragraph(ptext, styles["Bullet"]))

    ptext= (f'<bullet>&bull;</bullet>Valor que houve menos predições corretas: {countPredicted[0][1][0]} ({countPredicted[0][1][1]}x)<br/>')
    Story.append(Paragraph(ptext, styles["Bullet"]))

    ptext = (f'<bullet>&bull;</bullet>Valor que houve mais predições incorretas: {countPredicted[1][0][0]} ({countPredicted[1][0][1]}x)<br/>')
    Story.append(Paragraph(ptext, styles["Bullet"]))

    ptext = (f'<bullet>&bull;</bullet>Valor que houve menos predições incorretas: {countPredicted[1][1][0]} ({countPredicted[1][1][1]}x)<br/>')
    Story.append(Paragraph(ptext, styles["Bullet"]))

    ptext = (f'<bullet>&bull;</bullet>Predições corretas feitas pelo modelo original:  {resultPredictionsOrig}<br/>')
    Story.append(Paragraph(ptext, styles["Bullet"]))

    ptext = (f'<bullet>&bull;</bullet>Predições corretas feitas pelo modelo após substituição dos valores nulos:  {resultPredictionsReplace}<br/><br/><br/>')
    Story.append(Paragraph(ptext, styles["Bullet"]))

    ptext = (f"<bullet>&bull;</bullet>Predições corretas dos valores de 'revision': {resultValidation[0]} do total de {resultValidation[1]}<br/><br/><br/>")
    Story.append(Paragraph(ptext, styles["Bullet"]))

    ptext = '''
    <br/><br/><br/><font size=14><seq>. </seq> Gráficos Gerados</font> <br/><br/>
    '''

    Story.append(Paragraph(ptext, styles["Bullet"]))

    img = svg2rlg('graficos/Acertos e Erros.svg')

    im = Image(img, 680, 493)
    Story.append(im)

    img = svg2rlg('graficos/Porcentagem.svg')


    im = Image(img, 680, 493)
    Story.append(im)

    img = svg2rlg('graficos/Valor.svg')

    im = Image(img)
    Story.append(im)

    ptext = '''
    <br/><br/><br/><br/>
    '''
    Story.append(Paragraph(ptext, styles["Bullet"]))


    ptext = '''
    <font size=14><seq>. </seq>Métricas de Desempenho</font><br/><br/><br/>
    '''
    Story.append(Paragraph(ptext, styles["Bullet"]))

    ptext = (f'''
    No geral foi alcançada uma precisão que pode ser considerada satisfatória, 
    dado o tamanho reduzido de dados disponíveis no modelo. 
    Segundo a precisão e a acurácia foi obtido um desempenho de {accuracy*100:.2f}% de acerto nas predições, 
    sua igualdade se deve ao fato de o modelo possivelmente não possuir divergências com falsos positivos e falsos negativos, 
    que poderiam interferir no valor da acurácia. Então pode-se assumir que o modelo tem um grau de confusão baixo. 
    Enquanto que o Mean Absolute Error aponta uma taxa de acerto de {100 - meanAbsoluteError:.2f}%, 
    assim sendo possível inferir que o modelo mesmo errando ainda prediz valores próximos aos esperados. 
    Quanto ao que pode ter interferido no alcance de um resultado melhor, 
    deve ser considerado o tamanho da base de dados e também os campos vazios.<br/><br/><br/>
    ''')

    Story.append(Paragraph(ptext, styles["Normal"]))

    ptext=(f'<font size=13><bullet>&bull;</bullet>Precisão: ({accuracy*100:.2f}%)</font><br/><br/>')
    Story.append(Paragraph(ptext, styles["Bullet"]))

    ptext = '''
    A precisão é a métrica mais simples de se utilizar para medir o desempenho, 
    sendo simplesmente feita pela divisão da quantidade de acertos pela quantidade total de elementos.<br/><br/><br/>
    '''
    Story.append(Paragraph(ptext, styles["Bullet"]))

    ptext= (f'<font size=14><bullet>&bull;</bullet>Mean Absolute Error: ({100 - meanAbsoluteError:.2f}%)</font><br/><br/>')
    Story.append(Paragraph(ptext, styles["Bullet"]))

    ptext='''
    Outro método utilizado para calcular a precisão foi o Mean Absolute Error (Erro Médio Absoluto). 
    Seu cálculo se dá por: Erro Absoluto = |Valor Esperado - Valor Obtido| e ao final é calculada a média entre todos erros.<br/><br/><br/>
    '''
    Story.append(Paragraph(ptext, styles["Bullet"]))

    ptext = (f'<font size=14><bullet>&bull;</bullet>Acurácia: ({accuracyScore*100:.2f}%)</font><br/><br/>')
    Story.append(Paragraph(ptext, styles["Bullet"]))

    ptext = '''
    A acurácia pode ser confundida com a precisão, porém seus cálculos diferem, enquanto a precisão apenas divide os acertos pelo total, 
    a acurácia leva em conta para realizar os cálculos os positivos, negativos, falsos positivos que são predições dadas como corretas quando estavam erradas e falsos negativos que são tidas como erradas quando na verdade estão corretas.
    Segue a fórmula: (P + N) / (P + N + FP + FN)<br/>
    ''' 
    Story.append(Paragraph(ptext, styles["Bullet"]))

    ptext = '''
    Sendo P os valores de predições corretas, N de predições incorretas, FP os Falsos Positivos e FN os Falsos Negativos.
    '''
    Story.append(Paragraph(ptext, styles["Bullet"]))

    doc.build(Story)