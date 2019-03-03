
final_state = '123'
start_state = '3 2 1'
final_state = final_state.split(" ")
start_state = start_state.split(" ")


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
        # ontable = "ontable("+final_state[i]+")"
        # clear = "clear("+final_state[i]+ ")"
        temp_stack.update([ ('type', 'action') , ('name', 'ontable') , ('params', final_state[i])] )
        combine_tstack.append(temp_stack)
        temp_stack = {}
        temp_stack.update([('type', 'action'), ('name', 'clear'), ('params', final_state[i])])
        combine_tstack.append(temp_stack)
    else:
        for j in range(len(final_state[i])):
            if j == 0:
                temp_stack = {}
                # clear = "clear(" + final_state[i][j] + ")"
                temp_stack.update([('type', 'predicate'), ('name', 'on'),
                                    ('params', final_state[i][j] + "," + final_state[i][j + 1])])
                combine_tstack.append(temp_stack)
                # on = "on("+final_state[i][j]+","+final_state[i][j+1]+")"
                temp1_stack = {}
                temp1_stack.update([('type', 'predicate'), ('name', 'clear'), ('params', final_state[i][j])])
                combine_tstack.append(temp1_stack)
                # temp_stack.append(on)
                # temp_stack.append(clear)
            elif j != len(final_state[i])-1:
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

# temp_stack = {}
# temp1_stack = {}
temp_start_stack = []
counter_test = 1
# loop each tower in start state
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
                elif j == len(start_state[i])-1:
                    temp1_stack = {}
                    temp1_stack.update([('type', 'predicate'), ('name', 'ontable'), ('params', start_state[i][j])])
                    temp_start_stack.append(temp1_stack)
                else:
                    temp_stack = {}
                    temp_stack.update([('type', 'predicate'), ('name', 'on'), ('params', start_state[i][j] + "," + start_state[i][j+1])])
                    temp_start_stack.append(temp_stack)
    counter_test = 0
counter = 0
counter_putdown  =0
counter_holding  =0
if start_state == final_state:
    print ("No Change")
