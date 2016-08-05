from random import*
from time import*

#Randomize Options

Choice_1_Value = [0,1,2]
argueChoice = [0,1]
fightChoice = [0,1]
wallChoice = [0,1]
leftChoice = [0,1]
rightChoice = [0,1]


#ChooseYourAdventure Story 

Character_name = raw_input("What's your name?") 
alert("Was",Character_name,"your name?")
confirmName = raw_input("yes or no")
if confirmName == "no":
	Character_name = raw_input("What's your name?") 
	alert("Was",Character_name,"your name?")
	confirmName = "yes"
elif confirmName == "yes":
	alert(Character_name,"have fun")
	
sleep(1)
alert("note- Type all answers in caps from now on")
sleep(2)

alert("The palace")

sleep(1)

alert("You wake up in a cold and stuffy room, with cob webs draped around the room, there are two doors, one on your LEFT annd one on your RIGHT, you hear someone coming from the RIGHT.")
sleep(1)

alert("What do you do? STAY, go LEFT, or go RIGHT")
Choice_1 = raw_input("STAY,LEFT,RIGHT")






#STAYYYYYYYYYYYYYYYYYYYYY
if Choice_1 == "STAY":
	alert("You decided to STAY")
	sleep(.5)
	Choice_1_Value = choice(Choice_1_Value)
	if Choice_1_Value == 0:
		alert("""A young woman with a boorish appearnece walks into the room and at the sight of you begins to scowl, she rudely asks you to follow her to the room on the right""")
		Choice_2 = raw_input("FOLLOW, ARGUE")
		if Choice_2 == "FOLLOW":
			alert("You decided to FOLLOW her, and she leads you into the RIGHT door way where you go into an open field with all sorts of animals and people enjoying the aromic garden that seemed to span the horizon.")
		if Choice_2 == "ARGUE":
			argueChoice = choice(argueChoice)
			if argueChoice == 0:
				alert("she cut your throat, for arguing with her")
			if argueChoice == 1:
				alert("she was angered by you, but decided to make nothing of it and instead grabs you with her inhuman strength and drags you behind her")
				sleep(1)
				alert("she brings you to the entrance you are free to go")
				alert("YOU WON!!!!")
	
	
	
	#OUTCOME 2 FOR CHOICE 1
	if Choice_1_Value == 1:
		alert(" A young boy with tears in his eyes walks into the room with a brown rabbit in his arms, the rabbit seems lifeless, you are suddenly hungry")
		sleep(.5)
		alert("What do you do, HELP, EAT")
		Choice_2 = raw_input("HELP, EAT")
		if Choice_2 =="HELP":
			alert("You decided to HELP the boy and proceeds to shake the rabbit to life, the boy is overjoyed! He asks you your name?")
			tellName = raw_input("TELL, NOTHING")
			if tellName == "TELL":
				alert("you replied with",Character_name)
				alert("The boy writes your name down in a book he takes out of his pocket")
				sleep(.5)
				alert("You died")
		if Choice_2 == "EAT":
			alert("you ripped the bunny away from the boy, and proceed in devouring the animal, your stomach doesn't seem to enjoy the rabbit")
			sleep(.5)
			alert(" eating a raw rabbit killed you")
	
	
	
	#outcome 3 FOR CHOICE 1
	
	if Choice_1_Value == 2:
		alert("The door opens and a husky puma, pounces into the room, he stares at you what do you do?")
		Choice_2 = raw_input("FIGHT, RUN")
		if Choice_2 == "FIGHT":
			fightChoice = choice(fightChoice)
			if fightChoice == 0:
				alert("You decided to FIGHT the puma")
				sleep(.5)
				alert("The puma killed you")
				sleep(.5)
				alert("The end")
			if fightChoice == 1:
				alert("You decided to FIGHT a puma bare handed")
				sleep(.5)
				alert("well you must be tarzan or something because you somehow won the fight")
				sleep(.5)
				alert("the adrenaline from fighting a puma and winning kills you")
		if Choice_2 == "RUN":
			alert("You decided to RUN")
			sleep(.5)
			alert("You looked around the room and decided to make a run towards the left door, you narrowly escape the puma as you close the door behind you. There is a long corridor to explore with many familiar paintings on the walls")
			alert("one of the paintings come out of the picture and proceeds to eat your soul")
			alert("you died")
	
	
	


