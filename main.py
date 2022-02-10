import Events
from os import system, name
from time import sleep
def clear():
    if name == 'nt':
        _ = system("cls")
    else:
        _ = system("clear")
import time
Red = "\033[0;31m"
Green = "\033[0;32m"
Blue = "\033[0;34m"
Reset = "\033[0;37m"
print("Anouncer: Welcome to the first tourist flight to the moon!\n")
time.sleep(3)
print("Anouncer: Many of you have been in space and left our buetifull blue rock before, but we are going where no tourist has gone before, another planet!\n")
time.sleep(2)
print(Green+"You hear a small child ask their parents if the moon is acually a planet\n")
time.sleep(1)
print(Reset+"Epic music starts playing\n")
time.sleep(4)
print(Blue+"Robotic voice: You have arrived"+Reset)
time.sleep(4)
clear()
time.sleep(1)
print("In front of you are two ways you could go, the employies only area and the cafeteria\n")
time.sleep(1)
choice1 = input("1. Go to the "+Red+"Employies Only Area"+Reset+"\n2. Go to "+Blue+"Cafeteria"+Reset+"\nChoice: ")
HasCard = Events.choice1(choice1)