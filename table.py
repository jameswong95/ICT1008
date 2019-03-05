from block_stack import *
from queue import *


def createTable(table, numStackAtGoal):
    numOfStack = numStackAtGoal  # set the number of stacks required
    stack_list = table.split()  # split the strings
    table_stacks = [Stack() for i in range(numOfStack)]  # create the number of stacks

    # add blocks onto stacks which are on the table
    for string in stack_list:
        for char in string:
            table_stacks[stack_list.index(string)].push(char)

    return table_stacks


# create a stack if there's a dead lock
def addStack(table):
    pass


def classicalPlanning(init_table_stacks, goal_table_stacks):

    moveStack = Stack()  # to record all movements made
    stackPosition = []  # to record the movements of the block

    size = len(goal_table_stacks)
    temp_stacks = [Stack() for i in range(size)]  # to store the current stack

    temp_stacks = init_table_stacks

        # if not in correct position, how to get there
        # check if can move
        # if cannot, check for other moves



