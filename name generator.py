import random
'''
These variables are stored with the first and second part that would make first and last names. These will be added together to form a full name
'''
first_name_1 = ("Rom", "Kor", "Sep", "Sor", "Ren", "Jarl", "Kren", "Balg", "Boro", "Orog", "Kora", "Imu", "Ora", "Imon", "Lukar", "Orlan", "Torg", "Ma", "Lor", "Be", "Uka", "Bori", "Zen", "Ze")
first_name_2 = ("ulan", "ulas", "ulus" ,"ulan", "oran", "lero", "udan", "igan", "oro", "on", "uru", "korag", "lan", "ohk", "lem", "tar", "sek", "cor", "kor", "sor", "mar", "kahn", "kan", "can", "mok", "yuk", "zar")

last_name_1 = ("Rom", "Kor", "Sep", "Sor", "Ren", "Jarl", "Kren", "Balg", "Boro", "Orog", "Kora", "Imu", "Ora", "Imon", "Lukar", "Orlan", "Torg", "Ma", "Lor", "Be", "Uka", "Bori", "Zen", "Ze")
last_name_2 = ("ulan", "ulas", "ulus" ,"ulan", "oran", "lero", "udan", "igan", "oro", "on", "uru", "korag", "lan", "ohk", "lem", "tar", "sek", "cor", "kor", "sor", "mar", "kahn", "kan", "can", "mok", "yuk", "zar")
'''
This function takes as a parameter the number of names to generate and generates and prints out that number of names
'''
def random_name(name_amount):
    try:
        for x in range(0, name_amount):
            fullfirstname = random.choice(first_name_1)+""+random.choice(first_name_2)
            fulllastname = random.choice(last_name_1)+""+random.choice(last_name_2)
            fullname = fullfirstname+ " " +fulllastname
            print fullname
    except:
       pass #Does nothing

'''
This function asks the user to enter a numerical value and returns that value
'''
def user_input():
    try:
        name_amount = input("How many names would you like generated? ")
        return name_amount
    except:
        print("Please enter a number: ")
        
'''
This function takes the numerical input from user_input and stores it in the "x" variable, then calls random_name with "x" as a parameter
'''
def main():
    while True:
        x = user_input()
        random_name(x)

'''
Calls the main function and starts the program
'''
main()






