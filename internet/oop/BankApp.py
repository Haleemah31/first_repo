print ("Welcome to bankApp!")


logged_in_user = False
########

firstname = input("Please enter your name : ")
surname = input("Please enter your surname : ")
username = input("Please enter your username : ")

password = input("Please enter your password : ")
confirm_password = input("Please re-enter your password : ")

while password != confirm_password:
    
    while True:

    # task = input(("\nWelcome trinity bank \nPlease enter : \n# su for signup\n# si for signin\n# wr to add journal\n# r to read journal\n# del to delete jornal\n# stats to get stats\n\n> : ")


    # if task == "su":
    #     ############# Sign UP ######

    #         print("Sorry you passwords dont match !!\n")
    #         password = input("Please enter your password : ")
    #         confirm_password = input("Please re-enter your password : ")