import PyPDF2
import sys

input = sys.argv[1:]

def filetocombine(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in (pdf_list):
        merger.append(pdf)
    merger.write('super.pdf')

filetocombine(input)