'''
File: w05_textadventure_msa.py
Author: Max Appleton (msa)

Purpose: A text based adventure game.
'''
#-----------------------------------------------------------------------------------
loop = 1
print('\n----------------------------------------------------------------------------------------------\n')
print('Welcome to my text adventure game "The Twilight Meadow"')
print('If at anytime you want to exit the game just type "EXIT" or "STOP".')

#The game
while True:
    #Scenario 1 START
    while loop == 1:
        if loop == 1:
            print('\n----------------------------------------------------------------------------------------------\n')
            print('You awake in a twilight lit meadow, with a dull fuzzy pain in the back of your head.') 
            print('There is a path to your SOUTH towards the forest. You have a bag, and a flashlight with you.')
            print('As you take stock of where you are you see an obscured path to the WEST.') 
            print('Looks like there is a house there.')
            choice = input('\nWhere will you go? ').upper()
        #Result of heading SOUTH
        if choice == 'SOUTH':
            print('\n----------------------------------------------------------------------------------------------\n')
            print('You head south into the forest.')
            loop = 2
        #Result of heading WEST
        elif choice == 'WEST':
            print('\n----------------------------------------------------------------------------------------------\n')
            print('You are traveling west, towards what looks like a house.')
            loop = 4
        #Exit Condiditon
        elif choice in ['EXIT', 'STOP']:
            loop = 10
        #Reset to the beginning of the current loop to get a correct answer.
        else:
            print('\n----------------------------------------------------------------------------------------------\n')
            print('Please pick a correct option.')

    #Scenario 2 SOUTH of START
    while loop == 2:
        if loop ==2:
            print('\n----------------------------------------------------------------------------------------------\n')
            print('As you travel down the southern path, the forest becomes dark and twisted. The dull pain in your')
            print('head increases as you travel. The trees start to thicken and the light begins to fade, perhaps') 
            print('the FLASHLIGHT can provide some light. You can always go back NORTH.')
            print('There is a sound in the brush to your EAST. You could investigate it.')
            choice = input('\nWhat will you do? ').upper()
        #Result of using your FLASHLIGHT
        if choice == 'FLASHLIGHT':
            print('\n----------------------------------------------------------------------------------------------\n')
            print('You turn on your flashlight and look around.')
            loop = 3
        #Result of going NORTH
        elif choice == 'NORTH':
            print('\n----------------------------------------------------------------------------------------------\n')
            print('You return to the meadow, leaving the forest.')
            loop = 1
        #Result of going EAST
        elif choice == 'EAST':
            print('\n----------------------------------------------------------------------------------------------\n')
            print('As you travel into the brush a little ways you see a rabbit bolt from under a bush.')
            print('Could be fun to chase it.')
            chase = input('').upper()
            if chase == 'CHASE':
                print('\n----------------------------------------------------------------------------------------------\n')
                print('You begin to chase the rabbit.')
                loop = 8
            else:
                print('\nThe rabbit got away. You return to the trail you were already on.')
        #Exit Condiditon
        elif choice in ['EXIT', 'STOP']:
            loop = 10
        #Reset to the beginning of the current loop to get a correct answer. 
        else:
            print('\n----------------------------------------------------------------------------------------------\n')
            print('Please pick a correct option.')

    #Scenario 3 Hidden Ladder
    while loop == 3:
        if loop == 3:
            print('\n----------------------------------------------------------------------------------------------\n')
            print('As you look around there is a hole and a ladder underneath a small tree. Do you want to go DOWN')
            print('the ladder or RETURN the way you came?')
            choice = input('\nWhat will you do? ').upper()
        #Result of choosing DOWN
        if choice == 'DOWN':
            print('\n----------------------------------------------------------------------------------------------\n')
            print('You go down the ladder.')
            loop = 6
        #Result of choosing RETURN
        elif choice == 'RETURN':
            print('\n----------------------------------------------------------------------------------------------\n')
            print('You return to the meadow, leaving the forest to the north.')
            loop = 1
        #Exit Condiditon
        elif choice in ['EXIT', 'STOP']:
            loop = 10
        #Reset to the beginning of the current loop to get a correct answer. 
        else:
            print('\n----------------------------------------------------------------------------------------------\n')
            print('Please pick a correct option.')
    
    #Scenario 4 WEST to the house
    while loop == 4:
        if loop == 4:
            print('\n----------------------------------------------------------------------------------------------\n')
            print('As you are walking west you see a house, old and abandoned, left to be slowly relcaimed by')
            print('nature. Vines and moss seem to be engulfing what is left of the house. The path you are on')
            print('continues to the WEST, there is also a path NORTH to the house. You see a MAILBOX in front of')
            print('you, rusted and bent. There is also the meadow EAST, back the way you came.')
            choice = input('\nWhat do you do? ').upper()
        #Result of WEST
        if choice == 'WEST':
            print('\n----------------------------------------------------------------------------------------------\n')
            print('You continue west down the path as you do you find a road. After awhile you are able to flag')
            print('down a car and geta ride to the nearest town. Still a mystery what happened to you, and this')
            print('darn pain in your head just wont go away.')
            print('\nWelcome to the ending of "Twilight Meadow", feel free to play again.')
            loop = 10
        #Result of NORTH
        elif choice == 'NORTH':
            print('\n----------------------------------------------------------------------------------------------\n')
            print('You head towards the house.')
            loop = 5
        #Result of MAILBOX
        elif choice == 'MAILBOX':
            print('\n----------------------------------------------------------------------------------------------\n')
            print('Welcome to "Twilight Meadow", your goal is to get rid of the pain your head. Good luck!')
        #Result of EAST
        elif choice == 'EAST':
            print('\n----------------------------------------------------------------------------------------------\n')
            print('You head back to the meadow where you woke up. Leaving the house and path behind.')
            loop = 1
        #Exit Condiditon
        elif choice in ['EXIT', 'STOP']:
            loop = 10
        #Reset to the beginning of the current loop to get a correct answer. 
        else:
            print('\n----------------------------------------------------------------------------------------------\n')
            print('Please pick a correct option.')
    
    #Scenario 5 NORTH of WEST of START
    while loop == 5:
        if loop == 5:
            print('\n----------------------------------------------------------------------------------------------\n')
            print('As you head towards the house you see the door is slightly ajar. Looks like you could go INSIDE.')
            print('You also see that there is a path AROUND the house, perhaps there is something in the back.')
            print('Could head BACK to the path as well, go another way.')
            choice = input('\nWhat do you do? ').upper()
        #Result for INSIDE
        if choice == 'INSIDE':
            print('\n----------------------------------------------------------------------------------------------\n')
            print('You head inside the house, pushing the door aside.')
            loop = 7
        elif choice == 'AROUND':
            print('\n----------------------------------------------------------------------------------------------\n')
            print('You go around the house, and there is nothing in the backyard except an abandoned dog house.')
            print('you go back to the front of the house.')
        elif choice == 'BACK':
            print('\n----------------------------------------------------------------------------------------------\n')
            print('You go back to path at the fence.')
            loop = 4
        #Exit Condiditon
        elif choice in ['EXIT', 'STOP']:
            loop = 10
        #Reset to the beginning of the current loop to get a correct answer. 
        else:
            print('\n----------------------------------------------------------------------------------------------\n')
            print('Please pick a correct option.')
    
    #Scenario 6 The hidden hole
    while loop == 6:
        if loop == 6:
            print('\n----------------------------------------------------------------------------------------------\n')
            print('As you go down the ladder you find yourself in a dark short tunnel. As you move forward the cave')
            print('opens up into a small room, smelling richly of earth. You see a small twisted looking emblem in')
            print('front of you made of stick and bone. As you look at it you feel entranced by it as the pain in')
            print('your head grows stronger. You feel compelled to LOOK at it, but part of you wants to BREAK it,') 
            print('or RUN away as fast as you can.')
            choice = input('\nWhat will you do? ').upper()
        #Result of LOOK
        if choice == 'LOOK':
            print('\n----------------------------------------------------------------------------------------------\n')
            print('As you continue to stare into the emblem, the pain continues to grow in your head.')
        #Result of BREAK
        elif choice == 'BREAK':
            print('\n----------------------------------------------------------------------------------------------\n')
            print('You smash the emblem in front of you. As you do the pain in your head vanishes. This place is')
            print('creepy. You head back to the meadow where you woke up.')
            loop = 1
        #Result of RUN
        elif choice == 'RUN':
            print('\n----------------------------------------------------------------------------------------------\n')
            print('You run as fast as you can, just knowing that you need to get away as fast as possible. Running') 
            print('back to the meadow, at least you felt safe there, although the pain in your head still remains.')
            loop = 1
        #Exit Condiditon
        elif choice in ['EXIT', 'STOP']:
            loop = 10
        #Reset to the beginning of the current loop to get a correct answer. 
        else:
            print('\n----------------------------------------------------------------------------------------------\n')
            print('Please pick a correct option.')

    #Scenario 7 The house
    while loop == 7:
        if loop == 7:
            print('\n----------------------------------------------------------------------------------------------\n')
            print('As you walk through the door you see that there is a chest of drawers right next to the door.')
            print("You see some STAIRS headed to the second floor and perhaps a bathroom, it's pretty dark thought,")
            print('might need your flashlight. Past the STAIRS you see a KITCHEN, could be worth investigating.') 
            print('Could always go BACK outside and go somewhere else.')
            choice = input('\nWhat do you do? ').upper()
        #Result for STAIRS
        if choice == 'STAIRS':
            print('\n----------------------------------------------------------------------------------------------\n')
            print('You head up the stairs and do find a bathroom, there is not much here. There are a few medicine')
            print('bottles around, one even has pills labeled as Tylenol. Could TAKE the pills maybe they would help.')
            choice_2 = input('\nDo you take the PILLS? Y/N: ').upper()
            #Decision making about the PILLS
            if choice_2 == 'Y':
                print('\n----------------------------------------------------------------------------------------------\n')
                print('You take the PILLS and head back downstairs')
            elif choice_2 == 'N':
                print('\n----------------------------------------------------------------------------------------------\n')
                print('You do not TAKE the PILLS and head back downstairs')
            else:
                print('\n----------------------------------------------------------------------------------------------\n')
                print('Please pick a correct option.')
        #Result for KITCHEN
        elif choice == 'KITCHEN':
            print('\n----------------------------------------------------------------------------------------------\n')
            print('You walk past the stairs, there is a table thats broken and some chairs, as you test the faucet')
            print('for water, it does have some water. Could DRINK some if you wanted')
            choice_3 = input('\nDo you take a DRINK? Y/N: ').upper()
            #Decision about the WATER
            if choice_3 == 'Y':
                print('\n----------------------------------------------------------------------------------------------\n')
                print('You take a drink and feel refreshed and head back to the front of the house.')
            elif choice_3 == 'N':
                print('\n----------------------------------------------------------------------------------------------\n')
                print('You do not take a drink, should not risk drinking abandoned house water.')
                print('You head back to the front of the house.')
            else:
                print('\n----------------------------------------------------------------------------------------------\n')
                print('Please pick a correct option.')
        #Result for BACK
        elif choice == 'BACK':
            print('\n----------------------------------------------------------------------------------------------\n')
            print('You go back to path at the fence.')
            loop = 5
        #Exit Condiditon
        elif choice in ['EXIT', 'STOP']:
            loop = 10
        #Reset to the beginning of the current loop to get a correct answer. 
        else:
            print('\n----------------------------------------------------------------------------------------------\n')
            print('Please pick a correct option.')

    #Scenario 8 Rabbit CHASE
    while loop == 8:
        if loop ==8:
            print('\n----------------------------------------------------------------------------------------------\n')
            print('The rabbit bolts away wildly from the bush, darting quickly through the underbrush.')
            print('The rabbit is getting hard to see. Do you dart LEFT, RIGHT, or Just go STRAIGHT ahead?')
            choice = input('What do you do? ').upper()
        #Result for going LEFT or RIGHT
        if choice in ['LEFT', 'RIGHT']:
            print('\n----------------------------------------------------------------------------------------------\n')
            print('You seem to have lost the rabbit. You can hear it but you cannot see it. Too bad, I guess you')
            print('should go back to the trail.')
            loop = 2
        #Result for going STRAIGHT
        elif choice == 'STRAIGHT':
            print('\n----------------------------------------------------------------------------------------------\n')
            print('You rush forward and leap through the air! As you do so you catch the rabbit! So congratulations')
            print('you have a rabbit do not know what you are going to do with them, but hey you have one.')
            print('You return to the trail with your new friend.')
            loop = 2
        #Exit Condiditon
        elif choice in ['EXIT', 'STOP']:
            loop = 10
        #Reset to the beginning of the current loop to get a correct answer. 
        else:
            print('\n----------------------------------------------------------------------------------------------\n')
            print('Please pick a correct option.')

    #Exit loop
    while loop == 10:
        #Starting the Exit loop
        if loop == 10:
            print('\n----------------------------------------------------------------------------------------------\n')
            exit_inp = input('\nDo you want to continue?\nY/N: ').upper()
        #Exiting the loop and ending the game
        if exit_inp == 'N':
            print('\nThanks for playing!')
            exit()
        #Restarting the game
        elif exit_inp == 'Y':
            print('\nWell then, back to the beginning with you!')
            loop =1
        #Reset to the beginning of the current loop to get a correct answer.
        else:
            print('\n----------------------------------------------------------------------------------------------\n')
            print('Please pick a correct option.')