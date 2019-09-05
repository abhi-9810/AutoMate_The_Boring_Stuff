import os
import shutil
import zipfile

my_dir = os.getcwd()
my_zip = os.getcwd()+"\\isafe_1_online_1_1.zip"
print(my_zip)

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

for filename in os.listdir(os.getcwd()):
    try:
        if filename.endswith('.zip'):
            n1=find_nth(filename, "_", 2)
            n2=find_nth(filename, "_", 3)
            temp=filename[n1+1:n2]
            print(filename)
            print(temp)
            zip_file = zipfile.ZipFile(filename, 'r')
            for files in zip_file.namelist():
                name=files
                extension = os.path.splitext(name)[1][1:]
                outpath =os.getcwd()
                data = zip_file.read(files)
                outpath+="\\"+str(temp)+"_"+str(extension)
                print(outpath)
                print("\n\n\n\n\n\nqwerty")
                if not os.path.exists(outpath):
                    os.makedirs(outpath)
                print(files.split("/"))
                print(files)
                myfile_path = os.path.join(outpath, files.split("/")[-1])
                print(myfile_path)
		
                myfile = open(myfile_path, "wb")
                myfile.write(data)
                myfile.close()
    except Exception as e:
        print(e)
        
