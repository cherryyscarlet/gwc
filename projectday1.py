start = '''
You're offered a promotion at Disneyland. You have been waiting 2 years for this offering. 
Your task is to do your job correctly or be fired
'''
keepplaying = "yes"
print(start)

while keepplaying == "Yes" or keepplaying == "yes": 
    userChoice = input("It's your first day on the job and already a ride has broken down due to ears that have fallen off someone's head. Type 1 to get the people off the ride and fix it. Type 2 to keep them in a never ending anguish")
    if userChoice == "1":
        print("You stop the ride and allow the riders to get off. You quickly fix it. You have not yet disgraced Walt Disney")
        print("Congratulations. You may go on to the next task")
        print("")
        keepplaying = "no"
    elif userChoice == "2": 
        print("The riders scream in agony. Your manager comes to scream at you while you are eating a chimichanga")
        print("You have been fired and have been known to be the worst Disneyland employee on a Buzzfeed news article.")
        keepplaying = input("Would you like to try again? Type yes or no. ")
        if keepingplaying == "no"
            quit()
    else: 
        print("Please select one of the valid options: 1 or 2. ")
        if keepplaying == "no": 
            quit()

keepplaying = "yes"
 while keepplaying == "Yes" or keepplaying == "yes": 
    userChoice = input("Oh no! You have heard a rumor that an unvaccinated child has the measles. You have located the child and see the rash on his arm. Type 1 to kick out patient zero before it spreads. Type 2 if you allow them to stay and repeat 2014 all over again")
    if userChoice == "1": 
        print("Good choice. You have prevented the death of millions.")
        print("You may proceed to your next task")
    elif  userChoice == "2":
        print("As you walk away from the family, you see a rash appear on your leg. Soon you are diagnosed with measles!")
        print("You have been asked to never come back again. ")
        keepplaying = input("Would you like to try again? Type yes or no. ")
        if keepplaying == "no":
            quit()
