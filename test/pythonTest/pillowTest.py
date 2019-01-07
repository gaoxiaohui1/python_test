from PIL import Image
im=Image.open('test.jpg')
print(im.format,im.size,im.mode)
im.thumbnail((1000,600))
im.save('thumb.jpg','JPEG')