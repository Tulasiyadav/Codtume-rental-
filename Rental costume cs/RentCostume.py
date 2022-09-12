import RentInvoice
def rentCostume(costume):
    alphaCheck=True
    while(alphaCheck):
        name = input("Enter the customer's name here ->: ")
        if not name.isalpha():
            print("Please enter the valid name.")
        else:
            alphaCheck=False
            num=True
            while(num):
                try:
                    number=int(input("Enter costume number ->: "))
                    if (number<=(len(costume))):
                        num=False
                    else:
                        print("Enter value less than "+str(len(costume)+1)+" !")
                except ValueError:
                    print(" Please Enter an integer value for costume number.")

    loop=True
    while(loop): 
        quanantity = int(input("Enter quantity -> ")) 
        if int(costume[number-1][3])>=quanantity:  
            loop=False
            for i in range(len(costume)):
                if(i+1==number):
                    a = int(costume[i][3])
                    a -= quanantity
                    costume[i][3]=a
                    CostumeQuantity(costume)
                    RentInvoice.invoice(number,name,costume,quanantity)
                    print("*---*---**---*---**---*---**---*---**---*---**---*---**---*---**---*---**---*---**---*---*")
                    print("Congrats! "+costume[i][0]+ "Costume Rented successfully to "+ name)
                    print("        Please check your Invoice")
                    print("*---*---**---*---**---*---**---*---**---*---**---*---**---*---**---*---**---*---**---*---*")
        else:
            print("Sorry! We only have "+costume[number-1][3]+" costumes available.")

        
            
    
def CostumeQuantity(costume):
    with open("Costume.txt","w") as Data_update:
        for i in range(len(costume)):
            for j in range(len(costume[i])):
                if j==3 and i<(len(costume)-1):
                    Data_update.write(str(costume[i][j])+'\n')
                elif j==3 and i==(len(costume)-1):
                    Data_update.write(str(costume[i][j]))
                else:
                    Data_update.write(str(costume[i][j])+ ',')
    Data_update.close()                   

