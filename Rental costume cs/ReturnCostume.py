from RentCostume import CostumeQuantity
import ReturnInvoice
import datetime


def returnCostume(costume):
    k=datetime.datetime.now()
    customerName=input("Enter the name of customer ->\n")
    try:
        costumeNo=int(input("Enter the costume number to return -> \n"))
    except ValueError:
        print("Please Enter an integer value for costumeno")    

    costumeReturnQuantity=int(input("Enter the quantity you wish to return ->\n"))
    rentDay=int(input("Please enter the rented day ( less than "+str(k.day)+")->"))
    for i in range(len(costume)):
        if(i+1==costumeNo):
                k=int(costume[i][3])
                k += costumeReturnQuantity
                costume[i][3]=k
                CostumeQuantity(costume)
                ReturnInvoice.invoice(costume,costumeNo,costumeReturnQuantity,customerName,rentDay)
                print("*******************************************")
                print("Return quantity successfully and quantity updated to "+str(costume[i][3]))
                print("*******************************************")
           
                       





    

    
    
    