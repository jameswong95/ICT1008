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

    # size of current stacks #
    init_size = len(init_stacks)
    goal_size = len(goal_stacks)

    # copy from initial stack to temp stack
    temp_stack = [Stack() for i in range(init_size)]
    for i in range(init_size):
        temp_stack[i] = init_stacks[i].copyTo()

    temp_size = len(temp_stack)

    arm = armFunction()  # declare robot arm

    # comparing individual stacks #

    # compare number of stacks
    if init_size > goal_size:
        pass
    elif init_size < goal_size:
        pass
    elif init_size is goal_size:
        # check if stack have the same length
        for i in range (temp_size):
            if temp_stack[i] is not goal_stacks[i]:  # if the compared stacks are not the same
                # check if both stacks have the same length
                if len(temp_stack[i]) > len(goal_stacks[i]):
                    # are the current blocks correct?
                    block_pick = temp_stack[i].peek()
                    arm.action_pickup(block_pick)
                if len(temp_stack[i]) < len(goal_stacks[i]):
                # are the current blocks correct?
                    pass
                elif len(temp_stack[i]) is len(goal_stacks[i]):
                    # are the current blocks correct?
                    pass


def checkCurrStack(currStack, goalStack):
    curr_size = len(currStack)
    goal_size = len(goalStack)
    if len(curr_size) > len(goalStack):
        pass
    elif len(curr_size) < len(goalStack):
        pass
    elif len(curr_size) is len(goalStack):
        for i in range():
            pass

# create an empty stack if there's a deadlock
def addStack(tableStack):
    newSize = len(tableStack) + 1
    addStack = Stack()
    tableStack.append(addStack)
    return tableStack

# remove empty stack when not required
def deleteStack(tableStack, goalStack):
    pass


