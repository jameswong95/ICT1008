from block_stack import *
from functions import *


def createTable(table):
    stack_list = table.split()  # split the strings
    numOfStack = len(stack_list)  # set the number of stacks required
    table_stacks = [Stack() for i in range(numOfStack)]  # create the number of stacks

    # add blocks onto stacks which are on the table
    for string in stack_list:
        for char in string:
            table_stacks[stack_list.index(string)].push(char)

    return table_stacks


def classicalPlanning(init_stacks, goal_stacks):

    # to hold each movement #
    moveStack = []  # to record all movements made
    stackPosition = []  # to record the movements of the block

    # if initial stack has lesser stacks than goal stacks, add until they have the same amount of stacks
    while len(init_stacks) < len(goal_stacks):
        init_stacks = addStack(init_stacks)

    # size of current stacks #
    init_size = len(init_stacks)
    goal_size = len(goal_stacks)

    # copy from initial stack to temp stack
    temp_stacks = [Stack() for i in range(init_size)]
    for i in range(init_size):
        temp_stacks[i] = init_stacks[i].copyTo()

    temp_size = len(temp_stacks)
    arm = armFunction()  # declare robot arm

    incorrect_index = []

    # comparing individual stacks #
    # compare number of stacks
    if init_size > goal_size:
        pass
    elif init_size is goal_size:
        # check if stack have the same length
        for i in range(temp_size):
            if temp_stacks[i] is not goal_stacks[i]:  # if the compared stacks are not the same
                # check if both stacks have the same length
                if len(temp_stacks[i]) > len(goal_stacks[i]):
                    # pop the extra block
                    block_pickup = temp_stacks[i].pop()
                    # robot picks up extra block; function used depends on if block is on table or on stack
                    if temp_stacks[i].isEmpty():
                        arm.action_pickup(block_pickup)
                    else:
                        arm.action_unstack(block_pickup)
                    # check if the current blocks in stack are correct
                    incorrect_index = checkCurrStack(temp_stacks[i], goal_stacks[i])
                    if len(incorrect_index) > 0:
                        pass
                if len(temp_stacks[i]) < len(goal_stacks[i]):
                    incorrect_index = checkCurrStack(temp_stacks[i], goal_stacks[i])

                elif len(temp_stacks[i]) is len(goal_stacks[i]):
                    incorrect_index = checkCurrStack(temp_stacks[i], goal_stacks[i])


# check stack to see if the blocks are correct #
def checkCurrStack(currStack, goalStack):
    curr_size = len(currStack)

    incorrect_index = []  # list of blocks at index that do not match

    for i in range(curr_size):
        # compare value at index
        if curr_size[i].peekAt(i) is not goalStack[i].peekAt(i):
            incorrect_index.append(str(i))

    return incorrect_index

def blockMovement(block, currStacks, goalStacks):
    currPos = ""
    finalPos = ""
    # find current position of block
    # find final position of block
    # check if block is clear

    pass


# create an empty stack if there's a deadlock #
def addStack(tableStack):
    addStack = Stack()
    tableStack.append(addStack)
    return tableStack


# remove empty stack when not required #
# - to check if currTable stack is more than goal stack
def deleteStack(tableStack):
    tableStack[len(tableStack)-1].pop()


