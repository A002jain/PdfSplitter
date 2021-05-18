from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileWriter
from PyPDF2 import PdfFileMerger
from pdf.utils import get_out_pdf_name


def _split(input_pdf, output_pdf, startPage, lastPage):
    pdf_file = PdfFileReader(input_pdf)
    pdfWriter = PdfFileWriter()
    for i in range(startPage - 1, lastPage):
        pdfWriter.addPage(pdf_file.getPage(i))
    outputPdf = open(output_pdf, mode='wb')
    pdfWriter.write(outputPdf)
    outputPdf.close()


def _merge(pdf_file_lists, out_file_path):
    merger = PdfFileMerger()
    for pdf_file in pdf_file_lists:
        merger.append(PdfFileReader(open(pdf_file, mode='rb')))
    merger.write(out_file_path)
    merger.close()


def split(input_pdf):
    for pdf_file in input_pdf:
        try:
            output_pdf = get_out_pdf_name()
            startPage = int(input("Start Page No.: "))
            lastPage = int(input("Last Page No.: "))
            if startPage <= lastPage:
                pass
                _split(pdf_file, output_pdf, startPage, lastPage)
            else:
                print("start page is greater than last page, YOU DUMB ASS")
        except ValueError:
            print("Enter Number")


def merge(pdf_file_lists):
    out_path = get_out_pdf_name()
    _merge(pdf_file_lists, out_path)

