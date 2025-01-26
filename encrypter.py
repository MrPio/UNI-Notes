import os
from PyPDF2 import PdfReader, PdfWriter

PDF_FOLDER='pdf/'

def encrypt_all_pdf(password):
    pdf_files = [f for f in os.listdir(PDF_FOLDER) if f.endswith('.pdf')]

    for pdf_file in pdf_files:
        path = os.path.join(PDF_FOLDER, pdf_file)
        reader = PdfReader(path)
        writer = PdfWriter()
        for page in reader.pages:
            writer.add_page(page)
        writer.encrypt(password)
        with open(path, "wb") as output_file:
            writer.write(output_file)
        print(f"Password-protected: {path}")

password=input('Password         --> ')
if password==input('Confirm password --> '):
  encrypt_all_pdf(password)
else:
  print('Password mismatch!')
