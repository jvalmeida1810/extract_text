from PyPDF2 import PdfReader

def extrair_texto_pdf(acesso_pdf):
    reader = PdfReader(acesso_pdf)
    texto = ''

    for pagina_num in range(len(reader.pages)):
        pagina = reader.pages[pagina_num]
        texto += pagina.extract_text()

    return texto

acesso_pdf = 'Acesso.pdf'
texto_extraido = extrair_texto_pdf(acesso_pdf)
print(texto_extraido)