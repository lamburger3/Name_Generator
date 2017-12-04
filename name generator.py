import random

first_name_1 = ("Rom", "Kor", "Sep", "Sor", "Ren", "Jarl", "Kren", "Balg", "Boro", "Orog", "Kora", "Imu")
first_name_2 = ("ulan", "ulas", "ulus" ,"ulan", "oran", "lero", "udan", "igan", "oro", "on", "uru", "korag", "lan")

last_name_1 = ("Rom", "Kor", "Sep", "Sor", "Ren", "Jarl", "Kren", "Balg", "Boro", "Orog", "Kora", "Imu")
last_name_2 = ("ulan", "ulas", "ulus" ,"ulan", "oran", "lero", "udan", "igan", "oro", "on", "uru", "korag", "lan")

group = list()

def random_name():
    for x in range(0, name_amount):
        fullfirstname = random.choice(first_name_1)+""+random.choice(first_name_2)
        fulllastname = random.choice(last_name_1)+""+random.choice(last_name_2)
        fullname = fullfirstname+ " " +fulllastname
    print fullname
    user_input()
    random_name()


def user_input():
    global name_amount
    try:
        name_amount = input("How many names would you like generated? ")
    except:
        print("Please enter a number: ")
        user_input()
user_input()
random_name()






