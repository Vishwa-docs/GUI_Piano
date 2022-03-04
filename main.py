'''
#MYSPACE
Change Font and Background Colour
Check online Notes Importing
see if you can make it a key input (if event.type == pygame.KEYDOWN and event.key == pygame.K_a:)
'''


#NOTES FILE : https://drive.google.com/file/d/0B5VO9Z-lZzRYSncwNGhmWmhHenc/view

#CODE
from tkinter import*
import time
import datetime
import pygame
#from playsound import playsound as p : https://realpython.com/playing-and-recording-sound-python/

pygame.init()
root =Tk()
root.title("Music Box")
root.geometry('1352x700+0+0')
root.configure(background ='white')

ABC=Frame(root, bg="powder blue", bd=20, relief= RIDGE)
ABC.grid()

ABC1=Frame(ABC, bg="powder blue", bd=20, relief= RIDGE)
ABC1.grid()
ABC2=Frame(ABC, bg="powder blue", relief= RIDGE)
ABC2.grid()
ABC3=Frame(ABC, bg="powder blue", relief= RIDGE)
ABC3.grid()


str1 = StringVar()
str1.set("Last key : ")
Date1=StringVar()
Time1=StringVar()

Date1.set(time.strftime("%d/%m/%Y"))
Time1.set(time.strftime("%H:%M:%S"))

