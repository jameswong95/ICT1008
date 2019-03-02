# from functions import *
# from block_stack import *
start_state = "1 23"  #Start State
final_state = "132" #Goal State


combine_tstack = []
stack = []
arm = []
steps =[]
temp_start_stack = []
final_state = final_state.split(" ")
start_state = start_state.split(" ")

# loop each tower in final state
for i in range(len(final_state)):
    # make this easier to refer
    tower = final_state[i]
    tower_height = len(tower)
    # when tower has only 1 block
    # this if part can be handled outside the loop
    if tower_height == 1:
        combine_tstack.append({
          'type': "action",
          'name': "ontable",
          'params': tower[0]
        })
        #temp_stack = {}
        #temp_stack.update([('type', 'action'), ('name', 'clear'), ('params', tower[0])])
        combine_tstack.append({
          'type': "action",
          'name': "clear",
          'params': tower[0]
        })
    else:
        # handle bottom block
        temp_stack = {
          'type': "predicate",
          'name': "ontable",
          'params': tower[0]
        }
        # clear = "clear(" + tower[j] + ")"
        combine_tstack.append(temp_stack)
        # on = "on("+tower[j]+","+tower[j+1]+")"
        
        # handle top block
        temp1_stack = {
          'type': "predicate",
          'name': "clear",
          'params': tower[-1]
        }
        combine_tstack.append(temp1_stack)

        # loop each block in tower, excluding the first block
        for j in range(1, len(tower)):
          temp_stack = {
            'type': "predicate",
            'name': "on",
            'params': tower[j] + "," + tower[j-1]
          }
          # on = "on(" + tower[j-1] + "," + tower[j] + ")"
          # ontable = ontable = "ontable("+tower[j]+")"
          combine_tstack.append(temp_stack)
stack.append(combine_tstack)
for i in combine_tstack:
    stack.append(i)

temp_stack = {}
temp1_stack = {}

# loop each tower in start state
for i in range(len(start_state)):
    # make this easier to refer
    tower = start_state[i]
    tower_height = len(tower)
    # when tower has only 1 block
    # this if part can be handled outside the loop
    if tower_height == 1:
        temp_start_stack.append({
          'type': "action",
          'name': "ontable",
          'params': tower[0]
        })
        #temp_stack = {}
        #temp_stack.update([('type', 'action'), ('name', 'clear'), ('params', tower[0])])
        temp_start_stack.append({
          'type': "action",
          'name': "clear",
          'params': tower[0]
        })
    else:
        # handle bottom block
        temp_stack = {
          'type': "predicate",
          'name': "ontable",
          'params': tower[0]
        }
        # clear = "clear(" + tower[j] + ")"
        temp_start_stack.append(temp_stack)
        # on = "on("+tower[j]+","+tower[j+1]+")"
        
        # handle top block
        temp1_stack = {
          'type': "predicate",
          'name': "clear",
          'params': tower[-1]
        }
        temp_start_stack.append(temp1_stack)

        # loop each block in tower, excluding the first block
        for j in range(1, len(tower)):
          temp_stack = {
            'type': "predicate",
            'name': "on",
            'params': tower[j] + "," + tower[j-1]
          }
          # on = "on(" + tower[j-1] + "," + tower[j] + ")"
          # ontable = ontable = "ontable("+tower[j]+")"
          temp_start_stack.append(temp_stack)


temp_stack = {}
temp1_stack = {}
counter = 0
# print temp_start_stack[3]['name']
# if stack[-1]['name'] == 'ontable':
#     print stack[-1]['params']


# print stack[-1]

# print stack[-1]['type']

combine_tstack = []
counter_unstack = 0
counter_stack = 0
counter_pickup  =0
counter_putdown  =0
counter_holding  =0
if start_state == final_state:
    print ("No Change")

