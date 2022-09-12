import datetime
import os.path
a = datetime.datetime.now()

def invoice(costumeName,customerName,costume,quantity):
    for i in range(len(costume)):
        if(i+1==costumeName):
         costumeName=costume[i][0]
         brand=costume[i][1]
         costumePrice=costume[i][2]

    cp = costumePrice.split('$')

    price= cp[1]

    if not os.path.exists(customerName+".txt"):
        x = customerName+".txt"
        x=open(x,"w")
        x.write("\n"+"|*---*---*--*---*---*---*---*---*--*---*---*--*---*---*--*---*---*--*---*---*--*---*---*--*---*---*--*---*---*--*---*") 
        x.write("\n"+"|                                                                   Date:"+str(a.year)+" /" +str(a.month)+" /" +str(a.day))
        x.write("\n"+"|                                                                    PAN No. 23254165")
        x.write("\n"+"|                           CostumeRental Store                    ")
        x.write("\n"+"|                           Biratnagar,Nepal                       ")
        x.write("\n"+"|                                                             Contact no.: 024-5656652")
        x.write("\n"+"|*---*---*--*---*---*--*---*---*--*---*---*--*---*---*--*---*---*--*---*---*--*---*---*--*----*---*--*---*---*--*---*--")
        x.write("\n"+"|Client's Name:"+str(customerName))
        x.write("\n"+"|Costume Name:"+costumeName)
        x.write("\n"+"|Brand"+brand)
        x.write("\n"+"|Quantity:"+str(quantity))
        x.write("\n"+"|CostumePrice"+costumePrice)
        x.write("\n"+"|*---*---*--*---*---*--*---*---*--*---*---*")
        x.write("\n"+"|Total Price: $"+str(float(price)*quantity))
        x.write("\n"+"|*---*---*-*---*---*-*---*---*-*---*---*-*---*---*--*---*---*--*---*---*--*---*---*--*---*--")
        x.write("\n"+"|                                  Please double-check your invoice")
        x.write("\n"+"|                                  We appreciate your visit")
        x.write("\n"+"|*---*---*-*---*---*-*---*---*-*---*---*-*---*---*-*---*---*-*---*---*-*---*---*"+"\n"+"\n")
        x.close()
        
    else:
        x = customerName+".txt"
        x=open(x,"a")
        x.write("\n"+"\n"+"\n"+"*---*---*-*---*---*-*---*---*-*---*---*-*---*---*-*---*---*-*---*---*-*---*---*-*---*---*-*---*---*-*--")
        x.write("\n"+"|*---*---*-*---*---*-*---*---*-*---*---*-*---*---*-*---*---*--*---*---*--*---*---*--*---*---*--*---*---*--*---*---")
        x.write("\n"+"|                                                                Date:"+str(a.year)+" / "+str(a.month)+" / "+str(a.day))
        x.write("\n"+"|                                                                PAN No. 23254165")
        x.write("\n"+"|*---*---**---*---**---*---* CostumeRental Store *---*---**---*---**---*---*--*---*---*--*")
        x.write("\n"+"|   *********************    Biratnagar,Nepal  *************************    ")
        x.write("\n"+"|                                                               Contact No.: 024-5656652")
        x.write("\n"+"|*---*---**---*---**---*---**---*---**---*---**---*---**---*---**---*---**---*---*--*---*---*")
        x.write("\n"+"|Client's Name:"+str(customerName))
        x.write("\n"+"|Costume Name:"+costumeName)
        x.write("\n"+"|Brand"+brand)
        x.write("\n"+"|Quantity:"+str(quantity))
        x.write("\n"+"|CostumePrice:"+costumePrice)
        x.write("\n"+"|*---*---**---*---**---*---**---*---**---*---*--*---*---*--*---*---*--*---*---*--*---*---*")
        x.write("\n"+"|Total Price"+str(float(price)*quantity))
        x.write("\n"+"|*---*---**---*---**---*---**---*---**---*---**---*---**---*---*--*---*---*--*----*---*---*")
        x.write("\n"+"|                             Please double-check your invoice")
        x.write("\n"+"|                             We appreciate your visit")
        x.write("\n"+"|*---*---**---*---**---*---**---*---**---*---**---*---**---*---*--*---*---*--*---*---*--*---*")
        x.close()