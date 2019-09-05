import os
from PIL import Image
import rawpy
import imageio
i=0
for filename in os.listdir(os.getcwd()):
    if not filename.endswith('.py'):
        raw = rawpy.imread(filename)
        rgb = raw.postprocess()
        temp="../temp1/intellify_"+str(i)+".jpg"
        i=i+1
        imageio.imsave(temp, rgb)
        
    
