# from block_problem import *
def action(a):
    pass
    # stack[-1] = a
    # current_stack = stack[-1]
    # new_name = current_stack['name']
    # new_value = current_stack['params']
    # if new_name == 'unstack':
    #     steps.append(current_stack)
    #     new_value2 = new_value[2]
    #     temp_stack = {}
    #     temp_stack.update([('type', 'predicate'), ('name', 'clear'), ('params', new_value[2])])
    #     temp_start_stack.append(temp_stack)
    #     for i in temp_start_stack:
    #         if i['name'] == 'on' and i['params'] == str(new_value[0]) + "," + str(new_value[2]):
    #             ele_found = i
    #             temp_start_stack.remove(i)
    #     for i in temp_start_stack:
    #         if i['name'] == 'clear' and i['params'] == new_value[0]:
    #             ele_found = i
    #             temp_start_stack.remove(i)
    #
    #     arm.append(new_value[0])
    #     stack.pop()
    # elif new_name == 'pickup':
    #     arm.append(new_value)
    #     for i in temp_start_stack:
    #         if i['name'] == 'clear' and i['params'] == new_value:
    #             ele_found = i
    #             temp_start_stack.remove(i)
    #     for i in temp_start_stack:
    #         if i['name'] == 'ontable' and i['params'] == new_value:
    #             ele_found = i
    #             temp_start_stack.remove(i)
    #     for i in temp_start_stack:
    #         if i['name'] == 'on' and i['params'][0] == new_value:
    #             ele_found = i
    #             temp_start_stack.remove(i)
    #     stack.pop()
    #     steps.append(current_stack)
    # elif new_name == 'stack':
    #     for i in temp_start_stack:
    #         if i['name'] == 'clear' and i['params'] == new_value[2]:
    #             ele_found = i
    #             temp_start_stack.remove(i)
    #     temp_stack.update([('type', 'predicate'), ('name', 'clear'), ('params', new_value[0])])
    #     temp1_stack.update([('type', 'predicate'), ('name', 'on'), ('params', new_value[0] + "," + new_value[2])])
    #     temp_start_stack.append(temp_stack)
    #     temp_start_stack.append(temp1_stack)
    #     stack.pop()
    #     steps.append(current_stack)
    #     arm.pop()
    # elif new_name == 'putdown':
    #     temp_stack = {}
    #     temp1_stack = {}
    #     if len(new_value) == 1:
    #         temp_stack.update([('type', 'predicate'), ('name', 'clear'), ('params', new_value)])
    #         temp1_stack.update([('type', 'predicate'), ('name', 'ontable'), ('params', new_value)])
    #         temp_start_stack.append(temp_stack)
    #         temp_start_stack.append(temp1_stack)
    #     else:
    #         temp_stack.update([('type', 'predicate'), ('name', 'clear'), ('params', new_value[0])])
    #         temp1_stack.update([('type', 'predicate'), ('name', 'on'), ('params', new_value[0] + "," + new_value[2])])
    #         temp_start_stack.append(temp_stack)
    #         temp_start_stack.append(temp1_stack)
    #     stack.pop()
    #     steps.append(current_stack)
    #     arm.pop()