import os
from PIL import Image
#resize images in a given directory
for filename in os.listdir(os.getcwd()):
    if not filename.endswith('.py'):
        foo = Image.open(filename)
        foo = foo.resize((300,200),Image.ANTIALIAS)
        temp="../temp/"+filename;
        foo.save(temp,optimize=True,quality=95)
    
