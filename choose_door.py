choices = False

print('You woke up in a mysterious room and there are three doors that you')
print('can use to get out of there: DOOR ONE, and DOOR TWO, and DOOR THREE.')

choices = input('Which door do you choose to leave the room? ')
print("================================================")
if choices.lower() in ('door one', 'door 1', 'one', '1'):
    print("You entered in door one and found a singboard that say 'The nearest town is 10 miles away.")
    print("You have two options to make the trip of 10 miles: a CAR or a BICYCLE.")

    choice1 = input('Which one do you choose?: ')
    if choice1.lower() == 'car':
        print('You chose the car and after you drove during three miles the car ran out of gas,')
        print('but you still have to make 7 miles to get to the Town. You have option A: come back')
        print('to pick up the bicycle or option B: walk the 7 miles')
        choices1_2 = input('Which option do you choose: A or B? ')
        if choices1_2.lower() == 'a':
            print("You came back fot the bicycle, but the bicycle is gone.Now you have to walk the 10")
            print("miles to get to the Town.'The end'")
        elif choices1_2.lower() == 'b':
            print("After you walked the 7 miles you got to the Town.'CONGRATULATION'")
        else:
            print('Your only two options are A nad')
    elif choice1.lower() == 'bicycle':
        print('You drove the bicycle for 5 miles, but now the road splits in two ways.')
        choice1_3 = input('Which way do you want to follow: RIGHT or LEFT? ')
        if choice1_3.lower() == 'right':
            print('You took the right way, after you drove the bicycle for 5 minutes you found a')
            print('celphone that you can use to ask for help.')
        elif choice1_3.lower() == 'left':
            print('You decided to go for the left way, but in the left way there are 3 lion')
            print('coming for you.')
    else:
        print("you did not choose bicycle, nor car.")

elif choices.lower() in ('door two', 'door 2', 'two', '2'):
    print('You entered in door two, and there is a person coming for you. You have option 1: ask him')
    choice2 = input("for help or option 2: run . Which option do yuo prefer '1' or '2'? ")
    if choice2 == '1':
        print('You chose to ask him for help, but he just wants to use you for his experiments')
    elif choice2 == '2':
        print(' You ran faster as you could, and you found the police station. Now you are safe')
        print('because the police helped you to get back home')

elif choices.lower() in ('door three', 'door 3', 'three', '3'):
    print('You entered in door three and now you are in a nice place with all that you need')
    print('to be comfortable. You can stay there or you can go home. What do you want:')
    choice3 = input('STAY/HOME? ')
    if choice3.lower() == 'stay':
        print('You decided to stay, but you realized the this magical place is no real, and')
        print('all it was just your imagination')
    elif choice3.lower() == 'home':
        print('You woke up again, but this time you are at your home, and you are glad it')
        print('was just a dream')
else:
    print("you did not choose any door, you can continue with your life")

