import fitz
import json

def extrair_informacoes_pdf(pdf_path):
    pdf_document = fitz.open(pdf_path)
    informacoes = []
    print(f"Total de páginas: {pdf_document.page_count}")
    
    for page_num in range(pdf_document.page_count):
        print(f"Entrou pela {page_num}° vez")
        page = pdf_document.load_page(page_num)
        page_text: str = page.get_text("text")
        lines_text = page_text.splitlines()
        document_user = {}
        for line in lines_text:
            if ':' in line:
                split_data = line.split(':')
                document_user[split_data[0]] = split_data[1] if len(split_data) > 1 else ''
        informacoes.append(document_user)

    pdf_document.close()
    print(f"Retornou: {informacoes}")
    return informacoes

pdf_path = "Acesso.pdf"
informacoes_extraidas = extrair_informacoes_pdf(pdf_path)

with open('result.json', 'w', encoding='utf-8') as file:
    json.dump(informacoes_extraidas, file, indent=2, ensure_ascii=False)