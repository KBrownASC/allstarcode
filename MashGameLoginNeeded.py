from random import *
from Myro import *
from sys import *

login=0
atmp=0
x=2    


#Login and Password

while login<1:
    userName=raw_input("Username:")
    if userName=="Goldman":
        print("Now type in your password")
        passwd=raw_input("Password:")
        if passwd=="daregreatly":
            print("You are logged in")
            login=login+1
        else:
            print("wrong password")
            atmp=atmp + 1
            print("you have",x,"attempts left")
            x=x-1
            if atmp==3:
                print("No more attempts")
                exit()
    else:
        print("try again")
        atmp=atmp + 1
        print("you have",x,"attempts left")
        x=x-1
        if atmp==3:
            print("No more attempts")
            exit()
            
#Actual MASH Game
            
wait(3)           
print("WELCOME TO THE MASH GAME!")         
            
newPet = raw_input("What will be your pet")
print(newPet, "is what you want")
newJob = raw_input("What will be your job")
print(newJob, "is what you want")
newWife= raw_input("Who will be your wife")
print(newWife, "is who you want")


#input print
yes = [ "yes","yeah","sure"]


#List
pets = ["Dung Beetle  ", "A rock  ", "Bird  ", newPet  ]
jobs = ["Unemployed  ", "Interlude  ","GoofyGoober Enterprises  ", newJob]
wives = ["Camilla Cabello  ", "Girl next door  ", "You didn't get a wife!  ", newWife]
houses = ["Mansion  ","Apartment  ","Shack  ","House  "]

#code
print("RESULTS")
wait(1)
print("Disclaimer")
print("These are very reliable results with 99% accuracy")

cont = raw_input("Are you sure you wanna know... Yes or No")
if cont == "Yes":
    wait(1)
    wait(1)
    print("you'll have a...",choice(pets))
    wait(1)
    print("you'll work at...",choice(jobs))
    wait(1)
    print("you'll marry...",choice(wives))
    wait(1)
    print("you'll live in a...",choice(houses))
    wait(2)
    print("satisfied")
elif cont == "No":
    wait(1)
    print("okay, you are gonna know anyway")
    wait(1)
    print("you'll have a...",choice(pets))
    wait(1)
    print("you'll work at...",choice(jobs))
    wait(1)
    print("you'll marry...",choice(wives))
    wait(1)
    print("you'll live in a...",choice(houses))
    wait(1)
    print("Happy?")