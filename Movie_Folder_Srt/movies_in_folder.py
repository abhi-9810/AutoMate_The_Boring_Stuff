import os
from os import listdir
from os.path import isfile, join
# this code was used to move all the movies and subtitles into their specific folder to organise them
files=[]
for files in listdir("./"):
	if(not files.endswith(".py")):
		folder=os.path.splitext(files)[0]
		folder=folder.replace("(", "[")
		folder=folder.replace(")", "]")
		print(folder)
		print(files+"\n")
		try:
			if(not os.path.isdir("./"+folder)):
				os.mkdir("./"+folder)
			os.rename(files, "./"+folder+"/"+files)
		except Exception as e:
				print(e)