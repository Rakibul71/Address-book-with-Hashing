# import csv
# f=open("student.csv","a",newline="")
# tup1=("bob",19)
# writer=csv.writer(f)
# writer.writerow(tup1)
# f.close;



# print ("My name is Rakibull Islam ")

import csv

with open('student.csv') as csv_file:
    contacts=csv.DictReader(csv_file)
    for contact in contacts:
        print(contact['Name'],contact['Marks'])

