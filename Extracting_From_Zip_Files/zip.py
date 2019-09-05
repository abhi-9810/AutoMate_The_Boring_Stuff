import os
import zipfile
for filename in os.listdir(os.getcwd()):
    try:
        
        if filename.endswith('.zip'):
            z = zipfile.ZipFile(filename)
            for name in z.namelist():
                extension = os.path.splitext(name)[1][1:]
                outpath =os.getcwd()
                outpath+="\\temp_"+str(extension)
                if not os.path.exists(outpath):
                    os.makedirs(outpath)
                z.extract(name, outpath)
                print(outpath)
            print(filename)
        #filename.close()
    except:
         pass
