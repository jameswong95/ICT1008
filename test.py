import table
import time


#input_start_state = raw_input("Enter start state: ")
#input_goal_state = raw_input("Enter goal state: ")

input_init_state = "B ACDE F G H"  #Start State
input_goal_state = "DC BA F E H G" #Goal State


if input_init_state is input_goal_state:
    print("Start state and goal state are the same")
else:
    # create table obj
    # create the tables with stacks and blocks
    final_size = len(input_goal_state.split())
    start_table = table.createTable(input_init_state, final_size)
    goal_table = table.createTable(input_goal_state, final_size)

    print start_table

    # algorithm 1
    a1_start = time.time()  # start timer

    # code here
    # table.classicalPlanning(start_table, goal_table)

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


