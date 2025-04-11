import csv

with open("bank_details.csv",'r') as file:
    a=1
    read=csv.reader(file)
    for i in read:
        a+=1
    global Account_id
    Account_id=a-1

def write_file(account_id,message):
    f = "Account_" + str(account_id) + ".csv"
    with open(f,"a",newline='') as file:
        write=csv.writer(file)
        write.writerow([message])

def add_user(account_id,name,password,amount):
    with open("bank_details.csv",'a',newline="") as file:
        field_names=['Account ID','User Name','Password','Amount']
        write=csv.DictWriter(file,fieldnames=field_names)
        write.writerow({"Account ID":account_id,"User Name":name,"Password":password,"Amount":amount})
        f="Account_"+str(account_id)+".csv"
        with open(f,'w',newline='') as f1:
            write=csv.writer(f1)
            write.writerow([f'Account created Successfully\n Welcome {name}\n Initial Deposit amount Rs {amount}'])

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
                elif (manipulation=="withdraw amount" or manipulation=="transfer amount") and int(rows[i][3])<amount:
                    return 0
                elif manipulation=="withdraw amount" and int(rows[i][3])>=amount:
                    Amount = int(rows[i][3]) - amount
                    rows[i][3] = Amount
                file.seek(0)
                write.writerows(rows)
                break

def valid_user(account_id):
    with open("bank_details.csv",'r') as file:
        read=csv.DictReader(file)
        for i in read:
            if i['Account ID']==account_id:
                return True
    return False

def amount_transfer(my_account,sending_account,amount):
    with open("bank_details.csv","r+",newline='') as file:
        read=csv.reader(file)
        write=csv.writer(file)
        rows=list(read)
        counter=0
        for i in range(1,len(rows)):
            if rows[i][0]==my_account:
                Amount=int(rows[i][3])-amount
                rows[i][3]=Amount
                counter+=1
            if rows[i][0]==sending_account:
                Amount=int(rows[i][3])+amount
                rows[i][3]=Amount
                counter+=1
            if counter==2:
                file.seek(0)
                write.writerows(rows)
                break

def display_file(account_id):
    f = "Account_" + str(account_id) + ".csv"
    with open(f,"r") as file:
        read=csv.reader(file)
        for i in read:
            print(i)

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
                    print("Select the option \n 1) Check Balance \n 2) Deposit Amount \n 3) WithDraw Amount \n 4) Transfer amount \n 5) Display Transaction History \n 6)Logout")
                    option_2=int(input("Enter the option : "))

                    match option_2:

                        case 1:
                            check_balance=view(login)
                            print(f"Available balance : {check_balance}")

                        case 2:
                            deposit_amount=int(input("Enter the deposit amount : "))
                            deposit_Amount=operation(login,"deposit amount",deposit_amount)
                            print("Amount has been deposited")
                            write_file(login,f'Deposited amount Rs {deposit_amount}')

                        case 3:
                            withdraw_amount=int(input("Enter the withdraw amount : "))
                            withdraw=operation(login,"withdraw amount",withdraw_amount)
                            while withdraw==0:
                                print("Can't able to withdraw your available balance is less than the with draw amount")
                                withdraw_amount = int(input("Renter the withdraw amount : "))
                                withdraw = operation(login, "withdraw amount", withdraw_amount)
                            print("Amount with drawn successfully")
                            write_file(login,f'Withdrawn amount Rs {withdraw_amount}')

                        case 4:
                            another_account=input("Enter the account id you want to send : ")
                            valid_account=valid_user(another_account)

                            while valid_account!=True:
                                another_account = input("Renter the account id you want to send : ")
                                valid_account = valid_user(another_account)

                            amount=int(input("Enter the amount to be shared : "))
                            valid_amount=operation(login,"transfer amount",amount)
                            while valid_amount==0:
                                print("Can't able to transfer the amount because your available balance is less than the entered amount ")
                                amount = int(input("Enter the amount to be shared : "))
                                valid_amount = operation(login, "transfer amount", amount)

                            amount_transfer(login, another_account, amount)
                            write_file(login,f'Transferred amount Rs {amount} to account {another_account}')
                            write_file(another_account,f'Amount Rs {amount} credited from the account {login}')

                        case 5:
                            display_file(login)

                        case 6:
                            break

        case 3:
            break





