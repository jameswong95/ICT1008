# from functions import *
# from block_stack import *
#
#
#
# start_state = "B AC"  #Start State
# final_state = "CBA" #Goal State
# KB = []
# goal_state = []
# table = []
# plan = []
# KB = []
# initial_state = start_state.split()
# goal_state_ = final_state.split()
# print "Initial State:"
# for i in range(len(initial_state)):
#     if len(initial_state[i]) == 1:
#         ontable(initial_state[i], table)
#         KB.append("ontable_"+initial_state[i])
#         # print clear(initial_state[i])
#         KB.append("clear_"+initial_state[i])
#         print
#     else:
#         for j in range(len(initial_state[i])):
#             if j == 0:
#                 ontable(initial_state[i][j], table)
#                 KB.append("ontable_"+initial_state[i][j])
#                 table.append(initial_state[i][j])
#             if j == len(initial_state[i])-1:
#                 # print clear(initial_state[i][j])
#                 KB.append("clear_"+initial_state[i][j])
#                 print
#             else:
#                 # print on(initial_state[i][j + 1], initial_state[i][j])
#                 KB.append("on_"+initial_state[i][j+1]+initial_state[i][j])
#
#
#
# print "Goal State"
# msg = ""
# for i in range(len(goal_state_)):
#     if len(goal_state_[i]) == 1:
#         ontable(goal_state_[i], table)
#         # print clear(goal_state_[i])
#         table.append(goal_state_[i])
#         print
#     else:
#         for j in range(len(goal_state_[i])):
#             if j == 0:
#                 ontable(goal_state_[i][j], table)
#                 # table.append(goal_state_[i][j])
#                 goal_state.append("ontable_" + goal_state_[i][j])
#                 msg += "ontable_"+goal_state_[i][j]
#                 # goal_state.append(goal_state_[i][j]+goal_state_[i][j+1])
#             if j == len(goal_state_[i]) - 1:
#                 # print clear(goal_state_[i][j])
#                 print
#             else:
#                 print on(goal_state_[i][j + 1], goal_state_[i][j])
#                 goal_state.append("on_"+goal_state_[i][j]+goal_state_[i][j+1])
#                 msg += " on_"+goal_state_[i][j]+goal_state_[i][j+1]
# goal_state.insert(0,msg)
# counter1 = 0
# counter = 0
# KB.sort(reverse=True)
# while len(goal_state)>0:
#     # for i in KB:
#     #     if i not in goal_state:
#     # print len(goal_state)
#     if "on_" in goal_state[-1] and len(goal_state) > 2:
#         # print len(goal_state)
#         last_ele = goal_state[-1].replace("on_", "")
#         Armempty()
#         action_unstack(last_ele[1], table, last_ele[0])
#         print
#         goal_state. append("movefromtable_" + last_ele[1] + last_ele[0])
#         goal_state.append("ontable_" + last_ele[1] + " clear_" + last_ele[1] + " clear_" + last_ele[0])
#         goal_state.append("clear_" + last_ele[1])
#         goal_state.append("clear_" + last_ele[0])
#         goal_state.append("ontable_" + last_ele[1])
#     elif "on_" in goal_state[-1] and len(goal_state) == 2:
#         last_ele = goal_state[-1].replace("on_", "")
#         goal_state.append("movefromtable_" + last_ele[1] + last_ele[0])
#     elif len(goal_state) == 1:
#         last_state = ""
#         temp_goal_state = goal_state
#         for i in temp_goal_state:
#             last_state = i.split(" ")
#             # goal_state.append(last_state)
#         # print "I NEED HELP", KB
#         change_last_state = last_state[-1].replace("on_","")
#         # print "I NEED HELP", change_last_state[0]
#         #
#         # print "clear_"+change_last_state[0]
#         KB.remove("clear_"+change_last_state[0])
#         KB.remove("clear_" + change_last_state[1])
#         KB.remove("ontable_"+change_last_state[0])
#         KB.remove("ontable_" + change_last_state[1])
#         plan.remove("movefromtable_"+change_last_state[1]+change_last_state[0])
#         plan.append("movefromtable_" + change_last_state[1] + change_last_state[0])
#         KB.append("on_"+change_last_state[0]+change_last_state[1])
#         goal_state.pop()
#
#
#         # print "YAY"
#     elif "clear_" in goal_state[-1]:
#         last_ele = goal_state[-1].replace("clear_", "")
#         for i in KB:
#             if "on_" in i:
#                 i  = i.replace("on_","")  # type: str
#                 if last_ele in i:
#                     action_stack(i[0], table, i[1])
#                     # print
#                     # print "clear section"
#                     goal_state.append("movetotable_" + i[0] + i[1])
#                     goal_state.append("on_" + i[0]+i[1] + " clear_" + i[0])
#                     goal_state.append("clear_" + i[0])
#                     goal_state.append("on_" + i[0]+i[1])
#                     break
#
#     elif "movetotable_" in goal_state[-1]:
#         plan.append(goal_state[-1])
#         # goal_state.pop()
#         # print "321321321321"
#         totable = goal_state[-1].replace("movetotable_","")
#
#         for i in KB:
#             if "on_" in i:
#                 newi = i.replace("on_","")
#     #             # print "new",newi[0]
#     #             # print "new", newi[1]
#                 KB.append("ontable_"+ newi[0])
#                 KB.append("clear_" + newi[1])
#                 KB.remove(i)
#         goal_state.pop()
#     elif "movefromtable_" in goal_state[-1]:
#         # KB.sort(reverse=True)
#         plan.append(goal_state[-1])
#         # goal_state.append("1")
#         fromtable = goal_state[-1].replace("movefromtable_", "")
#         # print "12321321",fromtable[0]
#         goal_state.remove(goal_state[-1])
#         # print goal_state
#
#
#         # print "hihi",fromtable
#         temp = ""
#         temp2 = ""
#         if len(goal_state) ==2:
#             for i in KB:
#                 newi2 = i.replace("ontable_", "")
#                 if "on_" in i:
#                     newi2 = i.replace("on_", "")
#                     KB.append("ontable_"+newi2[1])
#                     KB.append("clear_" + newi2[0])
#                     KB.remove("on_" + newi2[0] + newi2[1])
#
#             for i in KB:
#                 newi2 = i.replace("ontable_", "")
#                 if fromtable[1] == newi2:
#                     temp2 = newi2
#                     # print "fromtable",fromtable[1]
#                     # print "temp2",temp2
#                 if fromtable[0] == newi2:
#                     # print "fromtable", fromtable[0]
#                     # print "newi",newi
#                     # print "HERE HERE","clear_"+fromtable[0]
#                     # print KB
#                     # KB.remove(i)
#                     KB.remove("clear_"+fromtable[1])
#                     KB.append("on_"+fromtable[1]+fromtable[0])
#                     # goal_state.remove("on_"+fromtable[0]+fromtable[1])
#
#             # print "CHECK CHECK", newi2[0], newi2[1]
#         else:
#             string2 =""
#             for i in KB:
#                 newi = i.replace("ontable_", "")
#                 # print newi
#                 if fromtable[1] == newi:
#                     temp = newi
#                     # print "fromtable",fromtable[1]
#                     # print "temp",temp
#                 if fromtable[0] == newi:
#                     # print "fromtable", fromtable[0]
#                     # print "newi",newi
#                     # print i
#                     KB.remove(i)
#                     KB.remove("clear_"+temp)
#                     KB.append("on_"+temp+newi)
#                     goal_state.remove("on_"+temp+newi)
#         # counter1 += 1
#     for i in goal_state:
#         for j in KB:
#             i_list = i.split(" ")
#             # print i_list
#             # if len(i_list) >= 2:
#             #     goal_state.pop()
#             #     break
#             if j == i:
#                 goal_state.remove(j)
#
#     for i in goal_state:
#         for j in KB:
#             i_list = i.split(" ")
#             if j == i:
#                 goal_state.remove(j)
#     if len(goal_state)>0:
#         check_last_ele = goal_state[-1].split(" ")
#         # print "check", check_last_ele
#         if len(check_last_ele) >= 2 and len(goal_state)>1:
#             goal_state.pop()
#     counter +=1
# # j = len(goal_state[-1].split(" "))
# print
# for i in xrange(len(goal_state)):
#
#     # if -i == i:
#     #     for k in xrange(j):
#     #         print goal_state[-1].split(" ")[-k]
#
#     print goal_state[-i -1]
#
#
#
#
# print
# print
# print "Goal State     ",goal_state
# print "Knowledge Base " ,KB
# print
# print initial_state
# print table
# print plan
#
# # print string2




