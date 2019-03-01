from PIL import Image
import os

path2='D:\Rcnn\Listed_cats'
path1='D:\Rcnn\Cats'

listing=os.listdir(path1)
for file in listing:
    im = Image.open(path1 + '\\' + file)            
    im.save(path2 +'\\' + 'Cat '+ file, "JPEG")
