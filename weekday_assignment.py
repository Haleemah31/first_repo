# for i in range(100, 999):
#     sum_nums = i + i + i

#     last_char_of_num 

# = str(i)[2]*3

#     sum_nums_as_str = str(sum_nums)

#     print(i,sum_nums,last_char_of_num,sum_nums_as_str == last_char_of_num)

#     if sum_nums_as_str == last_char_of_num: break;



# PRINT EVEN AND ODD NUMBERS FOR DECADE
total_even = 0
total_odd = 0

for i in range(1,101):
    if i%2 == 0:
        total_even += i
        # print("even", i)
    else:
        total_odd +=i
        # print("odd", i)

    if i%10 == 0:
        print("decade - ", i, total_even,total_odd, total_even/total_odd)
        total_even = 0
        total_odd = 0



        
    