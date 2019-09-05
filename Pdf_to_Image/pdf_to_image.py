import PyPDF2

from PIL import Image

import sys
from os import path
import warnings
warnings.filterwarnings("ignore")

#this code was used to extract images from a given pdf.
#PyPDF library was used
number = 0

def recurse(page, xObject):
    global number

    xObject = xObject['/Resources']['/XObject'].getObject()

    for obj in xObject:
       try: 
        if xObject[obj]['/Subtype'] == '/Image':
            size = (xObject[obj]['/Width'], xObject[obj]['/Height'])
            data = xObject[obj]._data
            if xObject[obj]['/ColorSpace'] == '/DeviceRGB':
                mode = "RGB"
            else:
                mode = "P"

            imagename = "%s - p. %s - %s"%(abspath[:-4], p, obj[1:])

            if xObject[obj]['/Filter'] == '/FlateDecode':
                img = Image.frombytes(mode, size, data)
                img.save(imagename + ".png")
                number += 1
            elif xObject[obj]['/Filter'] == '/DCTDecode':
                img = open(imagename + ".jpg", "wb")
                img.write(data)
                img.close()
                number += 1
            elif xObject[obj]['/Filter'] == '/JPXDecode':
                img = open(imagename + ".jp2", "wb")
                img.write(data)
                img.close()
                number += 1
        else:
            recurse(page, xObject[obj])
       except:
           pass


try:
    _, filename = sys.argv
    abspath = path.abspath(filename)
except BaseException:
    print('Usage :\nPDF_extract_images file.pdf page1 page2 page3 …')
    sys.exit()


file = PyPDF2.PdfFileReader(open(filename, "rb"))
pages=file.getNumPages()
for p in range(0,int(pages)):
    page0 = file.getPage(p)
    recurse(p, page0)

print('%s extracted images'% number)
