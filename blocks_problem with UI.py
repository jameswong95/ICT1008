import sys
import table
import time
from solutionOne import *

# Edit log(s) :
# 1 Edited block_problem.py for a basic UI
#   [IMPORTANT] Refactored code to python 3.6
# 2 (10/03/2019)
# - Implemented algo 2
# - Move split string to before algo 1 is being called.

# Test cases:
# final_state = '123'
# start_state = '1 32'

# final_state = '63 245 1'
# start_state = '2 3 16 5 4'

# final_state = '1 3 2 6 54'
# start_state = '23 1 654'

# final_state = '6 32 451'
# start_state = '2 31654'

# final_state = '6 32 45 1'
# start_state = '2 316 54'

# final_state = '6 3245 1'
# start_state = '2 316 54'

# final_state = '63 245 1'
# start_state = '2 316 54'

# final_state = '63 24 5 1'
# start_state = '231654'

#Current Stack
# <-- Top | Bottom -->
# final_state = '12345'
# start_state = '1 32 4 5'

# Message(s)
welcome = "= = = = = = ICT 1008, Simple AI Block's Problem. = = = = = =\n"
startStateReq = "Enter your initial Start state : "
endStateReq = "Enter your final Goal state : "
selectionChoice = "\nSelect your choice of algorithm. \n[1] Algorithm 1\n[2] Algorithm 2\n"
goBackMaybe = "\nEnter [Y] if you wish to repeat the program.\nEnter any other button to quit."
# Error Message(s)
genericError = "[ERROR] You shouldn't be here."
repFound = "[ERROR] Repeated character input found! Please check your that you have not entered a reapeated character\n"
selectionError = "[ERROR] Invalid Selection made."
noChange = "No Change(s) required as Start state and End state are the same."

def main():
    # Program starts here!
    print(welcome)
    start_state = str(raw_input(startStateReq))
    final_state = str(raw_input(endStateReq))

    # Check for user input
    # if there is an issue with duplicate numbers/alphabets
    if (checkForRep(start_state) is True) or (checkForRep(final_state) is True):
        print(repFound)
        main() # Throws user back to main to repeat inputs
    else:
        #start_state = start_state.split(" ")
        #final_state = final_state.split(" ")

        # Check if goal state is the same as start state.
        if checkStartnFinal(start_state, final_state) is True:
            # Splinter points for the 2 Algorithm
            print(selectionChoice)
            userSelection = input()

            if str(userSelection) == "1":  # [1] James's Algorithm Solution
                start_state = str(start_state).split(" ")
                final_state = str(final_state).split(" ")
                solutionOne(start_state, final_state)
            elif str(userSelection) == "2":  # [2] Algorithm Solution
                solutionTwo(start_state, final_state)
            else:
                print(genericError)

            # Offer user to repeat the program
            print(goBackMaybe)
            userSelection = raw_input() # Changed from original to Python 2.
            if userSelection == "y" or userSelection == 'Y':
                main()
            sys.exit

# Check if there are repeated character in String
# return 'True' when there are repeating characters
def checkForRep(toCheck):
    removeSpaces = str(toCheck).replace(" ","")
    seen = set()
    for x in removeSpaces:
        if x not in seen:
            seen.add(x)
        else:   # Repeated character found
            return True


# Check if Goal condition is the same as the Start condition.
# Eg : Start 123, End 123
def checkStartnFinal(start_state, final_state):
    if start_state == final_state:  # Basically O(1) if no sorting is required.
        print(noChange)
        return False    # No need to continue with the rest of the program.
    else:
        return True     # Continue with the whole sorting of blocks


def solutionOne(start_state, final_state):
    algo(start_state,final_state)


def solutionTwo(start_state, final_state):
    # Enter Solution 2 here
    start_table = table.createTable(str(start_state))
    goal_table = table.createTable(str(final_state))

    start = time.clock()
    dict = table.alt(start_table, goal_table)
    completed = time.clock() - start

    # print output
    for key, value in dict.items():
        print("Move {0}".format(key))
        for a, b in value.items():
            print("{0}: {1}".format(a, b))
            # remove break to print held block & block position
            break
    print "Time Completed in: ", completed

# initialize main method
main()
