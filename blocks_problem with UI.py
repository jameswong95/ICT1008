import sys
import table

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
    start_state = str(input(startStateReq))
    final_state = str(input(endStateReq))

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
    stack = []
    arm = []
    temp_stack = {}
    temp1_stack = {}
    steps = []
    combine_tstack = []

    # loop each tower in final state
    for i in range(len(final_state)):
        if len(final_state[i]) == 1:
            temp_stack = {}
            temp_stack.update([('type', 'predicate'), ('name', 'ontable'), ('params', final_state[i])])
            combine_tstack.append(temp_stack)
            temp_stack = {}
            temp_stack.update([('type', 'predicate'), ('name', 'clear'), ('params', final_state[i])])
            combine_tstack.append(temp_stack)
        else:
            for j in range(len(final_state[i])):
                if j == 0:
                    temp_stack = {}
                    temp_stack.update([('type', 'predicate'), ('name', 'on'),
                                       ('params', final_state[i][j] + "," + final_state[i][j + 1])])
                    combine_tstack.append(temp_stack)
                    temp1_stack = {}
                    temp1_stack.update([('type', 'predicate'), ('name', 'clear'), ('params', final_state[i][j])])
                    combine_tstack.append(temp1_stack)
                elif j != len(final_state[i]) - 1:
                    temp_stack = {}
                    temp_stack.update([('type', 'predicate'), ('name', 'on'),
                                       ('params', final_state[i][j] + "," + final_state[i][j + 1])])
                    combine_tstack.append(temp_stack)
                else:
                    temp1_stack = {}
                    temp1_stack.update([('type', 'predicate'), ('name', 'ontable'), ('params', final_state[i][j])])
                    combine_tstack.append(temp1_stack)
    stack.append(combine_tstack)
    for i in combine_tstack:
        stack.append(i)

    temp_start_stack = []
    counter_test = 1
    # loop each tower in start state
    counter = 0
    while counter_test == 1:
        for i in range(len(start_state)):
            if len(start_state[i]) == 1:
                temp_stack = {}
                temp_stack.update([('type', 'predicate'), ('name', 'ontable'), ('params', start_state[i])])
                temp_start_stack.append(temp_stack)
                temp_stack = {}
                temp_stack.update([('type', 'predicate'), ('name', 'clear'), ('params', start_state[i])])
                temp_start_stack.append(temp_stack)
            else:
                for j in range(len(start_state[i])):
                    if j == 0:
                        temp_stack = {}
                        temp_stack.update([('type', 'predicate'), ('name', 'clear'), ('params', start_state[i][j])])
                        temp_start_stack.append(temp_stack)
                        temp1_stack = {}
                        temp1_stack.update([('type', 'predicate'), ('name', 'on'),
                                            ('params', start_state[i][j] + "," + start_state[i][j + 1])])
                        temp_start_stack.append(temp1_stack)
                    elif j == len(start_state[i]) - 1:
                        temp1_stack = {}
                        temp1_stack.update([('type', 'predicate'), ('name', 'ontable'), ('params', start_state[i][j])])
                        temp_start_stack.append(temp1_stack)
                    else:
                        temp_stack = {}
                        temp_stack.update([('type', 'predicate'), ('name', 'on'),
                                           ('params', start_state[i][j] + "," + start_state[i][j + 1])])
                        temp_start_stack.append(temp_stack)
        counter_test = 0

    while len(stack) > 0:
        list_counter = 0
        combine_tstack = []
        unstackfrom = ""
        if type(stack[-1]) is list:
            list_counter = 0
            ele_notfound = ""
            for i in temp_start_stack:
                for j in stack[-1]:
                    if i == j:
                        list_counter += 1

            if len(stack) > 1:
                if len(arm) == 0 or len(arm) == 1:
                    list_counter += 1
            if list_counter == len(stack[-1]):
                stack.pop()
            else:
                stack.append(i)

        elif stack[-1]['type'] == 'predicate':

            if stack[-1] in temp_start_stack:
                stack.pop()
            else:
                temp_stack = {}
                temp1_stack = {}
                temp2_stack = {}
                temp3_stack = {}
                if stack[-1]['name'] == 'on':
                    current_stack = stack[-1]
                    new_value = current_stack['params']
                    temp1_stack = {}
                    temp1_stack.update(
                        [('type', 'action'), ('name', 'stack'), ('params', new_value[0] + "," + new_value[2])])
                    stack.append(temp1_stack)
                    temp_stack = {}
                    temp_stack.update([('type', 'predicate'), ('name', 'clear'), ('params', new_value[2])])
                    combine_tstack.append(temp_stack)
                    temp1_stack = {}
                    temp1_stack.update([('type', 'predicate'), ('name', 'holding'), ('params', new_value[0])])

                    combine_tstack.append(temp1_stack)
                    stack.append(combine_tstack)
                    for i in combine_tstack:
                        stack.append(i)
                    combine_tstack = []
                    temp1_stack = {}
                    temp1_stack.update([('type', 'action'), ('name', 'pickup'), ('params', new_value[0])])
                    stack.append(temp1_stack)
                    temp_stack = {}
                    temp_stack.update([('type', 'predicate'), ('name', 'armempty'), ('params', "")])
                    temp1_stack = {}
                    temp1_stack.update([('type', 'predicate'), ('name', 'clear'), ('params', new_value[0])])
                    temp2_stack = {}
                    temp2_stack.update([('type', 'predicate'), ('name', 'ontable'), ('params', new_value[0])])
                    combine_tstack.append(temp_stack)
                    combine_tstack.append(temp2_stack)
                    combine_tstack.append(temp1_stack)

                    stack.append(combine_tstack)
                    for i in combine_tstack:
                        stack.append(i)

                elif stack[-1]['name'] == 'ontable':
                    if stack[-1] in temp_start_stack:
                        stack.pop()
                    # print "in"
                    else:
                        temp1_stack = {}
                        temp_stack = {}
                        temp2_stack = {}
                        current_stack = stack[-1]
                        new_value = current_stack['params']
                        # print new_value

                        i = 0
                        while not unstackfrom and i < len(temp_start_stack):
                            if temp_start_stack[i]['name'] == 'on' and temp_start_stack[i]['params'][
                                2] == new_value:
                                unstackfrom = temp_start_stack[i]['params'][0]
                                temp_stack.update(
                                    [('type', 'predicate'), ('name', 'armempty'), ('params', new_value)])
                                combine_tstack.append(temp_stack)
                                temp1_stack.update(
                                    [('type', 'action'), ('name', 'unstack'),
                                     ('params', unstackfrom + "," + new_value)])

                            elif temp_start_stack[i]['name'] == 'on' and temp_start_stack[i]['params'][
                                0] == new_value:
                                unstackfrom = temp_start_stack[i]['params'][2]
                                temp_stack.update(
                                    [('type', 'predicate'), ('name', 'armempty'), ('params', new_value)])
                                combine_tstack.append(temp_stack)
                                temp1_stack.update(
                                    [('type', 'action'), ('name', 'unstack'),
                                     ('params', new_value + "," + unstackfrom)])
                            i += 1

                        temp_stack = {}
                        temp3_stack = {}
                        for i in combine_tstack:
                            stack.append(i)
                        stack.append(temp1_stack)
                elif stack[-1]['name'] == 'clear':
                    current_stack = stack[-1]
                    new_value = current_stack['params']
                    temp_stack = {}
                    temp_stack.update([('type', 'predicate'), ('name', 'armempty'), ('params', new_value)])
                    stack.append(temp_stack)
                    temp_stack = {}
                    for i in temp_start_stack:
                        if i['name'] == 'on':
                            if i['params'][2] == new_value:
                                new_value = i['params']
                                temp_stack = {}
                                temp_stack.update([('type', 'action'), ('name', 'unstack'), ('params', new_value)])
                    new_value2 = temp_stack["params"]
                    stack.append(temp_stack)
                    temp_stack = {}
                    temp2_stack = {}
                    temp3_stack = {}

                    temp_stack.update([('type', 'predicate'), ('name', 'armempty'), ('params', new_value[0])])
                    temp1_stack.update([('type', 'predicate'), ('name', 'on'), ('params', new_value2)])
                    temp2_stack.update([('type', 'predicate'), ('name', 'clear'), ('params', new_value2[0])])
                    combine_tstack.append(temp_stack)
                    combine_tstack.append(temp1_stack)
                    combine_tstack.append(temp2_stack)
                    stack.append(combine_tstack)
                    for i in combine_tstack:
                        stack.append(i)
                elif stack[-1]['name'] == 'holding':
                    current_stack = stack[-1]
                    new_value = current_stack['params']
                    if arm[0] == new_value:
                        stack.pop()
                elif stack[-1]['name'] == 'armempty':
                    current_stack = stack[-1]
                    temp_stack = {}
                    new_value = current_stack['params']
                    temp1_stack = {}
                    for i in arm:
                        arm_value = i
                    if len(arm) == 0:
                        stack.pop()
                    else:
                        combine_tstack = []
                        temp1_stack.update([('type', 'action'), ('name', 'putdown'), ('params', arm_value)])
                        stack.append(temp1_stack)
                        temp_stack.update([('type', 'predicate'), ('name', 'holding'), ('params', arm_value)])
                        combine_tstack.append(temp_stack)
                        stack.append(combine_tstack)
                        for i in combine_tstack:
                            stack.append(i)
        else:
            current_stack = stack[-1]
            new_name = current_stack['name']
            new_value = current_stack['params']
            if new_name == 'unstack':
                steps.append(current_stack)
                new_value2 = new_value[2]
                temp_stack = {}
                temp_stack.update([('type', 'predicate'), ('name', 'clear'), ('params', new_value[2])])
                temp_start_stack.append(temp_stack)
                for i in temp_start_stack:
                    if i['name'] == 'on' and i['params'] == str(new_value[0]) + "," + str(new_value[2]):
                        ele_found = i
                        temp_start_stack.remove(i)
                for i in temp_start_stack:
                    if i['name'] == 'clear' and i['params'] == new_value[0]:
                        ele_found = i
                        temp_start_stack.remove(i)

                arm.append(new_value[0])
                stack.pop()
            elif new_name == 'pickup':
                arm.append(new_value)
                for i in temp_start_stack:
                    if i['name'] == 'clear' and i['params'] == new_value:
                        ele_found = i
                        temp_start_stack.remove(i)
                for i in temp_start_stack:
                    if i['name'] == 'ontable' and i['params'] == new_value:
                        ele_found = i
                        temp_start_stack.remove(i)
                for i in temp_start_stack:
                    if i['name'] == 'on' and i['params'][0] == new_value:
                        ele_found = i
                        temp_start_stack.remove(i)
                stack.pop()
                steps.append(current_stack)
            elif new_name == 'stack':
                for i in temp_start_stack:
                    if i['name'] == 'clear' and i['params'] == new_value[2]:
                        ele_found = i
                        temp_start_stack.remove(i)
                temp_stack.update([('type', 'predicate'), ('name', 'clear'), ('params', new_value[0])])
                temp1_stack.update(
                    [('type', 'predicate'), ('name', 'on'), ('params', new_value[0] + "," + new_value[2])])
                temp_start_stack.append(temp_stack)
                temp_start_stack.append(temp1_stack)
                stack.pop()
                steps.append(current_stack)
                arm.pop()
            elif new_name == 'putdown':
                temp_stack = {}
                temp1_stack = {}
                if len(new_value) == 1:
                    temp_stack.update([('type', 'predicate'), ('name', 'clear'), ('params', new_value)])
                    temp1_stack.update([('type', 'predicate'), ('name', 'ontable'), ('params', new_value)])
                    temp_start_stack.append(temp_stack)
                    temp_start_stack.append(temp1_stack)
                else:
                    temp_stack.update([('type', 'predicate'), ('name', 'clear'), ('params', new_value[0])])
                    temp1_stack.update(
                        [('type', 'predicate'), ('name', 'on'), ('params', new_value[0] + "," + new_value[2])])
                    temp_start_stack.append(temp_stack)
                    temp_start_stack.append(temp1_stack)
                stack.pop()
                steps.append(current_stack)
                arm.pop()
        counter += 1

    # print "Steps: ",steps
    print("\nSteps  :  Action(s)")
    for i in steps:
        if i['name'] == 'putdown':
            print(steps.index(i), "     : ", i['name'], ",", i['params'], "on table")
        elif i['name'] == 'pickup':
            print(steps.index(i), "     : ", i['name'], ",", i['params'], "from table")
        else:
            if i['name'] == 'unstack':
                print(steps.index(i), "     : ", i['name'], i['params'][0], "from", i['params'][2])
            else:
                print(steps.index(i), "     : ", i['name'], i['params'][0], "to", i['params'][2])


def solutionTwo(start_state, final_state):
    # Enter Solution 2 here
    start_table = table.createTable(str(start_state))
    goal_table = table.createTable(str(final_state))

    dict = table.alt(start_table, goal_table)

    # print output
    for key, value in dict.items():
        print("Move {0}:".format(key))
        for a, b in value.items():
            print("{0}: {1}".format(a, b))

# initialize main method
main()
