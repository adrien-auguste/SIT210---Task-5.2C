from tkinter import*
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

## LED assignments
red = LED(10)
green = LED(9)
yellow = LED(11)
## Defining the GUI

win = Tk()
win.title("Task 5.2 - Making GUI")
win.geometry('500x300')
myFont = tkinter.font.Font(family ='Arial' ,size = '13', weight = "bold")

## Functions

def redToggle():
    yellow.off()
    green.off()
    red.on()

def yellowToggle():
    yellow.on()
    green.off()
    red.off()

def greenToggle():
    yellow.off()
    green.on()
    red.off()

def closeProgram():
	RPi.GPIO.cleanup()
	win.destroy()

## Building widgets

redButton = Button(win, text= "Turn on red LED", command = redToggle, bg ='grey',height = 1, width = 20)
redButton.grid(row = 1, column = 1)

yellowButton = Button(win, text= "Turn on yellow LED", command = yellowToggle, bg ='grey',height = 1, width = 20)
yellowButton.grid(row = 3, column = 1)

greenButton = Button(win, text= "Turn on greeb LED", command = greenToggle, bg ='grey',height = 1, width = 20)
greenButton.grid(row = 5, column = 1)

exitProgram = Button(win, text= "Close program", command = closeProgram, bg ='red',height = 1, width = 20)
exitProgram.grid(row = 7, column = 1)

win.protocol("WM_DELETE_WINDOW", closeProgram)

win.mainloop()
