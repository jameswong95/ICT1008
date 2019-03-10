import table

#input_start_state = raw_input("Enter start state: ")
#input_goal_state = raw_input("Enter goal state: ")

# <-- Top | Bottom -->

# test 1: simple example
# working
#input_init_state = "CA B D"  #Start State
#input_goal_state = "DCBA" #Goal State

# test 2: same amount of stacks example
# working
#input_init_state = "CA FB DE"  #Start State
#input_goal_state = "BA DC FE" #Goal State

# test 3: init > goal example
# working
#input_init_state = "AE FB CD"  #Start State
#input_goal_state = "CBA FED" #Goal State

# test 4: init < goal example
# working
#input_init_state = "FEDCBA" #Start State
#input_goal_state = "CBA DEF"  #Goal State

# test 5: deadlock example
# working
#input_init_state = "AC B"  #Start State
#input_goal_state = "CBA" #Goal State

# alt test case from blocks_problem with UI.py
# test 1: deadlock
# working
#input_goal_state = '123'
#input_init_state = '1 32'

# test 2
# working
#input_goal_state = '63 245 1'
#input_init_state = '2 3 16 5 4'

# test 3
# not working
#input_goal_state = '1 3 2 6 54'
#input_init_state = '23 1 654'

# test 4
# not working
#input_goal_state = '6 32 451'
#input_init_state = '2 31654'

# test 5
# not working
#input_goal_state = '6 32 45 1'
#input_init_state = '2 316 54'

# test 6
# not working
#input_goal_state = '6 3245 1'
#input_init_state = '2 316 54'

# test 7
# working
#input_goal_state = '63 245 1'
#input_init_state = '2 316 54'

# test 8
# working
#input_goal_state = '63 24 5 1'
#input_init_state = '231654'

if input_init_state is input_goal_state:
    print("Start state and goal state are the same")
else:
    # create table obj
    # create the tables with stacks and blocks
    start_table = table.createTable(input_init_state)
    goal_table = table.createTable(input_goal_state)

    # code here
    dict = table.alt(start_table, goal_table)

    for key, value in dict.items():
        print("Move {0}: {1}".format(key, value))

