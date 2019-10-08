#!/usr/bin/env python
from numpy import *
from PIL import ImageOps
import time
import pyscreenshot as ImageGrab
import pyautogui as py


class Coordinate():
    dino = (218,438)
    #y = 470 x= 230

def press():

    py.keyDown('space')
    time.sleep(0.1)
    py.keyUp('space')


def IMG():
    Box=(Coordinate.dino[0]+70 ,Coordinate.dino[1],Coordinate.dino[0]+70+150,Coordinate.dino [1]+30)
    image= ImageGrab.grab(Box)
    image= ImageOps.grayscale(image)
    arr= array(image.getcolors())
    return(arr.sum())

def main():
    print("starting game....")
    x=0
    while(1):
        print(IMG())
        if(IMG()!= 4747):
            time.sleep(0.1)
            press()
            x=x+1
            print('jump number ',x)


main()
