from random import *
from Myro import *


#code input
newPet = raw_input("What will be your pet")
print(newPet, "good luck")
newJob = raw_input("What will be your job")
print(newJob, "good luck")
newWife= raw_input("Who will be your wife")
print(newWife, "good luck")


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