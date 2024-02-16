# Program that stores your purchases in an excel and then allows you to retrieve and see certain data from them. 
import pandas as pd 
from datetime import datetime
import json

def fDeposit(balance):
    x = int(input("How much to deposit? (0 to Return)\n"))
    fX = float(x)
    if fX == 0:
        return balance

    ans = input("Are you Sure? (y/n) ")
    if ans == 'n':
        return balance
        
    nb = balance + fX
    return nb

def fWithdraw(balance):
    x = input("How much to withdraw? (0 to Return)\n")
    fX = float(x)
    if fX == 0:
        return balance

    ans = input("Are you Sure? (y/n) ")
    if ans == 'n':
        return balance

    nb = balance - fX     
    fType(fX)

    return nb

def fType(spent): 
    y = input("What kind of spending?\n1) Grocery\n2) Emergency\n3) Rent\n4) Fun\n")
    date = str(datetime.today().strftime('%Y-%m-%d'))
    item = [spent, int(y)]
    

    openFile =  open("history.json", 'r') 
    json_object = json.load(openFile)
    openFile.close()
    print(json_object)
    if not json_object[date]:
        print("off")
        json_object[date] = []
        json_object[date].append(item)
        return
    json_object[date].append(item)
    openFile =  open("history.json", 'w') 
    json.dump(json_object, openFile)
    openFile.close()
    return 
    
def fHistory(date):
    openFile =  open("history.json", 'r') 
    json_object = json.load(openFile)
    openFile.close()

    types = ["Grocery", "Emergency", "Rent", "Fun"]
    sums = [0, 0, 0, 0] 

    for item in json_object[date]:
        sums[item[1] - 1] += item[0]
    
    print("")
    for i in range(len(sums)):
        print(str(types[i]) + ": $" + str(sums[i]) + "\n")
    return 

def fBalance():
    f = open("balance.txt", 'r')
    balance = float(f.read())
    f.close()

    print("Balance: $", end = "")
    print(balance) 
    x = input("\n1) Deposit\n2) Withdraw\n3) Back\n")

    if int(x) == 3: 
        return 
    elif int(x) == 1: 
        nb = fDeposit(balance)
        print("\nNew Balance: $" + str(nb) + "\n\n")
        open("balance.txt", 'w').close()
        f = open("balance.txt", 'w')
        f.write(str(nb))
        f.close()

    else:
        nb = fWithdraw(balance)
        print("New Balance: $" + str(nb))
        open("balance.txt", 'w').close()
        f = open("balance.txt", 'w')
        f.write(str(nb))
        f.close()

def fStats():
    date = str(datetime.today().strftime('%Y-%m-%d'))
    fHistory(date)
    return 

check = False

while check == False:
    x = input("Welcome To The Money Machine.\nDisclaimer: Balance may not reflect actual balance in your bank account, please be cautious when spending your money.\n\nWhat do you need.\n1) See Balance\n2) See Today's Stats\n")
    if x == '1': 
        fBalance()
    elif x == '2':
        fStats()



