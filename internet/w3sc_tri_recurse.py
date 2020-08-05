# def tri_recursion(k):
#     print(k)
#     if(k > 0):
#      result = k + tri_recursion(k - 3)
#         #   print(result)
#     else:
#         result = 0 

#     print(k, result)
#     return result 

# print("\n\nrecursion example results")
# tri_recursion(9)


# def factorial(x):
#     """This is a recursive function 
#     to find the factorial of an integar"""

#     if x == 1:
#         return 1
#     else:
#         return (x * factorial(x-1))


num = 8
print("the factorial of", num, "is", factorial(num))

_list = [3,4,8,22,34,54,60]

def moving_difference(_list, differences = []):
    
    if len(_list) < 2:
        return differences
    else:
        differences.append(_list[1]- _list[0])
        return moving_difference(_list[1:], differences )

print(moving_difference(_list))





