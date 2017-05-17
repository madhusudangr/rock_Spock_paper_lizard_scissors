import random
# The key idea of this program is to play the big bang theory version of the iconic Rock Paper scissors with computer as the second player

def name_to_number(name):
    if name=='rock' :
        return 0
    elif name=='Spock' :
        return 1
    elif name=='paper' :
        return 2
    elif name=='lizard' :
        return 3
    elif name=='scissors' :
        return 4
    else :
        print('Wrong option please enter another value')
        return -1;
    


def number_to_name(number):
    if number==0:
        return "rock"
    elif number==1:
        return "Spock"
    elif number==2:
        return "paper"
    elif number==3:
        return "lizard"
    elif number==4:
        return "scissors"
    else :
        print('wrong number please enter another number')
        return -1;
    

def rpsls(player_choice): 
    
    # print a blank line to separate consecutive games
    print(" ")
    # print out the message for the player's choice
    print ("Player's choice, %s"%player_choice)
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,4,1)
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    # print out the message for computer's choice
    print ("Computer's choice, %s"%comp_choice)
    # compute difference of comp_number and player_number modulo five
    ans = (comp_number-player_number)%5
    # use if/elif/else to determine winner, print winner message
    if ans==0: print ("Plyer and Computer Tie!")
    elif ans==1 or ans==2: print ("Computer Wins")
    elif ans==3 or ans==4: print ("Player Wins")
    

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")



