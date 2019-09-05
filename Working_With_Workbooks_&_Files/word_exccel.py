from xlrd import open_workbook
from xlwt import Workbook
import json,urllib.request
import math
import xlsxwriter								#NAME OF INPUT FILE CONTAINING ONE SHEET
import re	
workbook = xlsxwriter.Workbook('questions.xlsx')										#NAME OF GENERATED FILE
worksheet = workbook.add_worksheet()
wb = open_workbook('intellify_data.xlsx')														#NAME OF INPUT FILE CONTAINING ONE SHEET
wb_sheet_name="Sheet1"	

file = open("temp.txt", "r")
myList=file.readlines()
j=0
i=0
while(i!=len(myList)):
	string=myList[i]
	print(string)
	j=j+1
	i=i+1
	temp=""
	if(string[0].isdigit()):
		temp=""
		i=i-1
		while(not(string[0]=='a' and string[1]=='.') and i!=len(myList)-1):
			temp+=string
			i=i+1
			string=myList[i]
		worksheet.write(j,0,temp) 		
	if(string[0]=='a' and string[1]=='.' ):
		temp=""
		while(not(string[0]=='b' and string[1]=='.') and i!=len(myList)-1):
			temp+=string
			i=i+1
			string=myList[i]
		worksheet.write(j,1,temp)
		print(temp)
	if(string[0]=='b' and string[1]=='.'):
		temp=""
		while(not(string[0]=='c' and string[1]=='.') and i!=len(myList)-1):
			temp+=string
			i=i+1
			string=myList[i]	
		worksheet.write(j,2,temp)
		print(temp)
	if(string[0]=='c' and string[1]=='.'):
		temp=""
		while(not(string[0]=='d' and string[1]=='.') and i!=len(myList)-1):
			temp+=string
			i=i+1
			string=myList[i]
		worksheet.write(j,3,temp)
		print(temp)
	if(string[0]=='d' and string[1]=='.'):
		temp=""
		while(not(string[0].isdigit()) and i!=len(myList)-1):
			temp+=string
			i=i+1
			string=myList[i]	
		worksheet.write(j,4,temp)
		print(temp)
