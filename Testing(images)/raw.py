import rawpy
import imageio

raw = rawpy.imread('IMG_0988.CR2')
rgb = raw.postprocess()
imageio.imsave('img11.jpg', rgb)
