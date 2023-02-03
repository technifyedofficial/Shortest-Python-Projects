from PyPDF2 import PdfFileMerger
merging = PdfFileMerger()
PDFs = ['ppf0.pdf', 'ppf1.pdf']
for PDF in PDFs:
    merging.append(PDF)
merging.write("merged.pdf")
merging.close()