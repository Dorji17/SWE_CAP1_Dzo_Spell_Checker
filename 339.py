from docx import Document, document

def convert_docx_to_text(docx_file, text_file):
    doc = Document(docx_file)

    with open(text_file, 'w', encoding='utf-8') as text_file:
        for pragraph in doc.paragraphs:
            text_file.write(pragraph.text + '\n') 
      



convert_docx_to_text('339.docx', '339.txt')