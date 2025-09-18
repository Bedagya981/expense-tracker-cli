import json
import sys
from expense import Expense
from datetime import date
import requests
try:
    f= open("expense.json", "r")
    expenses = json.load(f)
    f.close()
except FileNotFoundError:
    expenses = []
def main():
    inp = ''
    while inp != 'a' and inp != 'c' and inp != 'd' and inp != 'e':
        inp = input("Would you like to add expense(a), check expense(c), delete expense(d) or exit program(e): ")
    match inp:
        case 'a':
            addExpense()
        case 'e':
            sys.exit()
        case 'c':
            checkExpense()
        case 'd':
            deleteExpense()

def addExpense():
    expId = len(expenses) + 1
    expTitle = input("Enter the title of the expense: ").title()
    val = 1
    while val:
        try:
            expAmt = int(input("Enter the amount of expenditure: "))
            val = 0
        except:
            print("Enter valid amount")
            pass
    expDate = input("Enter the date of expenditure(YYYY-MM-DD) or leave empty for todays date: ")
    if expDate == '':
        expDate = str(date.today())
    expense = Expense(expId, expTitle, expAmt, expDate)
    expense_dict = {
        "id": expense.id,
        "title": expense.title,
        "amount": expense.price,
        "date": expense.date
    }
    expenses.append(expense_dict)
    f = open("expense.json", "w")
    json.dump(expenses, f, indent=4)
    f.close()
    main()

def checkExpense():
    inp = ''
    val = 0
    totalExp = 0
    while inp != 'a' and inp != 's':
        inp = input("Would you like to list all expenses(a) or check specific expense(s): ")
    currencyInp = 'a'
    while currencyInp != '' and currencyInp != 'p':
        currencyInp = input("Would you like to view the expenditure in default currency (NPR) or would you like to change the currency?\nFor default currency press enter\nFor your prefreed currency press(p)\nInput: ")
    if currencyInp != '':
        currencyConvert(inp)
    else:
        if inp == 'a':
            for i in expenses:
                print(f"ID: {i['id']}, Title: {i['title']}, Expenditure amount: {i['amount']}, Date of expenditure: {i['date']}")
        else:
            userInp = input("Enter the id or title of the expenditure: ")
            try:
                userId = int(userInp)
                for i in expenses:
                    if i['id'] == userId:
                        print(f"ID: {i['id']}, Title: {i['title']}, Expenditure amount: {i['amount']}, Date of expenditure: {i['date']}")
            except ValueError:
                for i in expenses:
                    if i['title'] == userInp.title():
                        print(f"ID: {i['id']}, Title: {i['title']}, Expenditure amount: {i['amount']}, Date of expenditure: {i['date']}")
                        val += 1
                    if val > 1:
                        for i in expenses:
                            if i['title'] == userInp.title():
                                totalExp += i['amount']
                        print(f"The total expenditure in {userInp.title()} till date is {totalExp}")

def deleteExpense():
    if not expenses:
        print("No expense to delete")
        return
    userInp = 0
    while userInp == 0:
        try:
            userInp = int(input("Enter the id of the expense to delete"))
        except ValueError:
            print("Enter Valid ID")
            pass
    val = 1
    for i in expenses:
        if i['id'] == userInp:
            expenses.remove(i)
            print(f"Expense of id {i['id']} is deleted")
            f = open("expense.json", "w")
            json.dump(expenses, f, indent=4)
            val = 0
    if val:
        print("ID of the expenditure not found")

def currencyConvert(inp):
    totalExp = 0
    apiKey = "ccaf62b6f807d19549257f2090b20862"
    response = requests.get(f"https://data.fixer.io/api/latest?access_key={apiKey}&format=1")
    data = response.json()
    val = 1
    while val:
        curr = input("Enter the currency code you want the amount in: ").upper()
        if curr in data['rates']:
            currConverted = (1/data['rates']['NPR'])*data['rates'][curr]
            val = 0
        else:
            print("Currency code not found")
    if inp == 'a':
        for i in expenses:
            print(f"ID: {i['id']}, Title: {i['title']}, Expenditure amount: {i['amount']*currConverted: .3f}, Date of expenditure: {i['date']}")
    else:
        userInp = input("Enter the id or title of the expenditure: ")
        try:
            userId = int(userInp)
            for i in expenses:
                if i['id'] == userId:
                    print(f"ID: {i['id']}, Title: {i['title']}, Expenditure amount: {i['amount']*currConverted: .3f}, Date of expenditure: {i['date']}")
        except ValueError:
            for i in expenses:
                if i['title'] == userInp.title():
                    print(f"ID: {i['id']}, Title: {i['title']}, Expenditure amount: {i['amount']*currConverted: .3f}, Date of expenditure: {i['date']}")
                    val += 1
                if val > 1:
                    for i in expenses:
                        if i['title'] == userInp.title():
                            totalExp += i['amount']
                    print(f"The total expenditure in {userInp.title()} till date is {totalExp*currConverted: .3f}")   


main()