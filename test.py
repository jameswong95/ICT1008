import table
import time


#input_start_state = raw_input("Enter start state: ")
#input_goal_state = raw_input("Enter goal state: ")

# <-- Top | Bottom -->

# test 1: simple example
#input_init_state = "CA B D"  #Start State
#input_goal_state = "DCBA" #Goal State

# test 2: same amount of stacks example
#input_init_state = "CA FB DE"  #Start State
#input_goal_state = "BA DC FE" #Goal State

# test 3: init > goal example
#input_init_state = "BI ACDE FKL GJ HM"  #Start State
#input_goal_state = "ABC DEF GHM IJKL" #Goal State

# test 4: init < goal example
#input_init_state = "ABC DEF GHM IJKL" #Start State
#input_goal_state = "BI ACDE FKL GJ HM"  #Goal State

# test 5: deadlock example
#input_init_state = "AC B"  #Start State
#input_goal_state = "ABC" #Goal State

if input_init_state is input_goal_state:
    print("Start state and goal state are the same")
else:
    # create table obj
    # create the tables with stacks and blocks
    start_table = table.createTable(input_init_state)
    goal_table = table.createTable(input_goal_state)

    # code here
    dict = table.alt(start_table, goal_table)

    for k, v in dict.items():
        print(k, v)