#GO LEFFFFFTTTTTTTTTTTTTTTTTTTT
if Choice_1 == "LEFT":
	leftChoice = choice(leftChoice)
	if leftChoice == 0:
		alert("You WANTED to go LEFT, but you really wanted to STAY")
		sleep(.5)
		alert("You decided to STAY")
		sleep(.5)
		Choice_1_Value = choice(Choice_1_Value)
		if Choice_1_Value == 0:
			alert("""A young woman with a boorish appearnece walks into the room and at the sight of you begins to scowl, she rudely asks you to follow her to the room on the right""")
			Choice_2 = raw_input("FOLLOW, ARGUE")
			if Choice_2 == "FOLLOW":
				alert("You decided to FOLLOW her, and she leads you into the RIGHT door way where you go into an open field with all sorts of animals and people enjoying the aromic garden that seemed to span the horizon.")
			if Choice_2 == "ARGUE":
				argueChoice = choice(argueChoice)
				if argueChoice == 0:
					alert("she cut your throat, for arguing with her")
				if argueChoice == 1:
					alert("she was angered by you, but decided to make nothing of it and instead grabs you with her inhuman strength and drags you behind her")
					alert("She took you to a bad place undergroud")
					sleep(1)
					alert("you work there for the rest of your life and die")
	if leftChoice == 1:
		sleep(.5)
		alert("You escape to the LEFT into a corridor with alot of familiar paintings" + " you reach out to the paintings as you traverse through the hallway")
		sleep(.5)
		alert("you ponder is you should keep your hand on the wall or not")
		Choice_3 = raw_input("KEEP, OFF")
		wallChoice = choice(wallChoice)
		if wallChoice == 0:
			alert("seem to have no wall behind it")
			sleep(.5)
			goWall = raw_input("LOOK, STAY")
			if goWall == "LOOK":
				alert("You went into the painting and fell out of the building, you are fre but you are injured")
				alert("you won")
			if goWall == "STAY":
				alert("You continue down the passage only to find nothing but a gem")
				takeGem = raw_input("TAKE, LEAVE")
				if takeGem == "TAKE":
					alert("You took the gem, but a trap has been activated")
					sleep(.5)
					alert("you can't escape")
					alert("you die with the gem") 
				if takeGem == "LEAVE":
					alert("you left the gem alone, and returned to the first room, but something is different now. The cob webs are gone and the room seems more spacious. A young woman walks in with a huge smile on her face and tells you that she is here to murder you")
					sleep(1)
					argueChoice = choice(argueChoice)
					if argueChoice == 0:
						alert("you let her know that you are confused and she instead frees you")
						alert("YOU WIN!!!")
					if argueChoice ==1:
						alert("cat caught our toungue, you can't explain yourslef and now you are dead")
		if wallChoice ==1:
			alert("You continue down the passage only to find nothing but a gem")
			takeGem = raw_input("TAKE, LEAVE")
			if takeGem == "TAKE":
				alert("You took the gem, but a trap has been activated")
				sleep(.5)
				alert("you can't escape")
				alert("you die with the gem") 
			if takeGem == "LEAVE":
				alert("you left the gem alone, and returned to the first room, but something is different now. The cob webs are gone and the room seems more spacious. A young woman walks in with a huge smile on her face and tells you that she is here to murder you")
				sleep(1)
				argueChoice = choice(argueChoice)
				if argueChoice == 0:
					alert("you let her know that you are confused and she instead frees you")
				if argueChoice ==1:
					alert("cat caught our toungue, you can't explain yourslef and now you are dead")

	
	#OUTCOME 2 FOR CHOICE 1
	if Choice_1_Value == 1:
		alert(" A young boy with tears in his eyes walks into the room with a brown rabbit in his arms, the rabbit seems lifeless, you are suddenly hungry")
		sleep(.5)
		alert("What do you do, HELP, EAT")
		Choice_2 = raw_input("HELP, EAT")
		if Choice_2 =="HELP":
			alert("You decided to HELP the boy and proceeds to shake the rabbit to life, the boy is overjoyed! He asks you your name?")
			tellName = raw_input("TELL, NOTHING")
			if tellName == "TELL":
				alert("you replied with",Character_name)
				alert("The boy writes your name down in a book he takes out of his pocket")
				sleep(.5)
				alert("You died")
		if Choice_2 == "EAT":
			alert("you ripped the bunny away from the boy, and proceed in devouring the animal, your stomach doesn't seem to enjoy the rabbit")
			sleep(.5)
			alert(" eating a raw rabbit killed you")
	
	
	
	#outcome 3 FOR CHOICE 1
	
	if Choice_1_Value == 2:
		alert("The door opens and a husky puma, pounces into the room, he stares at you what do you do?")
		Choice_2 = raw_input("FIGHT, RUN")
		if Choice_2 == "FIGHT":
			fightChoice = choice(fightChoice)
			if fightChoice == 0:
				alert("You decided to FIGHT the puma")
				sleep(.5)
				alert("The puma killed you")
				sleep(.5)
				alert("The end")
			if fightChoice == 1:
				alert("You decided to FIGHT a puma bare handed")
				sleep(.5)
				alert("well you must be tarzan or something because you somehow won the fight")
				sleep(.5)
				alert("the adrenaline from fighting a puma and winning kills you")
		if Choice_2 == "RUN":
			alert("You decided to RUN")
			sleep(.5)
			alert("You looked around the room and decided to make a run towards the left door, you narrowly escape the puma as you close the door behind you. There is a long corridor to explore with many familiar paintings on the walls")
			alert("Timmy Turner wished for a Burner and killed you")
			alert("You died")
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
#GO RIGHTTTTTTTTTTTTTTTTTTTTTTTTTTTTT	
	
