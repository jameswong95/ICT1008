import table
import time


#input_start_state = raw_input("Enter start state: ")
#input_goal_state = raw_input("Enter goal state: ")

#input_init_state = "BI ACDE FKL GJ HM"  #Start State
#input_goal_state = "ABC DEF GHM IJKL" #Goal State

input_init_state = "BI ACDE FKL GJ HM"  #Start State
input_goal_state = "ABC DEF GHM IJ KL" #Goal State


if input_init_state is input_goal_state:
    print("Start state and goal state are the same")
else:
    # create table obj
    # create the tables with stacks and blocks
    start_table = table.createTable(input_init_state)
    goal_table = table.createTable(input_goal_state)

    print start_table

    # algorithm 1
    a1_start = time.time()  # start timer

    # code here
    table.classicalPlanning(start_table, goal_table)

    a1_end = time.time()  # end timer
    a1_timeTaken = a1_end - a1_start  # total time taken

    # algorithm 2
    a2_start = time.time()  # start timer

    # code here

    a2_end = time.time()  # end timer
    a2_timeTaken = a2_end - a2_start  # total time taken

    if a1_timeTaken > a2_timeTaken:
        print("A2 is the better algorithm")
    elif a2_timeTaken > a1_timeTaken:
        print("A1 is the better algorithm")
    else:
        print("They both took the same amount of time wtf?")


