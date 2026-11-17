from pypdf import PdfWriter

pdfs = ["archivo1.pdf", "archivo2.pdf", "archivo3.pdf"]
salida = "unido.pdf"

writer = PdfWriter()

for pdf in pdfs:
  writer.append(pdf)

writer.write(salida)
writer.close()
