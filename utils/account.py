import hashlib

def get_file():
    f = open("data/accounts.txt", "r")
    L = f.read().splitlines()
    for i in range(len(L)):
        L[i] = L[i].split(",")
    f.close()
    return L

def add_usr_pwd(usr, pwd):
    f = open("data/accounts.txt", "a")
    f.write(usr + "," + pwd + "\n")
    f.close()

def is_user(usr, L):
    for i in range(len(L)):
        if L[i][0] == usr and usr != "":
            print L[i]
            return i
    return -1

def is_pass(pwd, i, L):
    if L[i][1] == pwd:
        return True
    return False

def login(usr, pwd):
    print usr
    print pwd
    L = get_file()
    i = is_user(usr, L)
    if is_user(usr, L) != -1:
        if is_pass(pwd, i, L):
            return 1
        return 2
    return 3

def register(usr, pwd):
    L = get_file()
    if usr == "":
        return 4
    if pwd == hashlib.sha224("").hexdigest():
        return 5
    if is_user(usr, L) != -1:
        return 6
    add_usr_pwd(usr, pwd)
    return 7

def get_message(x):
    if x == 2:
        return "Sorry, the password you submitted was incorrect."
    if x == 3:
        return "Sorry, the username you submitted does not exist."
    if x == 4:
        return "Please enter a username."
    if x == 5:
        return "Please enter a password."
    if x == 6:
        return "Sorry, that username already exists."
    if x == 7:
        return "Congratulations, your account has been created!"
