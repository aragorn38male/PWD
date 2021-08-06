from m5stack import *
from m5ui import *
from uiflow import *
from time import sleep
import random

from machine import I2C
from machine import Pin

i2c = I2C(1, Pin(26), Pin(0))

pos=0
able=False

lst=[("aliexpress" , "$\.>DADush9#(hr"),
     ("amazon"     , "7W'5{j[R>,Mq`t_"),
     ("apple"      , "suG<\2N{%jhU)Vm"),
     ("decathlon"  , "!w9s-+[hw-(d7N}"),
     ("dropbox"    , "yx26-5Q8C*!MvFu"),
     ("facebook"   , "s)9?v-`wh{P,P}D"),
     ("firefox"    , "=e3\::,Y$WF/H[}"),
     ("google"     , "5zuNt6hT$C&'&s~"),
     ("instagram"  , "@.%JT[S(Bfab<72"),
     ("leboncoin"  , "mz+k]p2y^J5$6{b"),
     ("messenger"  , "SY+/>b?3':7BL-q"),
     ("paypal"     , "VkNgeR9,RNX(R;,"),
     ("snapchat"   , "Q(?3Wu9H-W+ts%3"),
     ("steam"      , "T~m]3^+QPa3%4>h"),
     ("twitter"    , "msN~~\Et`6KwkCu"),
     ("windows"    , ";Uw3(=]_vf482eU")]

tmp=[]
for i in range(len(lst)):
    x=random.choice(lst)
    lst.remove(x)
    tmp.append(x)
lst=tmp

setScreenColor(0x000000)

img = M5Img(0, 160, "res/unknown.jpg", True)
path="res/"+lst[0][0]+".jpg"
img.changeImg(path)

label0 = M5TextBox(75, 90, "", lcd.FONT_Default, 0xFFFFFF, rotate=90)

label1 = M5TextBox(60, 90, "", lcd.FONT_DejaVu18, 0xFFFFFF, rotate=90)
label2 = M5TextBox(40, 90, "", lcd.FONT_DejaVu18, 0xFFFFFF, rotate=90)
label3 = M5TextBox(20, 90, "", lcd.FONT_DejaVu18, 0xFFFFFF, rotate=90)

def scrollML(image):
    for i in range(120):
        image.setPosition(y=160-i)
    #sleep(1)
    
def scrollMR(image):
    for i in range(40):
        image.setPosition(y=40-i)
    #sleep(1)
        

#scrollML(img)


def buttonA_wasPressed():
  global lst,pos,able
  able=True
  pos+=1
  path="res/"+lst[pos%len(lst)][0]+".jpg"
  img.changeImg(path)
  label0.hide()
  label1.hide()
  label2.hide()
  label3.hide()
  scrollML(img)
  #i2c.writeto(0x50, 'S5XK(guU,,^@TxG*')
  pass
btnA.wasPressed(buttonA_wasPressed)

def buttonB_wasPressed():
  global lst,pos,able
  if able:
    able=False
    scrollMR(img)
    label0.setText(lst[pos%len(lst)][0])
    label1.setText(lst[pos%len(lst)][1][0:5])
    label2.setText(lst[pos%len(lst)][1][5:10])
    label3.setText(lst[pos%len(lst)][1][10:15])
    #label0.show()
    i2c.writeto(0x50, lst[pos%len(lst)][1])
  pass
btnB.wasPressed(buttonB_wasPressed)
