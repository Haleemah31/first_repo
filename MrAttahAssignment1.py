# text1 = "BH"
# text2 = "HE"

# txt1list = list(text1)
# txt2list = list(text2)

# result = ""

# for val in txt1list:
#     for sval in txt2list:
#         result += (val + sval) + ",\n"

# print(result)


text1 = "dara"
text2 = "rauf"
text3 = "tayo"

txt1list = list(text1)
txt2list = list(text2)
txt3list = list(text3)

result = ""
for val in txt1list:
    for sval in txt2list:
        for yval in txt3list:
            result += (val + sval + yval) + ",\n"

print(result)
