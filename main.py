import pyautogui
import time 
from PIL import Image
from os import listdir
from os.path import isfile, join
mypath = "animation"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]  
time.sleep(2)

pyautogui.PAUSE = 0

blackcount = 0

def setpixel(x,y):
    pyautogui.moveTo(6+x,146+y)
    pyautogui.click()

def drawline(x,y,x2,y2):
    pyautogui.moveTo(6+x,146+y)
    pyautogui.dragTo(6+x2,146+y2, duration=0.1)
    # pyautogui.mouseDown()
    # pyautogui.moveTo(6+x2,146+y2)
    # pyautogui.mouseUp()
    # time.sleep(0.01)

pointer = 0

for l in onlyfiles:
    print(l)
    im = Image.open("animation/"+l, "r")
    im = im.resize((400,300), Image.ANTIALIAS)
    im.save("animation/"+l)
    px = im.load()
    width, height = im.size
    print(width, height)
    
    for i in range(0,height,4):
        
        for j in range(0,width,1):
            if px[j,i][0] == 0 and pointer == 0:
                pointer = (j,i)
            if pointer != 0 and px[j,i][0] == 255 and pointer[1] == i:
                drawline(pointer[0],pointer[1],j,i)
                pointer = 0
            if pointer != 0 and pointer[1] != i:
                pointer = 0

    time.sleep(0.1)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.moveTo(245,70)
    pyautogui.click()
    

