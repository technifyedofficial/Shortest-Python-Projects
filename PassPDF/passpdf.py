from PyPDF2 import PdfFileWriter, PdfFileReader
output, pdfFile= PdfFileWriter(), PdfFileReader("iesc112.pdf")
n = pdfFile.numPages
for index in range(n):
	pages = pdfFile.getPage(index)
	output.addPage(pages)
passW = input("Enter Password: ")
output.encrypt(passW)
with open("encrypted.pdf", "wb") as F:
	output.write(F)
