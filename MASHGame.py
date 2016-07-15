from random import *
from Myro import *
from Graphics import *
#code input
newPet = raw_input("What will be your pet")
print(newPet, "good luck")
newJob = raw_input("What will be your job")
print(newJob, "good luck")
newWife= raw_input("Who will be your wife")
print(newWife, "good luck")


#input print



#List
pets = ["Dung Beetle", "A rock", "Bird", newPet]
jobs = ["Unemployed", "Interlude","GoofyGoober Enterprises", newJob]
wives = ["Camilla Cabello", "Rhiana", "You didn't get a wife!", newWife]
houses = ["Mansion","Apartment","Shack","House"]

#code
print("RESULTS")
wait(2)
print(choice(pets),choice(jobs),choice(wives),choice(houses))



