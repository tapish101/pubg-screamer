import pyscreenshot
from PIL import ImageEnhance, ImageChops, Image
import math, operator
from functools import reduce
from playsound import playsound

#global variables
x1=101
y1=110
x2=126
y2=134

maxkills=12   #the higest kills images you have in data folder

rmsdiff=[None]*(maxkills+1)    #the list that holds the rms diff of current img and the whole images in data

lastkill=-1    #don't change it
end = False

#function to return rms diff b/w two images
def diff(im1, im2):

    h = ImageChops.difference(im1, im2).histogram()

    #calculating the rms of diff and returning it
    return math.sqrt(reduce(operator.add,
        map(lambda h, i: h*(i**2), h, range(256))
    ) / (float(im1.size[0]) * im1.size[1]))


#modify(im) convert the image a little contraty, negative and then make it 1 bit b&w
def modify(im):
    for i in range(0, im.size[0]-1):

            for j in range(0, im.size[1]-1):

                pixelColorVals = im.getpixel((i,j));
                redPixel    = 255 - pixelColorVals[0];

                greenPixel  = 255 - pixelColorVals[1];

                bluePixel   = 255 - pixelColorVals[2];

                im.putpixel((i,j),(redPixel, greenPixel, bluePixel));

    img_contr_obj=ImageEnhance.Contrast(im)
    factor=2
    e_img=img_contr_obj.enhance(factor)
    thresh = 70
    fn = lambda x : 255 if x > thresh else 0
    new_im = e_img.convert('L').point(fn, mode='1')
    return new_im


#this functions does everything when a kill is registered
def dosomething(kill):
    print("Kills are "+str(kill))
    playsound("data/files/"+str(kill)+".mp3")  #save the sound(mp3 files) with corresponding kill name
    global lastkill,end
    lastkill=kill
    if(kill==maxkills): end=True


#the main loop
while(True):
    if(end==True):
        print("\nProgramm terminates here.")
        break

    img = pyscreenshot.grab()
    img=img.crop((x1,y1,x2,y2))

    img=modify(img)

    #loop to fill rmsdiff list with the val
    for k in range(maxkills+1):
        imgx =Image.open("data/img/"+str(k)+".jpeg")
        rmsdiff[k]= diff(imgx,img)

    kills = operator.indexOf(rmsdiff,min(rmsdiff))  #the returns the index of the min value in rmsdiff list and the index is same as the kill
    if kills!=lastkill:
        dosomething(kills)

    