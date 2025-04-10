import csv

with open("bank_details.csv",'r') as file:
    a=1
    read=csv.reader(file)
    for i in read:
        a+=1
    global Account_id
    Account_id=a-2



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



print("Select the option : \n 1) Create new Account \n 2) Log in \n ")
option_1=int(input("Enter the option : "))

if option_1==1:
    name=input("Enter the user name : ")
    password=input("Create the password to the account : ")
    initial_amount=int(input("Enter the initial amount to deposit (minimum Rs 100) : "))
    if initial_amount<100:
        print("The inital amount to be deposit should be minimum of Rs 100")
        initial_amount=int(input("Reenter the initial amount to deposit : "))
    add_user(Account_id,name,password,initial_amount)
    Account_id+=1
else:
    name=input("Enter the user name :")
    password=input("Enter the password : ")
    login=log_in(name,password)




