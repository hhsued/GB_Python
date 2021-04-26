from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger

from pathlib import Path

pdfW = PdfFileWriter

pdf_path = (
  Path.home()
  / "source" / "repos" / "P" / "N" / "GB" / "data" / "new.pdf"
)

pdf_path = (
  Path.home()
  / "source" / "repos" / "P" / "N" / "GB" / "data" / "new.pdf"
)

output_file =(
  Path.home()
)

input_pdf = PdfFileReader(str(pdf_path))

first_page = input_pdf.getPage(0)

pdf_writer = PdfFileWriter()
pdf_writer.addPage(first_page)

pdfOutput = open('FILEOUT.pdf', 'wb')
pdf_writer.write(pdfOutput)
pdfOutput.close()

with Path("first_page2.pdf").open(mode="wb") as output_file:
  pdf_writer.write(output_file)

