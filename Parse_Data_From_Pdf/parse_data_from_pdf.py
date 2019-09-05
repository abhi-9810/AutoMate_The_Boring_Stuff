from xlrd import open_workbook
from xlwt import Workbook
import json,urllib.request
import math
import xlsxwriter								
import re

#scrape data from a pdf	
workbook = xlsxwriter.Workbook('emails.xlsx')										
worksheet = workbook.add_worksheet()
import PyPDF2
import re
pdf_file = open('principaldetails.pdf', 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)
number_of_pages = read_pdf.getNumPages()
print(number_of_pages)
row_o=0
for i in range(0,30):
    page = read_pdf.getPage(i)
    page_content = page.extractText()
    page_content = page_content.replace('\n', '').replace('\r', '')
    m=[m.start() for m in re.finditer('Email:', page_content)]
    l=len(page_content)
    #print(page_content)
    
    for index in m:
        i=index
        while True:
            if(page_content[i-4:i]=='.com' or page_content[i-4:i]=='.org' or page_content[i-4:i]=='.edu' or page_content[i-3:i]=='.in' or i>=l or page_content[i-4:i]=='.net'):
                email=page_content[index+6:i]
                print(email)
                worksheet.write(row_o,0,email)
                row_o+=1
                break
            i+=1
workbook.close()
