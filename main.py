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


#Sharp FUNCTIONS (Try playsound) (Check importing from online source)
def value_Cs():
    str1.set("C#")
    sound = pygame.mixer.Sound ("C:\\Users\\Student\\Desktop\\Comp Project V\\Piano notes\\C_s.wav") #Check Pathways
    sound.play()
        
def value_Ds():
    str1.set("D#")
    sound = pygame.mixer.Sound ("C:\\Users\\Student\\Desktop\\Comp Project V\\Piano notes\\D_s.wav") #Check Pathways
    sound.play()
def value_Fs():
    str1.set("F#")
    sound = pygame.mixer.Sound ("C:\\Users\\Student\\Desktop\\Comp Project V\\Piano notes\\F_s.wav") #Check Pathways
    sound.play()    
def value_Gs():
    str1.set("G#")
    sound = pygame.mixer.Sound ("C:\\Users\\Student\\Desktop\\Comp Project V\\Piano notes\\G_s.wav") #Check Pathways
    sound.play()
def value_Bb():
    str1.set("Bb")
    sound = pygame.mixer.Sound ("C:\\Users\\Student\\Desktop\\Comp Project V\\Piano notes\\Bb.wav") #Check Pathways
    sound.play()    
def value_Cs1():
    str1.set("Cs1")
    sound = pygame.mixer.Sound ("C:\\Users\\Student\\Desktop\\Comp Project V\\Piano notes\\C_s1.wav") #Check Pathways
    sound.play()    
def value_Ds1():
    str1.set("Ds1")
    sound = pygame.mixer.Sound ("C:\\Users\\Student\\Desktop\\Comp Project V\\Piano notes\\D_s1.wav") #Check Pathways
    sound.play()
    
