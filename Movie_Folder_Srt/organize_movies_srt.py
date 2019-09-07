import os
from os import listdir
from os.path import isfile, join

for files in listdir("./"):
	if(not files.endswith(".py")):
		print(files)
		index=files.find("S01")
		temp=files[index+4:index+6]
		if(temp[0]=='0'):
			temp=temp[1:]
		name="Epi_"+temp+"(GOT_"+temp+")"
		print(name)
		folder="Episode_"+temp
		ext=os.path.splitext(files)[1]
		name=name+ext
		print(name)
		try:
			if(not os.path.isdir("./"+folder)):
				os.mkdir("./"+folder)
			os.rename(files, "./"+folder+"/"+name)
		except Exception as e:
				print(e)
		