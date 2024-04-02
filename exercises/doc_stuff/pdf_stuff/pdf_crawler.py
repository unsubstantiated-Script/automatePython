import PyPDF2

pdf_file = open('meetingminutes1.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

page = pdf_reader.pages[0]
text = page.extract_text()

print(text)

