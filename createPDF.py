from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import A4, landscape
from svglib.svglib import svg2rlg

from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm

doc = SimpleDocTemplate("Resultados_Automatico.pdf",pagesize=landscape(A4),
                        rightMargin=72,leftMargin=72,
                        topMargin=72,bottomMargin=18)

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER))

Story=[]

Story.append(Spacer(10,0))

ptext = '''
<strong><font size=15>Resultados</font></strong><br/><br/><br/><br/>
<font size=14><seq>. </seq> Dados descritivos inferidos sobre cada coluna</font> <br/><br/><br/><br/>
'''
Story.append(Paragraph(ptext, styles["Normal"]))

ptext='''
<font size=13><bullet>&bull;</bullet>Coluna True_class (antes da substituição dos valores nulos)</font><br/>
'''
Story.append(Paragraph(ptext, styles["Bullet"]))

ptext='<bullet>&bull;</bullet>Média: 38.57<br/>'
Story.append(Paragraph(ptext, styles["Bullet"]))

ptext= '<bullet>&bull;</bullet>Desvio Padrão: 39.58<br/>'
Story.append(Paragraph(ptext, styles["Bullet"]))

ptext = '<bullet>&bull;</bullet>Valor mais comum: 0.00<br/>'
Story.append(Paragraph(ptext, styles["Bullet"]))

ptext = '<bullet>&bull;</bullet>Variância: 1566.66<br/><br/><br/>'
Story.append(Paragraph(ptext, styles["Bullet"]))


ptext = '''
<font size=13><bullet>&bull;</bullet>Coluna True_class (após a substituição dos valores nulos)</font><br/>
'''
Story.append(Paragraph(ptext, styles["Bullet"]))

ptext='<bullet>&bull;</bullet>Média: 48.25<br/>'
Story.append(Paragraph(ptext, styles["Bullet"]))

ptext= '<bullet>&bull;</bullet>Desvio Padrão: 38.54<br/>'
Story.append(Paragraph(ptext, styles["Bullet"]))

ptext = '<bullet>&bull;</bullet>Valor mais comum: 74.00<br/>'
Story.append(Paragraph(ptext, styles["Bullet"]))

ptext = '<bullet>&bull;</bullet>Variância: 1485.51<br/><br/><br/>'
Story.append(Paragraph(ptext, styles["Bullet"]))

ptext = '''
<font size=13><bullet>&bull;</bullet>Coluna Pred_class</font><br/>
'''
Story.append(Paragraph(ptext, styles["Bullet"]))

ptext='<bullet>&bull;</bullet>Média: 52.71<br/>'
Story.append(Paragraph(ptext, styles["Bullet"]))

ptext= '<bullet>&bull;</bullet>Desvio Padrão: 37.60<br/>'
Story.append(Paragraph(ptext, styles["Bullet"]))

ptext = '<bullet>&bull;</bullet>Valor mais comum: 3.00<br/>'
Story.append(Paragraph(ptext, styles["Bullet"]))

ptext = '<bullet>&bull;</bullet>Variância: 1413.92<br/><br/><br/>'
Story.append(Paragraph(ptext, styles["Bullet"]))

ptext = '''
<font size=13><bullet>&bull;</bullet>Coluna probabilidade</font><br/>
'''
Story.append(Paragraph(ptext, styles["Bullet"]))

ptext='<bullet>&bull;</bullet>Média: 0.62<br/>'
Story.append(Paragraph(ptext, styles["Bullet"]))

ptext= '<bullet>&bull;</bullet>Desvio Padrão: 0.27<br/>'
Story.append(Paragraph(ptext, styles["Bullet"]))

ptext = '<bullet>&bull;</bullet>Valor mais comum: 1.00<br/>'
Story.append(Paragraph(ptext, styles["Bullet"]))

ptext = '<bullet>&bull;</bullet>Variância: 0.07<br/><br/><br/>'
Story.append(Paragraph(ptext, styles["Bullet"]))

ptext = '''
<font size=14><seq>. </seq> Dados descritivos inferidos sobre o modelo</font> <br/><br/><br/><br/>
'''
Story.append(Paragraph(ptext, styles["Bullet"]))

ptext='<bullet>&bull;</bullet>Valor que houve mais predições corretas: 74 (56x)<br/>'
Story.append(Paragraph(ptext, styles["Bullet"]))

ptext= '<bullet>&bull;</bullet>Valor que houve menos predições corretas: 48 (1x)<br/>'
Story.append(Paragraph(ptext, styles["Bullet"]))

ptext = '<bullet>&bull;</bullet>Valor que houve mais predições incorretas: 2 (14x)<br/>'
Story.append(Paragraph(ptext, styles["Bullet"]))

ptext = '<bullet>&bull;</bullet>Valor que houve menos predições incorretas: 62 (1x)<br/>'
Story.append(Paragraph(ptext, styles["Bullet"]))

ptext = '<bullet>&bull;</bullet>Predições corretas feitas pelo modelo original:  0<br/>'
Story.append(Paragraph(ptext, styles["Bullet"]))

ptext = '<bullet>&bull;</bullet>Predições corretas feitas pelo modelo após substituição dos valores nulos:  462<br/><br/><br/>'
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

ptext='<font size=13><bullet>&bull;</bullet>Precisão: (71.85%)</font><br/><br/>'
Story.append(Paragraph(ptext, styles["Bullet"]))

ptext = '''
A precisão é a métrica mais simples de se utilizar para medir o desempenho, 
sendo simplesmente feita pela divisão da quantidade de acertos pela quantidade total de elementos.<br/><br/><br/>
'''
Story.append(Paragraph(ptext, styles["Bullet"]))

ptext= '<font size=14><bullet>&bull;</bullet>Mean Absolute Error: (85.65%)</font><br/><br/>'
Story.append(Paragraph(ptext, styles["Bullet"]))

ptext='''
Outro método utilizado para calcular a precisão foi o Mean Absolute Error (Erro Médio Absoluto). 
Seu cálculo se dá por: Erro Absoluto = |Valor Esperado - Valor Obtido| e ao final é calculada a média entre todos erros.<br/><br/><br/>
'''
Story.append(Paragraph(ptext, styles["Bullet"]))

ptext = '<font size=14><bullet>&bull;</bullet>Acurácia: (71.85%)</font><br/><br/>'
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