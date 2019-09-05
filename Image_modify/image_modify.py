from PIL import Image

im = Image.open('i1.jpg')
im1 = Image.open('i2.jpg')
pix = im.load()
pix1=im1.load()
print(im.size)
print(im1.size)
count=0
for i in range(0,im.size[0]):
    for j in range(0,im.size[1]):
        if(pix1[i,j]!=pix[i,j]):
            count+=1
            print(str(pix[i,j])+"   "+str(pix1[i,j])+"   "+str(i)+","+str(j))

print(count)
