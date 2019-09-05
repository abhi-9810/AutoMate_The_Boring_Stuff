import os
from PIL import Image
i=0
for filename in os.listdir(os.getcwd()):
    try:

        if not filename.endswith('.py'):
            foo = Image.open(filename)
        #foo = foo.resize((300,200),Image.ANTIALIAS)
            temp="temp/"+str(i)+".jpg";
            foo.save(temp,optimize=False,quality=100)
            i=i+1
    except:
        pass
        
