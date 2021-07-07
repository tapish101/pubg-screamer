import pyscreenshot
import os
from PIL import ImageEnhance

try:
    os.mkdir("data/img")
    os.mkdir("data/files")
except FileExistsError:
    print("\nfolders already exist")


x1=101
y1=110

x2=126
y2=134

x=0

while(True):
    try:
        n= int(input("\nenter 1 for next kill entry and 2 to exit: "))
    except ValueError:
        n=0


    if n==1:
        image_real = pyscreenshot.grab()
        img = image_real.crop((x1,y1,x2,y2)) 
        

        for i in range(0, img.size[0]-1):

            for j in range(0, img.size[1]-1):

                pixelColorVals = img.getpixel((i,j));
                redPixel    = 255 - pixelColorVals[0];

                greenPixel  = 255 - pixelColorVals[1];

                bluePixel   = 255 - pixelColorVals[2];

                img.putpixel((i,j),(redPixel, greenPixel, bluePixel));

        img_contr_obj=ImageEnhance.Contrast(img)
        factor=2
        e_img=img_contr_obj.enhance(factor)
        thresh = 70
        fn = lambda x : 255 if x > thresh else 0
        r = e_img.convert('L').point(fn, mode='1')
        r.save("data/img/"+ str(x)+".jpeg")
        print("saved "+str(x)+" kill")
        x=x+1

    elif n==2:
        break

    else:
        print("\nthe input should be either 1 or 2")

