import PyPDF2
import sys

inputs = sys.argv[2:]


def combiner(pdl_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdl_list:
        merger.append(pdf)
    merger.write('combined.pdf')
    print(f'Merged {inputs} to combined.pdf')


def watermark_func(pdf_file, watermark):
    with open(pdf_file, 'rb') as input_file, open(watermark, 'rb') as watermark_file:
        input_pdf = PyPDF2.PdfFileReader(input_file)
        watermark_pdf = PyPDF2.PdfFileReader(watermark_file)
        watermark_page = watermark_pdf.getPage(0)

        output = PyPDF2.PdfFileWriter()

        for i in range(input_pdf.getNumPages()):
            pdf_page = input_pdf.getPage(i)
            pdf_page.mergePage(watermark_page)
            output.addPage(pdf_page)

        with open('watermarked.pdf', 'wb') as merged_file:
            output.write(merged_file)
        print(f'Watermarked {pdf_file} with {watermark}')


if __name__ == '__main__':
    try:
        if sys.argv[1] == 'combine':
            combiner(inputs)
        elif sys.argv[1] == 'watermark':
            watermark_func(sys.argv[2], sys.argv[3])
    except IndexError:
        print('hi')
