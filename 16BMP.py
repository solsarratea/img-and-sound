from PIL import Image

iname = 'index.bmp'
oname = 'indexe.bmp'

img = Image.open(iname)
newimg = img.convert(mode='P', colors=16)
newimg.save(oname)
