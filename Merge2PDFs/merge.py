from PyPDF2 import PdfFileMerger
merging = PdfFileMerger()
PDFs = ['0.pdf', '1.pdf']
for PDF in PDFs:
    merging.append(PDF)
merging.write("merged.pdf")
merging.close()
