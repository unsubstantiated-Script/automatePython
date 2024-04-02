import docx

d = docx.Document('demo.docx')
p = d.paragraphs[1]

r1 = p.runs[0].text
r2 = p.runs[1].text
r3 = p.runs[2].text
r4 = p.runs[3].text

print(r1, r2, r3, r4)
