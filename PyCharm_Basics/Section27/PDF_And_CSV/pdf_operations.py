import os
import PyPDF2
import pdfplumber

project_path = os.getcwd()
pdf_path = os.path.join(project_path, "pdf", "tutorial.pdf")

def read_pdf_properties():
    pdf = PyPDF2.PdfReader(pdf_path)
    print(pdf_path)
    print(pdf)

    num_of_pages = len(pdf.pages)
    print(f"Number of pages: {num_of_pages}")

    doc_info = pdf.metadata

    for key, value in doc_info.items():
        print(f"{key} : {value}")

def pdf_read_page(page_num=0):
    # pdfplumber -> open()

    with pdfplumber.open(pdf_path) as pdf:
        page = pdf.pages[page_num]
        content = page.extract_text()
        print(content)

def pdf_read_pages(start=0, end=1):
    # pdfplumber -> open()

    with pdfplumber.open(pdf_path) as pdf:
        for i in range(start, end + 1):
            print(f"start of page {i}")

            page = pdf.pages[i]

            content = page.extract_text()
            print(content)

            print(f"end of page {i}")

def extract_page(page_num=0):
    from PyPDF2 import PdfReader, PdfWriter
    new_pdf_path = os.path.join(project_path, "pdf", str(page_num) + ".pdf")

    pdf = PdfReader(pdf_path)

    page = pdf.pages[page_num]

    pdf_writer = PdfWriter()
    pdf_writer.add_page(page)

    with open(new_pdf_path, "wb") as result:
        pdf_writer.write(result)

def extract_pages(start=0, end=1):
    from PyPDF2 import PdfReader, PdfWriter
    new_pdf_path = os.path.join(project_path, "pdf", str(start) + "_" + str(end) + ".pdf")

    pdf = PdfReader(pdf_path)

    pdf_writer = PdfWriter()

    for i in range(start, end + 1):
        page = pdf.pages[i]

        pdf_writer.add_page(page)

    with open(new_pdf_path, "wb") as result:
        pdf_writer.write(result)

def pdf_merge(*args):
    from PyPDF2 import PdfMerger
    merger = PdfMerger()

    for arg in args:
        merger.append(arg)

    merged_pdf_path = os.path.join(project_path, "pdf", "merged_pdf.pdf")

    with open(merged_pdf_path, "wb") as merged_pdf:
        merger.write(merged_pdf)

def pdf_rotate(degree):
    from PyPDF2 import PdfReader, PdfWriter

    merged_pdf = PdfReader("pdf/merged_pdf.pdf")

    writer = PdfWriter()

    for i in range(len(merged_pdf.pages)):
        page = merged_pdf.pages[i]

        page.rotate(degree)

        writer.add_page(page)

    with open("pdf/merged_rotated_pdf.pdf", "wb") as rotated:
        writer.write(rotated)