while len(stack) > 0:
    if stack[-1] not in temp_start_stack:
        # print stack[-1]
        # print temp_start_stack[-1]
        for i in range(len(temp_start_stack)):
            if temp_start_stack[i]['name'] == 'on' and stack[-1]['name'] == 'ontable':
                ele_value = temp_start_stack[i]['params']
                if ele_value[0] == stack[-1]['params']:
                    temp1_stack.update(
                        [('type', 'action'), ('name', 'unstack'), ('params', ele_value[0] + ',' + ele_value[2])])
                    stack.append(temp1_stack)
    else:
        if stack[-1]['name'] == 'ontable':
            if stack[-1] in temp_start_stack:
                stack.pop()
    if type(stack[-1]) is not list:
        if stack[-1]['type'] == 'action':
            temp_stack = {}
            temp1_stack = {}
            if stack[-1]['name']=='unstack' and counter_unstack == 0:
                # print "hey"
                ele_value = stack[-1]['params']
                temp_stack = {}
                temp_stack.update([('type', 'predicate'), ('name', 'armempty'), ('params',"")])
                combine_tstack.append(temp_stack)
                temp1_stack = {}
                temp1_stack.update([('type', 'predicate'), ('name', 'on'), ('params',ele_value[0]+","+ele_value[2])])
                combine_tstack.append(temp1_stack)
                temp2_stack = {}
                temp2_stack.update([('type', 'predicate'), ('name', 'clear'), ('params', ele_value[0])])
                combine_tstack.append(temp2_stack)
                stack.append(combine_tstack)
                for i in combine_tstack:
                    stack.append(i)
                temp_stack = {}
                temp1_stack = {}
            elif stack[-1]['name'] == 'unstack' and counter_unstack == 1:
                temp1_stack = {}
                temp2_stack = {}
                temp_stack = {}
                ele_value = stack[-1]['params']
                for i in temp_start_stack:
                    if i['params'] == ele_value:
                        temp_start_stack.remove(i)
                        temp2_stack = {}
                        temp2_stack.update([('type', 'predicate'), ('name', 'clear'), ('params', ele_value[2])])
                        temp_stack = {}
                        # print ele_value[2]
                        temp_stack.update([('type', 'predicate'), ('name', 'ontable'), ('params', ele_value[0])])
                        # temp1_stack.update([('type', 'predicate'), ('name', 'ontable'), ('params', ele_value[0])])
                        temp_start_stack.append(temp_stack)
                        temp_start_stack.append(temp2_stack)
                        # temp_start_stack.append(temp1_stack)
                        arm.append(ele_value[0])
                # arm.append(ele_value[2])
                # print ele_value
                steps.append(stack[-1])
                stack.pop()
                counter_unstack = 0
            elif stack[-1]['name'] == 'stack' and counter_stack == 0:
                combine_tstack =[]
                # print "here"
                ele_value = stack[-1]['params']
                temp_stack = {}
                temp_stack.update([('type', 'predicate'), ('name', 'clear'), ('params', ele_value[2])])
                combine_tstack.append(temp_stack)
                temp1_stack = {}
                temp1_stack.update([('type', 'predicate'), ('name', 'holding'), ('params', ele_value[0])])
                combine_tstack.append(temp1_stack)
                stack.append(combine_tstack)
                for i in combine_tstack:
                    stack.append(i)
                counter_stack = 1
            elif stack[-1]['name'] == 'stack' and counter_stack == 1:
                ele_value = stack[-1]['params']
                steps.append(stack[-1])

                # for i in range(len(temp_start_stack)):
                for i in range(len(temp_start_stack)):
                    if temp_start_stack[i]['name'] == 'ontable' and temp_start_stack[i]['params'] == ele_value[0]:
                        temp_start_stack.remove(temp_start_stack[i])
                        temp_stack = {}
                        temp_stack.update([('type', 'predicate'), ('name', 'on'), ('params', ele_value[0]+","+ele_value[2])])
                        temp_start_stack.append(temp_stack)
                    if temp_start_stack[i]['name'] =='clear' and temp_start_stack[i]['params'] == ele_value[2]:
                        ele_index = i
                # print ele_index
                temp_start_stack.remove(temp_start_stack[ele_index])
                # print "work"
                stack.pop()
                # print stack
            elif stack[-1]['name'] == 'pickup' and counter_pickup == 0 :
                combine_tstack = []
                # print "here"
                ele_value = stack[-1]['params']
                temp_stack = {}
                temp_stack.update([('type', 'predicate'), ('name', 'armempty'), ('params', "")])
                combine_tstack.append(temp_stack)
                temp1_stack = {}
                temp1_stack.update([('type', 'predicate'), ('name', 'ontable'), ('params', ele_value[0])])
                combine_tstack.append(temp1_stack)
                temp2_stack = {}
                temp2_stack.update([('type', 'predicate'), ('name', 'clear'), ('params', ele_value[0])])
                # print
                combine_tstack.append(temp2_stack)
                stack.append(combine_tstack)
                counter_pickup = 1
                for i in combine_tstack:
                    stack.append(i)
                # print  "did it", stack
            elif stack[-1]['name'] == 'pickup' and counter_pickup == 1:
                ele_value = stack[-1]['params']
                # arm.append(ele_value[0])
                # temp_stack.update([('type', 'predicate'), ('name', 'ontable'), ('params', ele_value[0])])
                # temp_start_stack.append(temp_stack)
                # print counter_pickup
                steps.append(stack[-1])
                stack.pop()
                counter_pickup = 0
                if stack[-1]['name'] == 'holding':
                    stack.pop()
                # print stack
                counter_pickup = 0
            elif stack[-1]['name'] == 'putdown' and counter_putdown ==0 :
                ele_value = stack[-1]['params']
                temp_stack = {}
                temp1_stack = {}
                temp_stack.update([('type', 'predicate'), ('name', 'holding'), ('params', ele_value[0])])
                combine_tstack.append(temp_stack)
                stack.append(combine_tstack)
            elif stack[-1]['name'] == 'putdown' and counter_putdown == 1:
                ele_value = stack[-1]['params']
                temp1_stack = {}
                temp2_stack = {}
                # for i in temp_start_stack:
                #     if i['params'] == ele_value:
                        # temp_start_stack.remove(i)
                        # temp2_stack = {}
                        # temp2_stack.update([('type', 'predicate'), ('name', 'clear'), ('params', ele_value[0])])
                        # temp_start_stack.append(temp2_stack)
                # print ele_value
                # temp_stack.update([('type', 'predicate'), ('name', 'ontable'), ('params', ele_value[0])])
                # temp_start_stack.append(temp_stack)
                steps.append(stack[-1])
                arm = []
                stack.remove(stack[-1])
                # print "hihi" ,stack
                # print stack[-1]
                counter_putdown= 0


        # print stack
        check_list = []


        if len(arm) > 0 :
            temp1_stack = {}
            temp1_stack.update([('type', 'action'), ('name', 'putdown'), ('params',arm[0])])
            stack.append(temp1_stack)
        if stack[-1]['name'] == 'on':
            if stack[-1] in temp_start_stack:
                stack.pop()

            else:
                ele_value = stack[-1]['params']
                temp1_stack.update([('type', 'action'), ('name', 'stack'), ('params', ele_value[0] + ',' + ele_value[2])])
                stack.append(temp1_stack)

        # print counter_holding
        # print counter, stack[-1]
        if type(stack[-1]) is not list:
            if stack[-1]['name'] == 'holding' and counter_holding == 0:
                # print "hi"
                temp_stack = {}
                temp1_stack = {}
                ele_value = stack[-1]['params']
                temp_stack.update([('type', 'action'), ('name', 'armempty'), ('params', "")])
                stack.append(temp_stack)
                temp1_stack.update([('type', 'action'), ('name', 'pickup'), ('params', ele_value[0])])
                stack.append(temp1_stack)
                counter_holding = 1

            if stack[-1]['name'] == 'holding' and counter_holding == 1:
                # print "new"
                stack.pop()
                counter_holding = 0
            # if stack[-1]['name'] == 'pickup':
            #     ele_value = stack[-1]['params']
            #     temp_stack = {}
            #     temp1_stack = {}
            #     temp2_stack = {}
            #     temp2_stack.update([('type', 'predicate'), ('name', 'armemepty'), ('params', "")])
            #     stack.append(temp2_stack)
            #     temp_stack.update([('type', 'predicate'), ('name', 'ontable'), ('params', ele_value[0])])
            #     stack.append(temp_stack)
            #     temp1_stack.update([('type', 'predicate'), ('name', 'clear'), ('params', ele_value[0])])
            #     stack.append(temp1_stack)
            if stack[-1]['name'] == 'clear':
                for i in temp_start_stack:
                    for j in stack:
                        if type(j) is dict:
                            if i == j:
                                if j['params'] == stack[-1]['params']:
                                    check_list.append(j)
                                    stack.remove(j)
                                    # print  j
                                # if j['name'] == 'clear':
                                    # print j
                            if j['name'] == 'armempty':
                                if j['params'] == '':
                                    check_list.append(j)
                                    stack.remove(j)
            # print "after Clear" , stack
    # print stack[-1]
        if type(stack[-1]) is not list:
            if stack[-1]['name'] == "armempty" and stack[-1]['params'] == "":
                stack.pop()
    counter_putdown =1
    counter_unstack = 1
    temp1_stack = {}
    temp2_stack = {}
    temp_stack = {}
    # print stack
    # print counter
    counter += 1
    # print counter
# print stack[-1][oo'name']
# if not arm:
#     print True
    if type(stack[-1]) is list:
        # list_counter = 0
        # list_len = len(check_list)-1
        # # print list_len
        # for i in stack[-1]:
        #     for j in check_list:
        #         if i == j:
        #             check_list.remove(j)
        #             list_counter += 1
        #     if list_counter == list_len:
        #         stack.pop()
        #         check_list = []
        stack.pop()
print "Temp_start_Stack: ", temp_start_stack
print "Temp Stack: ", temp_stack
print "Stack: ",stack
# print combine_tstack
print "Arm: ", arm
print "Steps: ",steps
print len(steps)