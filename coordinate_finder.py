#run this script to find the coordinates of screenshots

import pyscreenshot

#(x1,y1) are the top left coordinate of the screenshot taken
x1=101
y1=110

#(x2,y2) are the bottom right coordinates
x2=126
y2=134

img = pyscreenshot.grab()
img = img.crop((x1,y1,x2,y2)) 

img.show()