while len(stack) >0:
    list_counter = 0

    combine_tstack = []

    if type(stack[-1]) is list:
        list_counter = 0
        ele_notfound = ""
        for i in temp_start_stack:
            for j in stack[-1]:
                if i == j:
                    list_counter += 1

        if len(stack)>1:
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
            temp_stack  = {}
            temp1_stack = {}
            temp2_stack = {}
            temp3_stack = {}
            if stack[-1]['name'] == 'on':
                current_stack = stack[-1]
                new_value = current_stack['params']
                temp1_stack = {}
                temp1_stack.update([('type', 'action'), ('name', 'stack'), ('params', new_value[0]+","+new_value[2])])
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
                    for i in temp_start_stack:
                        # print i['params'][0]
                        if i['name'] == 'on' and i['params'][0] == new_value:
                            unstackfrom =  i['params'][2]
                        if i['name'] == 'on' and i['params'][2] == new_value:
                            unstackfrom =  i['params'][0]
                    # temp1_stack.update([('type', 'action'), ('name', 'putdown'), ('params', new_value)])
                    temp_stack.update([('type', 'predicate'), ('name', 'armempty'), ('params', "")])
                    # temp3_stack.update([('type', 'predicate'), ('name', 'on'), ('params', new_value + "," + unstackfrom)])
                    # temp2_stack.update([('type', 'predicate'), ('name', 'clear'), ('params', new_value)])
                    # combine_tstack.append(temp1_stack)
                    combine_tstack.append(temp_stack)
                    # combine_tstack.append(temp3_stack)
                    # combine_tstack.append(temp2_stack)
                    temp1_stack.update([('type', 'action'), ('name', 'unstack'), ('params', new_value + "," + unstackfrom)])

                    temp_stack = {}
                    temp3_stack = {}


                    # print stack
                    for i in combine_tstack:
                        stack.append(i)
                    stack.append(temp1_stack)
                    # temp1_stack = {}
                    # temp1_stack.update([('type', 'action'), ('name', 'pickup'), ('params', new_value)])
                    # stack.append(temp1_stack)
                    # print stack
            elif stack[-1]['name'] == 'clear':
                current_stack = stack[-1]
                new_value = current_stack['params']
                temp_stack = {}
                for i in temp_start_stack:
                    if i['name'] == 'on':
                        if i['params'][2] == new_value:
                            new_value = i['params']
                            temp_stack = {}
                            temp_stack.update([('type', 'action'), ('name', 'unstack'),('params', new_value)])



                stack.append(temp_stack)


            elif stack[-1]['name'] == 'holding':
                current_stack = stack[-1]
                new_value = current_stack['params']
                if arm[0] == new_value:
                    stack.pop()
                # print "try ", stack

            elif stack[-1]['name'] == 'armempty':
                current_stack = stack[-1]
                temp_stack ={}
                new_value = current_stack['params']
                temp1_stack = {}
                for i in arm:
                    arm_value = i
                if len(arm) == 0:
                    stack.pop()
                else:
                    # print "arm"
                    combine_tstack = []

                    temp1_stack.update([('type', 'action'), ('name', 'putdown'), ('params',  arm_value)])
                    stack.append(temp1_stack)
                    temp_stack.update([('type', 'predicate'), ('name', 'holding'), ('params', arm_value)])
                    combine_tstack.append(temp_stack)
                    stack.append(combine_tstack)
                    for i in combine_tstack:
                        stack.append(i)

    else:
        current_stack = stack[-1]
        new_name  = current_stack['name']
        new_value = current_stack['params']
        if new_name == 'unstack':
            steps.append(current_stack)
            new_value2 = new_value[2]
            temp_stack = {}
            temp_stack.update([('type', 'predicate'), ('name', 'clear'), ('params', new_value[2])])
            temp_start_stack.append(temp_stack)
            for i in temp_start_stack:
                if i['name'] == 'on' and i['params'] == str(new_value[0])+","+str(new_value[2]):
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
            print new_value
            # print new_value
            for i in temp_start_stack:
                if i['name'] == 'clear' and i['params'] == new_value:
                    # print "in here"
                    ele_found = i
                    temp_start_stack.remove(i)
            for i in temp_start_stack:
                # print i
                # print i['params']
                if i['name'] == 'ontable' and i['params'] == new_value:
                    # print "in here"
                    ele_found = i
                    temp_start_stack.remove(i)
            for i in temp_start_stack:
                # print i
                # print i['params']
                if i['name'] == 'on' and i['params'][0] == new_value:
                    # print "in here"
                    ele_found = i
                    temp_start_stack.remove(i)
            print ele_found
            # temp_stack.update([('type', 'predicate'), ('name', 'clear'), ('params', new_value)])
            # temp_start_stack.append(temp_stack)
            stack.pop()
            steps.append(current_stack)
        elif new_name == 'stack':
            for i in temp_start_stack:
                if i['name'] == 'clear' and i['params'] == new_value[2]:
                    ele_found = i
                    temp_start_stack.remove(i)
            temp_stack.update([('type', 'predicate'), ('name', 'clear'), ('params', new_value[0])])
            temp1_stack.update([('type', 'predicate'), ('name', 'on'), ('params', new_value[0] + "," + new_value[2])])
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
                temp1_stack.update([('type', 'predicate'), ('name', 'on'), ('params', new_value[0] + "," + new_value[2])])
                temp_start_stack.append(temp_stack)
                temp_start_stack.append(temp1_stack)
            stack.pop()
            steps.append(current_stack)
            arm.pop()
    #         arm
    # # do
    # action
    # then
    # pop

    counter += 1

# print unstackfrom
print temp_start_stack
print "Stack",stack
print combine_tstack
print "Steps: ",steps
print arm