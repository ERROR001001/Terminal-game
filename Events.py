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
#choice1 = employee lounge or cafeteria
def choice1(choice):
  if choice == "1":
    #check if you have the keycard
    choice = choice
  elif choice == "2":
    cafeteria()
    choice = choice
  else:
    #Not a valid option
    choice = choice
def cafeteria():
  print("\nYou and the rest of the group go in to the cafeteria and sit down\n")
  smalltalk = input("1. Make small talk\n2. Stay quite\nChoice: ")
  if smalltalk == "1":
    print("\nYou make small talk with someone sitting across from you, he is rather strong and you talk about working out, video games, and how you got the money to afford this trip.\n")
    time.sleep(5)
    print("After a minute of talking an old projecter turns on and starts playing an introduction video\n")
    time.sleep(3)
    print(Red+"You don't pay attention\n"+Reset)
    time.sleep(4)
    print("After the video you are told to exit the cafeteria, you walk towards the exit and step on something, you look down and see a card. You pick up the card.\n")
    loop1 = False
    while loop1:
      HasCard = input("1. Take the card\n2. Return the card to staff\nChoice: ")
      if HasCard == "1":
        time.sleep(1)
        print("You pick up the card and continue leaving  the cafeteria")
        loop1 = True
      elif HasCard == "2":
       print("You pick up the card and give it to a staff member")
       time.sleep(1)
       print("Staff Member: Thanks!")
       loop1 = True
      else:
        print("Thats not an option")
        clear()
  elif smalltalk == "2":
    print("After a minute an old projecter turns on and starts playing an introduction video\n")
    time.sleep(3)
    print(Red+"\nYou don't pay attention"+Reset)
    time.sleep(4)
    print("After the video you are told to exit the cafeteria, you walk towards the exit and step on something, you look down and see a card. You pick up the card.\n")
    loop1 = False
    while loop1:
      HasCard = input("1. Take the card\n2. Return the card to staff\nChoice: ")
      if HasCard == "1":
        time.sleep(1)
        print("You pick up the card and continue leaving  the cafeteria")
        loop1 = True
      elif HasCard == "2":
       print("You pick up the card and give it to a staff member")
       time.sleep(1)
       print("Staff Member: Thanks!")
       loop1 = True
      else:
        print("Thats not an option")
        clear()
  return HasCard