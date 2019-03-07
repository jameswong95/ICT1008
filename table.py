from block_stack import *
from functions import *

def createTable(table):
    stack_list = table.split()  # split the strings
    numOfStack = len(stack_list)  # set the number of stacks required
    table_stacks = [Stack() for i in range(numOfStack)]  # create the number of stacks

    # add blocks onto stacks which are on the table
    for i in range(len(stack_list)):
        rstring = reverseString(stack_list[i])
        for char in rstring:
            table_stacks[i].push(char)
    return table_stacks


def alt(init_stacks, goal_stacks):
    # to hold each movement #
    stackMovement = {}  # to record the movements of the block

    # size of current stacks #
    init_size = len(init_stacks)
    goal_size = len(goal_stacks)

    # copy from initial stack to temp stack
    temp_stacks = [Stack() for i in range(init_size)]
    for i in range(init_size):
        temp_stacks[i] = init_stacks[i].copyTo()

    # if initial stack has lesser stacks than goal stacks, add until they have the same amount of stacks
    while len(temp_stacks) < len(goal_stacks):
        temp_stacks = addStack(temp_stacks)

    temp_size = len(temp_stacks)
    arm = armFunction()  # declare robot arm

    # add initial stack to block movement list
    addStackMovement(stackMovement, 'move ' + str(arm.action_counter), 'Initial Stack', arm.onHand, init_stacks)

    # START MOVING THINGS AROUND #
    for i in range(goal_size):

        position = 0  # start from bottom of stack
        temp_stack_counter = i

        temp_stack_size = temp_stacks[i].size()
        goal_block_size = goal_stacks[i].size()

        #while cmp(temp_stacks[i].toString(), goal_stacks[i].toString()) is not 0:
        while (temp_stacks[i].toString() > goal_stacks[i].toString()) - \
                (temp_stacks[i].toString() < goal_stacks[i].toString()) is not 0:
                if position > temp_stack_size-1:
                    temp_stack_counter += 1
                    # check block at the btm of goal stack & compare to btm of temp stack
                    goal_block_atPos = goal_stacks[i].peekAt(position)

                    # find where the goal block is currently & its status
                    goal_block_status = searchForValue(temp_stacks, goal_block_atPos)
                    # check the status of current block that is in wrong position

                    # move goal block to stack
                    if goal_block_status['clear']:
                        temp_stacks = moveClearGoalBlock(arm, temp_stacks, temp_block_status, goal_block_status,
                                                         goal_block_atPos, goal_block_status['stackIndex'], stackMovement)
                    elif goal_block_status['clear'] is False:
                        # go up to the next block
                        position += 1

                    position += 1

                else:
                    # check block at the btm of goal stack & compare to btm of temp stack
                    goal_block_atPos = goal_stacks[i].peekAt(position)
                    temp_block_atPos = temp_stacks[i].peekAt(position)

                    if temp_block_atPos is not goal_block_atPos:

                        # find where the goal block is currently & its status
                        goal_block_status = searchForValue(temp_stacks, goal_block_atPos)
                        # check the status of current block that is in wrong position
                        temp_block_status = searchForValue(temp_stacks, temp_block_atPos)

                        # remove the temp block if clear
                        if temp_block_status['clear']:
                            # move block to a stack that does not contain goal block
                            temp_stacks = moveClearBlock(arm, temp_stacks, temp_block_status, goal_block_status,
                                                         temp_block_atPos, i, stackMovement)
                        elif temp_block_status['clear'] is False:
                            # go up to the next block
                            position += 1
                        # move goal block to stack
                        if goal_block_status['clear']:
                            temp_stacks = moveClearGoalBlock(arm, temp_stacks, temp_block_status, goal_block_status,
                                                             goal_block_atPos, i, stackMovement)
                        elif goal_block_status['clear'] is False:
                            # go up to the next block
                            position += 1

                    position += 1

        if goal_size is i+1:
            while len(temp_stacks) > len(goal_stacks):
                deleteStack(temp_stacks)
            stackMovement['move ' + str(arm.action_counter)]['blockPosition'] = temp_stacks[i].toString()
            break
    return stackMovement


# search for value to find its position in stacks #
def searchForValue(table_stacks, value):
    block_info = {}
    arm = armFunction()

    # search each stack for value #
    for i in range(len(table_stacks)):
        # if value can be found in stack
        block_index = table_stacks[i].contains(value)
        if block_index is not -1:
            block_info['blockIndex'] = block_index
            block_info['stackIndex'] = i

            # get the status of the block #
            # check if block is on table
            if arm.ontable(value, table_stacks[i]):
                block_info['on'] = "table"
            else:
                block_info['on'] = "block"
            # check if block is clear
            if arm.clear(value, table_stacks[i]):
                block_info['clear'] = "True"
            else:
                block_info['clear'] = "False"

            return block_info


# reverse the string
def reverseString(s):
    str = ''
    for char in s:
        str = char + str  # appending chars in reverse order
    return str


# create an empty stack if there's a deadlock #
def addStack(tableStack):
    addStack = Stack()
    tableStack.append(addStack)
    return tableStack


# remove empty stack when not required #
# - to check if currTable stack is more than goal stack
def deleteStack(tableStack):
    tableStack.pop()


def stacksToString(tableStack):
    stackStr = ""
    stackSize = len(tableStack)
    for i in range(stackSize):
        if i < stackSize - 1:
            stackStr += tableStack[i].toString() + " "
        else:
            stackStr += tableStack[i].toString()
    return stackStr


