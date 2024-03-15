import pandas as pd 
from datetime import datetime
import json
import pika

# Function to deposit money into the balance
def fDeposit(balance):
    # Asking for the amount to deposit
    x = int(input("How much to deposit? (0 to Return)\n"))
    fX = float(x)
    if fX == 0:
        return balance

    # Confirming the deposit
    ans = input("Are you Sure? (y/n) ")
    if ans == 'n':
        return balance
        
    # Updating the balance
    nb = balance + fX
    return nb

# Function to withdraw money from the balance
def fWithdraw(balance):
    # Asking for the amount to withdraw
    x = input("How much to withdraw? (0 to Return)\n")
    fX = float(x)
    if fX == 0:
        return balance

    # Confirming the withdrawal
    ans = input("Are you Sure? (y/n)")
    if ans == 'n':
        return balance

    # Updating the balance
    nb = balance - fX     
    fConfirmSpending(fX)

    return nb

# PDF Creator Microservice by Ed 
def fCreatePDF(timeframe):
    openFile =  open("history.json", 'r') 
    json_obj = json.load(openFile)
    openFile.close()

    save_path = 'Expense-Report('+str(datetime.today().strftime('%Y-%m-%d'))+').pdf'
    data_tuple = (json_obj, save_path)
    serialized_tuple = json.dumps(data_tuple)

    connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))
    channel = connection.channel()
    channel.queue_declare(queue='expense-report')
    channel.basic_publish(exchange='',
                        routing_key='expense-report',
                        body=serialized_tuple)
    connection.close()
    return 


# Function to record the type of spending
def fConfirmSpending(spent): 
    # Asking for the type of spending
    y = input("What kind of spending?\n1) Grocery\n2) Emergency\n3) Rent\n4) Fun\n")
    date = str(datetime.today().strftime('%Y-%m-%d'))
    types = ["Grocery", "Emergency", "Rent", "Fun"]
    item = str({ "Expense Name": str(types[int(y) - 1]), "Date": str(datetime.today().strftime('%Y-%m-%d')), "Amount": str(spent) })
    
    # Opening the JSON file to store history
    openFile =  open("history.json", 'r') 
    json_object = json.load(openFile)
    openFile.close()

    # Appending the spending type and amount to the date
    json_object.append(item)

    # Writing the updated JSON object back to the file
    openFile =  open("history.json", 'w') 
    json.dump(json_object, openFile)
    openFile.close()
    return 
    
# Function to retrieve spending history for a specific date
def fHistory(date):
    # Opening the JSON file containing spending history
    openFile =  open("history.json", 'r') 
    json_object = json.load(openFile)
    openFile.close()

    # Types of spending
    types = ["Grocery", "Emergency", "Rent", "Fun"]
    sums = [0, 0, 0, 0] 

    # Calculating total spending for each type
    for item in json_object[date]:
        sums[item[1] - 1] += item[0]
    
    # Printing spending statistics
    print("")
    for i in range(len(sums)):
        print(str(types[i]) + ": $" + str(sums[i]) + "\n")
    return 

# Function to display balance and perform deposit or withdrawal
def fBalance():
    # Opening the file containing the balance
    f = open("balance.txt", 'r')
    balance = float(f.read())
    f.close()

    # Displaying the current balance
    print("Balance: $", end = "")
    print(balance) 
    x = input("\n1) Deposit\n2) Withdraw\n3) Back\n")

    # Performing deposit, withdrawal, or returning to main menu
    if int(x) == 3: 
        return 
    elif int(x) == 1: 
        nb = fDeposit(balance)
        print("\nNew Balance: $" + str(nb) + "\n\n")
        # Updating the balance file
        open("balance.txt", 'w').close()
        f = open("balance.txt", 'w')
        f.write(str(nb))
        f.close()

    else:
        nb = fWithdraw(balance)
        print("New Balance: $" + str(nb))
        # Updating the balance file
        open("balance.txt", 'w').close()
        f = open("balance.txt", 'w')
        f.write(str(nb))
        f.close()

# Function to display today's spending statistics
def fStats():
    date = str(datetime.today().strftime('%Y-%m-%d'))
    fHistory(date)
    return 

# Main program loop
check = False
while check == False:
    # Main menu options
    x = input("""Welcome To The Money Machine.\nDisclaimer: Balance may not reflect actual balance in your bank account, please be cautious when spending your money. What do you need.
    1) See Balance
    2) See Today's Stats
    3) Create PDF of Spendings\n""")
    if x == '1': 
        fBalance()
    elif x == '2':
        fStats()
    elif x == '3':
        fCreatePDF(30)
