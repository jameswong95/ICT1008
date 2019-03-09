

class armFunction:

    action_counter = 0
    armHolding = False
    onHand = "No block being held"

    # ROBOT ARM FUNCTIONS
    def action_unstack(self, a, tableStack, b):
        # CONSTRAINTS: a != b, a || b != table
        # check constraints
        if a is not b:
            # UNSTACK START
            # check if a is on b
            if self.on(a, b, tableStack):
                # check if block a is clear
                for i in range(len(tableStack)):
                    if self.clear(a, tableStack[i]):
                        # check if arm is empty
                        if self.armempty():
                            # remove a from stack
                            if tableStack[i].peek() is a:
                                tableStack[i].pop()
                                self.holding(a)
                                self.action_counter += 1
                            break
                    # break
            return tableStack
        else:
            return a + " is the same as " + b

    def action_stack(self, a, tableStack, b):
        # CONSTRAINTS: a != b, a || b != table
        # check constraints
        if a is not b:
            # STACK START
            # check if block b is clear
            for i in range(len(tableStack)):
                if tableStack[i].contains(b) is not -1:
                    if self.clear(b, tableStack[i]):
                        # check if block a is on hand
                        if self.armempty() is False and self.onHand is a:
                            # push block a into stack if b is the top of the stack
                            tableStack[i].push(a)
                            self.holding("")
                            self.action_counter += 1
                            break

        else:
            return a + " is the same as " + b

        return tableStack

    def action_pickup(self, a, tableStack):
        # CONSTRAINTS: a != table

        # PICKUP START
        # check if a is onTable
        for i in range(len(tableStack)):
            if tableStack[i].contains(a) is not -1:
                if self.ontable(a, tableStack[i]):
                    # check if a is clear
                    if self.clear(a, tableStack[i]):
                        # check if arm is empty
                        if self.armempty():
                            tableStack[i].pop()
                            self.holding(a)
                            self.action_counter += 1
                        break
        return tableStack

    def action_putdown(self, a, stack):
        # CONSTRAINTS: a != table
        if self.onHand is a and self.armempty() is False:
            stack.push(a)
            self.holding("")
            self.action_counter += 1

        return stack

        # Check for empty table
        # for stack in tableStack:
        #    if len(stack) is 0:
        #        pass

        # PUT DOWN START
        # if armFunction.onHand is a and armFunction.armempty() is False:
        #   for stack in tableStack:
        #       if len(stack) is 0:
        #           stack.push(a)
        #           armFunction.holding("")
        #           armFunction.action_counter += 1
        #           break
        # return tableStack

    # BLOCK STATUS
    def on(self, a, b, tableStack):
        # if the stack is clear check if the item below block a is b
        for stack in tableStack:
            aIndex = stack.contains(a)
            if aIndex is not -1:
                if stack.peekAt(aIndex-1) is b:
                    return True
        return False

    def ontable(self, a, stack):
        if stack.peekAt(0) is a:
            return True
        return False

    def clear(self, a, stack):
        # check each stack and ensure that a is at the top of the stack
        # for data in stack:
        if stack.peek() is a:
            return True
        return False

    # ROBOT ARM STATUS
    def holding(self, a):
        if a is not "":
            self.armHolding = True
            self.onHand = a
        else:
            self.armHolding = False
            self.onHand = "No block being held"
        return self.armHolding

    def armempty(self):
        if self.armHolding is False:
            return True
        return False