def addStackMovement(stackMovement, move, action, heldBlock, tableStacks):
    stackMovement[move] = {}
    stackMovement[move]['action'] = action
    stackMovement[move]['heldBlock'] = heldBlock
    stackMovement[move]['blockPosition'] = stacksToString(tableStacks)

    return stackMovement


def moveClearBlock(arm, temp_stacks, temp_block_status, goal_block_status, temp_block_atPos, stackIndex, stackMovement):

    if temp_block_status['on'] is "table":

        # pick up block on table
        arm.action_pickup(temp_block_atPos, temp_stacks)
        action = "Pick up block " + temp_block_atPos + " from table"
        addStackMovement(stackMovement, 'move ' + str(arm.action_counter), action, arm.onHand, temp_stacks)
        nextStack = stackIndex + 1

        # putting block down
        if nextStack is not goal_block_status['stackIndex']:

            # putting block on table if next stack is empty
            if temp_stacks[nextStack].isEmpty():
                temp_stacks[nextStack] = arm.action_putdown(temp_block_atPos, temp_stacks[nextStack])
                action = "Put down block " + temp_block_atPos + " on table"
                addStackMovement(stackMovement, 'move ' + str(arm.action_counter), arm, action, arm.onHand, temp_stacks)
            else:
                nextStack += 1
                nextStack_topBlock = temp_stacks[nextStack].peek()
                temp_stacks = arm.action_stack(temp_block_atPos, temp_stacks, nextStack_topBlock)
                action = "Stack block " + temp_block_atPos + " on block" + nextStack_topBlock
                addStackMovement(stackMovement, 'move ' + str(arm.action_counter), action, arm.onHand, temp_stacks)

    elif temp_block_status['on'] is "block":

        # pick up block on that is on another block
        onBlock = temp_stacks[stackIndex].peekAt(temp_stacks[stackIndex].size() - 2)
        temp_stacks = arm.action_unstack(temp_block_atPos, temp_stacks, onBlock)
        action = "Unstack block " + temp_block_atPos + " from block " + onBlock
        addStackMovement(stackMovement, 'move ' + str(arm.action_counter), action, arm.onHand, temp_stacks)
        nextStack = stackIndex + 1

        # putting block down
        if nextStack is not goal_block_status['stackIndex']:
            if temp_stacks[nextStack].isEmpty():
                temp_stacks[nextStack] = arm.action_putdown(temp_block_atPos, temp_stacks[nextStack])
                action = "Put down block " + temp_block_atPos + " on table"
                addStackMovement(stackMovement, 'move ' + str(arm.action_counter), action, arm.onHand, temp_stacks)
        else:
            nextStack += 1
            nextStack_topBlock = temp_stacks[nextStack].peek()
            temp_stacks = arm.action_stack(temp_block_atPos, temp_stacks, nextStack_topBlock)
            action = "Stack block " + temp_block_atPos + " on block"
            addStackMovement(stackMovement, 'move ' + str(arm.action_counter), action, arm.onHand, temp_stacks)
    return temp_stacks


def moveClearGoalBlock(arm, temp_stacks, temp_block_status, goal_block_status, goal_block_atPos, stackIndex,
                       stackMovement):

    if goal_block_status['on'] is "table":

        # pick up block on table
        temp_stacks = arm.action_pickup(goal_block_atPos, temp_stacks)
        action = "Pick up block " + goal_block_atPos + " from table"
        addStackMovement(stackMovement, 'move ' + str(arm.action_counter), action, arm.onHand, temp_stacks)

        # putting block down
        if temp_stacks[temp_block_status['stackIndex']].isEmpty():
            temp_stacks[temp_block_status['stackIndex']] = \
                arm.action_putdown(goal_block_atPos, temp_stacks[temp_block_status['stackIndex']])
            action = "Put down block " + goal_block_atPos + " on table"
            addStackMovement(stackMovement, 'move ' + str(arm.action_counter), action, arm.onHand, temp_stacks)
        else:
            stackOn_block = temp_stacks[temp_block_status['stackIndex']].peek()
            temp_stacks = arm.action_stack(goal_block_atPos, temp_stacks, stackOn_block)
            action = "Stack block " + goal_block_atPos + " on block " + stackOn_block
            addStackMovement(stackMovement, 'move ' + str(arm.action_counter), action, arm.onHand, temp_stacks)

    elif goal_block_status['on'] is "block":

        # pick up block on that is on another block
        onBlock = temp_stacks[stackIndex].peekAt(temp_stacks[stackIndex].size() - 2)
        temp_stacks = arm.action_unstack(goal_block_atPos, temp_stacks, onBlock)
        action = "Unstack block " + goal_block_atPos + " from block " + onBlock
        addStackMovement(stackMovement, 'move ' + str(arm.action_counter), action, arm.onHand, temp_stacks)
        # putting block down
        if temp_stacks[temp_block_status['stackIndex']].isEmpty():
                temp_stacks[temp_block_status['stackIndex']] = \
                    arm.action_putdown(goal_block_atPos, temp_stacks[temp_block_status['stackIndex']])
                action = "Put down block " + goal_block_atPos + " on table"
                addStackMovement(stackMovement, 'move ' + str(arm.action_counter), action, arm.onHand, temp_stacks)
        else:
            stackOn_block = temp_stacks[temp_block_status['stackIndex']].peek()
            temp_stacks = arm.action_stack(goal_block_atPos, temp_stacks, stackOn_block)
            action = "Stack block " + goal_block_atPos + " on block " + stackOn_block
            addStackMovement(stackMovement, 'move ' + str(arm.action_counter), action, arm.onHand, temp_stacks)
    return temp_stacks
