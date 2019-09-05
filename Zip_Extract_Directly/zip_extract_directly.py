import os
import shutil
import zipfile
from os.path import basename
my_dir = os.getcwd()
my_zip = os.getcwd()+"\\isafe_1_online_1_1.zip"
print(my_zip)

#This code was used to extract data from zip files
def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

for filename in os.listdir(os.getcwd()):
    try:
        if filename.endswith('.zip'):
            print(filename)
            zip_file = zipfile.ZipFile(filename, 'r')
            file1=os.path.splitext(filename)[0]
            outpath=os.getcwd()+"\\"+file1
            print(outpath)
            os.mkdir(outpath);
            outpath+="\\";
            print(outpath)
            zip_file.extractall(outpath)
    except Exception as e:
        print(e) 
        print("ex")
        pass       
        
