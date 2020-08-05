import random
word1 = input("please enter first word :")
word2 = input("please enter first word : ")

pass_lenght = int(input("how many chars of pass do you want(1-10) : "))


full_word = word1 + word2
password = "123-"
print(full_word)

for i in range(pass_lenght):

    while True:
        
        random_choice = random.randint(0, len(full_word)-1)

        if full_word[random_choice] not in password:
            break

    password += full_word[random_choice]
print(password)
