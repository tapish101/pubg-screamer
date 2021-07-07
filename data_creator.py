#this script creates the data of kills and save it to later compare with to find the kills

import pyscreenshot
import os
#to install PIL run "pip install pillow" in the terminal
from PIL import ImageEnhance

#creating the folders to save data
try:
    os.mkdir("data/img")
    os.mkdir("data/files")
except FileExistsError:
    print("\nfolders already exist")

#change these values with those you got from coordinate_finder.py script also change in the_screamer.py
x1=101
y1=110

x2=126
y2=134

#the factor holdes the val by which factor you want to contrast the image
#and the thresh hold the threshold to Black & White the image if you change them here remember to change them also in the_screamer.py script
factor=2
thresh = 70

x=0  #don't change it

while(True):
    try:
        n= int(input("\nenter 1 for next kill entry and 2 to exit: "))
    except ValueError:
        n=0


    if n==1:
        #take the screenshot and crop it to size of given coordinates
        image_real = pyscreenshot.grab()
        img = image_real.crop((x1,y1,x2,y2)) 
        
        #converting image to negative
        for i in range(0, img.size[0]-1):

            for j in range(0, img.size[1]-1):

                pixelColorVals = img.getpixel((i,j));
                redPixel    = 255 - pixelColorVals[0];

                greenPixel  = 255 - pixelColorVals[1];

                bluePixel   = 255 - pixelColorVals[2];

                img.putpixel((i,j),(redPixel, greenPixel, bluePixel));
        
        #making it a bit more contrasy
        img_contr_obj=ImageEnhance.Contrast(img)
        e_img=img_contr_obj.enhance(factor)
        
        #making it one bit B&W and then saving it
        fn = lambda x : 255 if x > thresh else 0
        r = e_img.convert('L').point(fn, mode='1')
        r.save("data/img/"+ str(x)+".jpeg")
        print("saved "+str(x)+" kill")
        x=x+1

    elif n==2:
        break

    else:
        print("\nthe input should be either 1 or 2")

