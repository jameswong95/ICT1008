

class armFunction:

    action_counter = 0
    armHolding = False
    onHand = ""

    # ROBOT ARM FUNCTIONS
    def action_unstack(self, a, tableStack, b):
        print ("Pick up clear block " + a + " from " + b)

        # CONSTRAINTS: a != b, a || b != table
        # check constraints
        if a is not b:
            if armFunction.ontable(a) or armFunction.ontable(b):
                return "Unable to unstack as either " + a + "or " + b + "is on the table"
        else:
            return a + " is the same as " + b

        # UNSTACK START
        # check if a is on b
        if armFunction.on(a, b):
            # check if block a is clear
            if armFunction.clear(a):
                # check if arm is empty
                if armFunction.Armempty():
                    # remove a from stack
                    for stack in tableStack:
                        if stack.peek() is a:
                            stack.pop()
                            armFunction.armHolding = True
                            armFunction.onHand = a
                            armFunction.action_counter += 1
                            break
        return tableStack

    def action_stack(self, a, tableStack, b):
        print ("Place " + a + " using the arm onto clear block " + b)

        # CONSTRAINTS: a != b, a || b != table
        # check constraints
        if a is not b:
            if armFunction.ontable(a) or armFunction.ontable(b):
                return "Unable to unstack as either " + a + "or " + b + "is on the table"
        else:
            return a + " is the same as " + b

        # STACK START
        # check if block b is clear
        if armFunction.clear(b, tableStack):
            # check if block a is on hand
            if armFunction.holding is True and armFunction.onHand is a:
                # push block a into stack if b is the top of the stack
                for stack in tableStack:
                    if stack.peek() is b:
                        stack.push(a)
                        armFunction.armHolding = False
                        armFunction.onHand = ""
                        armFunction.action_counter += 1
                        break
        return tableStack

    def action_pickup(self, a, tableStack):
        print ("Lift clear block " + a + " with the empty arm")
        # CONSTRAINTS: a != table

        # PICKUP START
        # check if a is onTable
        if armFunction.ontable(a):
            # check if a is clear
            if armFunction.clear(a):
                # check if arm is empty
                if armFunction.armHolding is False:
                    for stack in tableStack:
                        if stack.peek() is a:
                            stack.pop()
                            armFunction.armHolding = True
                            armFunction.onHand = a
                            armFunction.action_counter += 1
                            break

        return tableStack

    def action_putdown(self, a, tableStack):
        print ("Place the held block " + a + " onto a free space on the table")
        # CONSTRAINTS: a != table
        # Check for empty table
        for stack in tableStack:
            if len(stack) is 0:
                pass

        # PUT DOWN START
        if armFunction.onHand is a and armFunction.armHolding is True:
            for stack in tableStack:
                if len(stack) is 0:
                    stack.push(a)
                    armFunction.armHolding = False
                    armFunction.onHand = ""
                    armFunction.action_counter += 1
                    break
        return tableStack

    # BLOCK STATUS
    def on(self, a, b, tableStack):
        print("Block " + a + " is on Block " + b)
        # if the stack is clear check if the item below block a is b
        if armFunction.clear(a, tableStack):
            for stack in tableStack:
                if stack.peek() is a:
                    if stack.peekAt(len(stack)-2) is b:
                        return True
        return False

    def ontable(self, a, tableStack):
        print ("Block " + a + " is on the table")
        for stack in tableStack:
            if stack.peekAt(0) is a:
                return True
        return False

    def clear(self, a, tableStack):
        print ("Block " + a + " is clear")
        # check each stack and ensure that a is at the top of the stack
        for stack in tableStack:
            if stack.peek() is a:
                    return True
        return False

    # ROBOT ARM STATUS
    def holding(self, a):
        print("Arm is holding " + a)
        armFunction.holding = True
        armFunction.onHand = a
        return armFunction.holding

    def Armempty(self):
        print("Arm is Empty")
        if armFunction.armHolding is False:
            return True
        return False
