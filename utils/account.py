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
        if L[i][0] == usr:
            print L[i]
            return i
    return -1

def is_pass(pwd, i, L):
    if L[i][1] == pwd:
        return True
    return False
