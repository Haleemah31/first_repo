# def bla(*numbers):
#     print(numbers)
#     for i in numbers:
#         print(i*2)

# bla(2, 4, 6)

# def name (*char):

#     for i in char:
#         for x in i:
#             print (x.swapcase())

# name ("of", "set", "oh")


# def students(**data):
#     print(data)

# students(ade=23, bolu=12, shade=54, sean=50)


# def products(**data):
#     for key in data:
#         print(key, ":", data[key])

#         prices = sum(data.values())
#         print("total :", prices)
    
# products(coke=100, fanta=200, soda=150)


# def sort_values(*scattered_list, should_be_ascending = True):
#     scattered_list = list(scattered_list)

#     for i in range(len(scattered_list)):
        
#         for i in range(len(scattered_list)-1):
            
#             if scattered_list[i] > scattered_list[i+1]:
                
#                 scattered_list[i], scattered_list[i+1] = scattered_list[i+1], scattered_list[i]

#     if should_be_ascending:
#         print(scattered_list)
#     else:
#         print(scattered_list[::-1])


# sort_values(2,1,4,6,7,8,34,22,8,9,10)


def string_processor(string):
    string = string.lower()
    unique_values = list(set(string))
    quantities = []

    for value in unique_values:
        quantities.append(string.count(value))

    zipped_vals = list(zip(unique_values,quantities))

    sort_values(*zipped_vals, should_be_ascending=False)



    string_processor("I have a dream, a song to sing. To help me cope")