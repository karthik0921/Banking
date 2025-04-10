import csv

with open("bank_details.csv",'r') as file:
    read=csv.reader(file)
    for i in read:
        print(i)