if Choice_1 == "RIGHT":
	alert("You WANTED to go RIGHT, but you really wanted to STAY")
	sleep(.5)
	alert("You decided to STAY")
	sleep(.5)
	Choice_1_Value = choice(Choice_1_Value)
	if Choice_1_Value == 0:
		alert("""A young woman with a boorish appearnece walks into the room and at the sight of you begins to scowl, she rudely asks you to follow her to the room on the right""")
		Choice_2 = raw_input("FOLLOW, ARGUE")
		if Choice_2 == "FOLLOW":
			alert("You decided to FOLLOW her, and she leads you into the RIGHT door way where you go into an open field with all sorts of animals and people enjoying the aromic garden that seemed to span the horizon.")
		if Choice_2 == "ARGUE":
			argueChoice = choice(argueChoice)
			if argueChoice == 0:
				alert("she cut your throat, for arguing with her")
				sleep(.5)
				alert("You died")
			if argueChoice == 1:
				alert("she was angered by you, but decided to make nothing of it and instead grabs you with her inhuman strength and drags you behind her")
				sleep(1)
				alert("She leads you into the RIGHT door way where you go into an open field with all sorts of animals and people enjoying the aromic garden that seemed to span the horizon.")
				alert(" A rock fell from the sky and killed you")
				alert("You died")
	
	
	#OUTCOME 2 FOR CHOICE 1
	if Choice_1_Value == 1:
		alert(" A young boy with tears in his eyes walks into the room with a brown rabbit in his arms, the rabbit seems lifeless, you are suddenly hungry")
		sleep(.5)
		alert("What do you do, HELP, EAT")
		Choice_2 = raw_input("HELP, EAT")
		if Choice_2 =="HELP":
			alert("You decided to HELP the boy and proceeds to shake the rabbit to life, the boy is overjoyed! He asks you your name?")
			tellName = raw_input("TELL, NOTHING")
			if tellName == "TELL":
				alert("you replied with",Character_name)
				alert("The boy writes your name down in a book he takes out of his pocket")
				sleep(.5)
				alert("You died")
		if Choice_2 == "EAT":
			alert("you ripped the bunny away from the boy, and proceed in devouring the animal, your stomach doesn't seem to enjoy the rabbit")
			sleep(.5)
			alert(" eating a raw rabbit killed you")
	
	
	
	#outcome 3 FOR CHOICE 1
	
	if Choice_1_Value == 2:
		alert("The door opens and a husky puma, pounces into the room, he stares at you what do you do?")
		Choice_2 = raw_input("FIGHT, RUN")
		if Choice_2 == "FIGHT":
			fightChoice = choice(fightChoice)
			if fightChoice == 0:
				alert("You decided to FIGHT the puma")
				sleep(.5)
				alert("The puma killed you")
				sleep(.5)
				alert("The end")
			if fightChoice == 1:
				alert("You decided to FIGHT a puma bare handed")
				sleep(.5)
				alert("well you must be tarzan or something because you somehow won the fight")
				sleep(.5)
				alert("the adrenaline from fighting a puma and winning kills you")
		if Choice_2 == "RUN":
			alert("You decided to RUN")
			sleep(.5)
			alert("You looked around the room and decided to make a run towards the left door, you narrowly escape the puma as you close the door behind you. There is a long corridor to explore with many familiar paintings on the walls")
			alert("The puma didn't forget about you")
			sleep(.5)
			alert("The puma killed you")