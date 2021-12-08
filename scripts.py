import csv
# write the data on csv file
def write() :
    f=open("addressInfo.csv","w",newline="")
    addressInfoWriter=csv.writer(f)
    addressInfoWriter.writerow(['User_Name', 'Phone_Number',"User_Address","Birth_Date"])
    hashAddress=[]
    while True:
        name=input ("Enter User Name : ")
        PhnNumber=input("Enter Phone Number : ")
        UserAddress= input ("Enter User Address : ")
        UserMemoBirth=input ("Enter Birthdate : ")
        data=[name,PhnNumber,UserAddress,UserMemoBirth]
        hashAddress.append(data)
        YesNo=input("More (Y/N) ? ")
        if YesNo in "nN":
            break
    addressInfoWriter.writerows(hashAddress)
    print ("Data written in csv file Successfully")
    f.close()

# read the data from csv file 
def read() :
    f=open("addressInfo.csv","r",)
    print("Reading data from a csv file.")
    addressInfoReader=csv.reader(f) 
    for i in  addressInfoReader:   
        print(i)
    f.close()    

# search by mobile phone number and user name

def search() :
    f=open("addressInfo.csv","r",)
    print("Searching data from a csv file.")
    s=input("Enter User name to be searched : ")
    s=input("Enter mobile number  to be searched : ")
    addressInfoReader= csv.reader(f)
    for i in addressInfoReader :  
        if i[0] == s:
            print(i)
    f.close()
write()
read()
search()   

 