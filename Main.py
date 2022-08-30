# Collatz Conjecture Generator
# Main procedure
    # Collect user data (how many runs wished, start num, end num, run intervals)
    # 
# loop_itteration = the amount of times the outer while loop has functioned
# collatz_number =
# Importing the text prettifier
from termcolor import colored
# importing mathplotlib to plot graphs
import matplotlib.pyplot as plt
import mplcyberpunk


# Defining defs
def p_red(text):
    # Prints red text from the var 'text'
    print(colored(text, 'red'))
    
def p_blue(text):
    # prints blue text from the var 'text'
    print(colored(text, 'blue'))

def p_green(text):
    # prints green text from the var 'text'
    print(colored(text, 'green'))

# # Varuibles
#     # Determines the type of numbers to run, as inputted by the user
# run_type = ''
#     # The initial input value for the range to run (before split)
# run_input = ''
#     # The list produced after splitting hte initial range run val
# split_list = []
#     # The final int. start num to the range
# start_range_num = 0
#     # The final int. end num to the range
# itteration_list = []
#     # The list of numbers which the program will run through / graph
# run_num = 0
#     # The current ORIGINAL number from the itteration list being run
# itr_num = 0
#     # The current itteration of the original num being run
# temp_check = 0
#     # Used to check if the itr_num is even or odd
# Introduction to program
# itteration_num = 0
# the number of itterations done
# x_axis_list
# a simple range list to corresponds to the x axis
p_green("Welcome to the Collatz conjecture simulator!\n")
print("Would you like to:\n")
p_red("1: run a single number")
p_red("2: run a range of numbers (eg.5-20)")
p_red("3: run a equation of numbers for a number of itterations (eg. n*3 = 5, 8, 11)")
run_type = input('')


if run_type == "1":
    print("input the number you'd like to run.")
    run_input = input('')
    itteration_list = []
    itteration_list.append(run_input)
    # split_list = run_input.split(":")
    # start_range_num = int(split_list[0])
    # end_range_num = int(split_list[1])
    # # appends the range of num into a list, plus one to end_range_num to make inclusive
    # for x in range(start_range_num, 1 + end_range_num):
    #     itteration_list.append(x)
# splits the range given by the user into a start and end var
    # the syntax given is "1:5"
if run_type == "2":
    print("input the range you'd like to run in this format (x:y)\n Note: range is inclusive.")
    run_input = input('')
    split_list = run_input.split(":")
    start_range_num = int(split_list[0])
    end_range_num = int(split_list[1])
    # appends the range of num into a list, plus one to end_range_num to make inclusive
    itteration_list = []
    for x in range(start_range_num, 1 + end_range_num):
        itteration_list.append(x)

# For loop to run list of numbers (itterations)
    # check if num is even or odd (check last digit)
        # if odd run 3n+1
        # if even run n/2
    # if num = 1 break
temp = 0
itteration_num = -1
master_list = []
x_highest = 0
x_axis_list = []
marks_of_10k = 0
highest_num = 0
# Running the Collatz Conjecture
for run_num in itteration_list:
    # seperating the original num into the one being run
    itr_num = run_num
    # indexing the number of itterations done
    itteration_num = itteration_num + 1
    master_list.append([itteration_num])
    master_list[itteration_num].append(0)
    while True:
        master_list[itteration_num].append(itr_num)
        # to terminate the program whence the loop has been reached     
        if itr_num == 1:
            break
        # checking if odd or even, then running collatz conjecture
        if (itr_num % 2) == 0:  
            itr_num = itr_num/2        
        else:  
            itr_num = 3*itr_num+1
        # making a new list per itteration

    # removes the first int used to create the list at the start (line 82)
    master_list[itteration_num].pop(0)
    # making a corresponding list for the x axis which simply counts up by one until the length of itterations are reached
    plt.style.use("cyberpunk")
    plt.plot(master_list[itteration_num], label = run_num, marker = 's', markersize = 3)
    plt.xlabel('x - Itteration')
    plt.ylabel('y - Value')
    plt.title('The Collatz Conjecture')
    if max(master_list[itteration_num]) > highest_num :
        highest_num = max(master_list[itteration_num])
    # shows progress for really long itterations
    if itteration_num % 10000 == 0:
        if marks_of_10k == 0:
            print('Sucessfully started calculations')
        elif marks_of_10k > 0:
            print('Sucessfully calculated through '+str(itteration_num)+' itterations.')
        marks_of_10k = marks_of_10k + 1
    # plt.plot(a, marker='o')
    # plt.plot(b, marker='v')
    # plt.plot(c, marker='s')
plt.show()
print(highest_num)
# MAPTPLOTLIB defaults to counting up when a x axis is not provided, eliminating the need for a x_axis_list







# factors:
# choice of:
#     running a sequence of numbers (eg.1,2,3)
#     running an equation of numbers (eg. n+3 or n*3) for a number of itterations

# Make machine to append all runned numbers into a list
# use for 



# collatz_number = 0
# loop_itteration = 0
# term_itteration = 6
# while loop_itteration < terminal_itteration:
#     loop_itteration = loop_itteration + 1
    
