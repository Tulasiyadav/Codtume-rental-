import datetime

def invoice(costume,costumeNo,quantityamount,customerName,rentDay):
    a=datetime.datetime.now()

    for i in range(len(costume)):
        if(i+1==costumeNo):
            costumeName=costume[i][0]
            brand=costume[i][1]
            price=costume[i][2]
            quantity=costume[i][3]
    cost = price.split('$')
    cp = cost[1]
    rentedDays=(a.day)-rentDay
    totalPrice=round((float(cp)*float(quantityamount)),2)
    fineAmount=round((float(5/100) * float(totalPrice)),2)
    priceWithFine=round((float(totalPrice+fineAmount)),2)      

    g="Return"+customerName+costumeName+".txt"
    g=open(g,"w")
    g.write("\n")
    g.write("    |                                     ******* Quantity return *******                                                      "+"\n")
    g.write("\n"+"|****************************************************************************************************************"+"\n")
    g.write("\n"+"|Client's Name:"+customerName)
    g.write("\n"+"|Costume Name  :-->"+costumeName)
    g.write("\n"+"|Costume Brand :-->"+brand)
    g.write("\n"+"|Costume Price :-->"+cp)
    g.write("\n"+"|Costume Quantity : "+str(quantity))
    g.write("\n"+"|Quantity Reutrn :"+str(quantityamount))
    g.write("\n"+"|Return Date   :-->"+str(a.year)+" -"+str(a.month)+" -"+str(a.day))
    g.write("\n"+"|Rented Date   :-->"+str(a.year)+" -"+str(a.month)+" -"+str(rentDay))
    g.write("\n"+"|Total rented days:-->"+str(rentedDays))
    g.write("\n"+"|*---*---*--*---*---*--*---*---*--*---*---*")
    if (rentedDays>=5):
        g.write("\n"+"|Fine(in %)  :-->5%")
    g.write("\n"+"|Total Price:--> $"+str(totalPrice))
    if (rentedDays>=5):
        g.write("\n"+"|Fine Amount    :--> $"+str(fineAmount))
        g.write("\n"+"|Total Price(with fine)    :--> $"+str(priceWithFine))
    g.write("\n"+"|**********************************************************************************************************************")
    g.write("\n"+"|*---*---*--*---         Please double-check your invoice*---*---*--*---")
    g.write("\n"+"|*---*---**---*-          We appreciate your visit")
    g.write("\n"+"|*---*---**---*---**---*---**---*---**---*---**---*---**---*---**---*---**---*---**---*---**---*---**---*---*")
    g.close() 



    

    
    
    