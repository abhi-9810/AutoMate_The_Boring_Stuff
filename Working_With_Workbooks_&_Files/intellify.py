from xlrd import open_workbook
from xlwt import Workbook
import json,urllib.request
import math
import xlsxwriter								#NAME OF INPUT FILE CONTAINING ONE SHEET
import re	
workbook = xlsxwriter.Workbook('irsc_data.xlsx')										#NAME OF GENERATED FILE
worksheet = workbook.add_worksheet()
wb = open_workbook('irsc.xlsx')														#NAME OF INPUT FILE CONTAINING ONE SHEET
wb_sheet_name="Sheet2"	


def split(value,row_o):
	school = re.compile(r'isco_\d\d\d\d')
	matchObj = school.search(value)
    
	if matchObj:
	    school_id=matchObj.group()
	    worksheet.write(row_o,0,school_id)

					
#starting point																			#DO ENTRY IN ROW WISE
for s in wb.sheets():
	if(s.name==wb_sheet_name):
		for row in range(325):
			col=0
			value  = (s.cell(row,col).value)
			print("%s" % value)
			if not value:
				continue
			j=len(value)
			print(row)
			k=-1
			while(k<j):
				if(value[k].isdecimal()):
					break

				
				k=k+1	

			if(k==j):
				worksheet.write(row,0,value)
				worksheet.write(row,1,value)
				continue
					
			temp=value[:k]
			temp1=value[k:]
			print(temp)
			print(temp1)
			worksheet.write(row,0,value)
			worksheet.write(row,1,temp)
			worksheet.write(row,2,temp1)
                        
                           
			#split(value,row)
		workbook.close()