#     if "stack(" in stack[-1]:
#         ele = stack[-1].replace("stack(", "")
#         ele = ele.replace(")", "")
#         ele = ele.replace(",", "")
#         clear = "clear(" + ele[1] + ")"
#         holding = "holding(" + ele[0] + ")"
#         temp_stack.append(clear)
#         temp_stack.append(holding)
#     if "holding(" in stack[-1]:
#         ele = stack[-1].replace("holding(", "")
#         ele = ele.replace(")", "")
#         ele = ele.replace(",", "")
#         pickup = "pickup("+ele+")"
#         armempty = "armempty()"
#         ontable = "ontable("+ele+")"
#         clear = "clear("+ele+")"
#         stack.append(pickup)
#         temp_stack.append(armempty)
#         temp_stack.append(ontable)
#         temp_stack.append(clear)
#     if "clear(" in stack[-1]:
#         ele = stack[-1].replace("holding(", "")
#         ele = ele.replace(")", "")
#         ele = ele.replace(",", "")

temp_list = [{'params': '1', 'type': 'predicate', 'name': 'ontable'}, {'params': '1', 'type': 'predicate', 'name': 'clear'}, {'params': '3', 'type': 'predicate', 'name': 'clear'}, {'params': '2', 'type': 'predicate', 'name': 'ontable'}, {'params': '2', 'type': 'predicate', 'name': 'clear'}, {'params': '3', 'type': 'predicate', 'name': 'ontable'}]


for i in range(len(temp_list)):
    while '2' in temp_list[i]['params']:
        print temp_list.pop(i)

# print temp_list.pop(4)
# print temp_list.pop(3)
# print temp_list