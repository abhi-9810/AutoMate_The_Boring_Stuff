import os
import zipfile
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
            z = zipfile.ZipFile(filename)
            for name in z.namelist():
                extension = os.path.splitext(name)[1][1:]
                outpath =os.getcwd()
                outpath+="\\temp_"+str(temp)+"_"+str(extension)
                if not os.path.exists(outpath):
                    os.makedirs(outpath)
                z.extract(name, outpath)
                print(outpath)
            print(filename)
        #filename.close()
    except:
         pass
