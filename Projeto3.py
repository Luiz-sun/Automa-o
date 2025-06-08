#Igual o  projeto um mas fazendo com meus arquivos:#

import PyPDF2
import os

merger = PyPDF2.PdfMerger()

lista_aulas = os.listdir("Aula")
print(lista_aulas)

for aulas in lista_aulas:
    if  ".pdf"  in  aulas:
        merger.append(f"aula/{aulas}")

merger.write("Pdf AulaFinal.pdf")