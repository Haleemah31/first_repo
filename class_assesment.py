# DICE ROLLING GAME

# import random

# player_score = 0

# while True:

#     input("please press enter to roll.!!")


# import datetime

# then = datetime.datetime.now()
# number_of_runs = 10000

# while number_of_runs>0:
#     500/2
#     number_of_runs -= 1
# now = datetime.datetime.now()

# time_taken = now- then
# print(time_taken.microseconds/1000) 

file = open("application_data.csv", "r")
write_file = open("application_data_copy.csv", "w")


for line_number, line in enumerate(file.readlines()):
    if line_number == 0:
        line_to_write = line.replace(line_to_w)
