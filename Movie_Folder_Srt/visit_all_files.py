import glob
import os
for files in glob.iglob("./" + '**/*', recursive=True):
	 index=files.find("GOT_")
	 if(not index == -1):
	 	print(files)
	 	ext=os.path.splitext(files)[1]
	 	new=files[:index]+"GOT_1)"+ext
	 	os.rename(files, new)
