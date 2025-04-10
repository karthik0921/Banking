import csv

with open("bank_details.csv",'r') as file:
    a=1
    read=csv.reader(file)
    for i in read:
        a+=1
    global Account_id
    Account_id=a-1



def add_user(account_id,name,password,amount):
    with open("bank_details.csv",'a',newline="") as file:
        field_names=['Account ID','User Name','Password','Amount']
        write=csv.DictWriter(file,fieldnames=field_names)
        write.writerow({"Account ID":account_id,"User Name":name,"Password":password,"Amount":amount})

def log_in(name,password):
    with open("bank_details.csv",'r') as file:
        read=csv.DictReader(file)
        for i in read:
            if i['User Name']==name and i['Password']==password:
                return i['Account ID']
        return 0

def view(account_id):
    with open("bank_details.csv",'r') as file:
        read=csv.DictReader(file)
        for i in read:
            if i['Account ID']==account_id:
                return i['Amount']

def operation(account_id,manipulation,amount):
    with open("bank_details.csv",'r+',newline='') as file:
        read=csv.reader(file)
        write=csv.writer(file)
        rows=list(read)
        for i in range(1,len(rows)):
            if rows[i][0]==account_id:
                if manipulation=="deposit amount":
                    Amount=int(rows[i][3])+amount
                    rows[i][3]=Amount
                elif manipulation=="withdraw amount" and int(rows[i][3])<amount:
                    return 0
                else:
                    Amount = int(rows[i][3]) - amount
                    rows[i][3] = Amount
                file.seek(0)
                write.writerows(rows)
                break


while(1):
    print("Select the option : \n 1) Create new Account \n 2) Log in \n 3) Exit")
    option_1=int(input("Enter the option : "))

    match option_1:

        case 1:
            name=input("Enter the user name : ")
            password=input("Create the password to the account : ")
            initial_amount=int(input("Enter the initial amount to deposit (minimum Rs 100) : "))
            if initial_amount<100:
                print("The inital amount to be deposit should be minimum of Rs 100")
                initial_amount=int(input("Reenter the initial amount to deposit : "))
            add_user(Account_id,name,password,initial_amount)
            Account_id+=1

        case 2:
            name=input("Enter the user name :")
            password=input("Enter the password : ")
            login=log_in(name,password)

            if login!=0:
                while (1):
                    print("Select the option \n 1) Check Balance \n 2) Deposit Amount \n 3) WithDraw Amount \n 4) Logout")
                    option_2=int(input("Enter the option : "))

                    match option_2:

                        case 1:
                            check_balance=view(login)
                            print(f"Available balance : {check_balance}")

                        case 2:
                            deposit_amount=int(input("Enter the deposit amount : "))
                            deposit_Amount=operation(login,"deposit amount",deposit_amount)
                            print("Amount has been deposited")

                        case 3:
                            withdraw_amount=int(input("Enter the withdraw amount : "))
                            withdraw=operation(login,"withdraw amount",withdraw_amount)
                            if withdraw==0:
                                print("Can't able to withdraw your available balance is less than the with draw amount")
                                withdraw_amount = int(input("Renter the withdraw amount : "))
                                withdraw = operation(login, "withdraw amount", withdraw_amount)
                            print("Amount with drawn successfully")

                        case 4:
                            break

        case 3:
            break





