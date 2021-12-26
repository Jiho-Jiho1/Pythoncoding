import sys

bankmoney = 100
username = input("Enter your username:")
def signup():
    correctpassword = "JIHO)&!!"
    inputpassword = input("Enter password:")
    if inputpassword == correctpassword:
        return True
    else:
        return False

def deposit():
    global username
    print("How much do you want to deposit?")
    depositmoney = int(input("Enter here:"))
    global bankmoney
    bankmoney += depositmoney
    print(username, " just deposited", depositmoney, "won!")

def withdrawal():
    global username
    print("How much do you want to withdrawal?")
    withdrawalmoney = int(input("Enter here:"))
    global bankmoney
    if bankmoney < withdrawalmoney:
        print(username,"you don't have enough money in you bank account!")
    else:
        bankmoney -= withdrawalmoney
        print(username," just withdrew", withdrawalmoney, "won!")

def balancecheck():
    print(username," has", bankmoney, "won in your account!")

while True:
    print("What do you want to do?")
    process = input("1.Deposit(D)  2.Withdrawal(W)  3.Balance check(C)  4.Quit(Q)")
    if process == "D":
        deposit()
    elif process == "W":
        passwordcorrect = signup()
        if passwordcorrect == True:
            withdrawal()
        else:
            print("The password is wrong, so you cannot withdrawal.")
    elif process == "C":
        balancecheck()
    elif process == "Q":
        print("Bank program is about to end! If you want to end the program, say yes. If not, say no.")
        quitquestion = input("Enter here:")
        if quitquestion == "yes":
            sys.exit()
    else:
        print("That is not an existing option! Please try again.")
    
    


