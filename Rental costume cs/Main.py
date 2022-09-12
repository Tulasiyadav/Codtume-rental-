import RentCostume
import ReturnCostume




def openCostume():
    costume=[]
    with open("Costume.txt","r") as data_file:
        for line in data_file:
            data = line.strip().split(',')
            costume.append(data)
    data_file.close()
    return costume



def displayCostume(costume):
    
    print('''                     <<<-- Available Costumes in Stock -->>>''')
    print('''                           *---*---**---*---**---*---*       ''')
    for i in range(len(costume)):
        print((str(i+1))+"->"+" Costume Name-"+costume[i][0]+"   Brand-"+costume[i][1]+"   Price-"+costume[i][2]+"   Quantity-"+costume[i][3] )


 


def startProgram():
    try:
        indicator=True
        while indicator:
            print(''' 
                *---*---**---*---**---*---**---*---**---*---**---*---**---*---**---*---**---*---**---*---*
                                                       COSTUME RENTAL STORE                                      
                *---*---**---*---**---*---**---*---**---*---**---*---**---*---**---*---**---*---**---*---*
                    
                    
                                Enter D for Display all available costume in stock      
                                Enter R To Rent a Costume
                                Enter C To Return Costume                                             
                                Enter E To Exit  ''')
            selectOption = input('''Please Enter Value to perform task:- ''').upper()
            if selectOption == "D":
                displayCostume(openCostume())

            elif selectOption == "R":
                RentCostume.rentCostume(openCostume())  
                rentMore=True
                while(rentMore):
                    again=input("Do you want to rent more?").upper()
                    if again=="Y":
                        RentCostume.rentCostume(openCostume())
                    elif again=="N":
                        rentMore=False
                    else:
                        indicator=False

            elif selectOption == "C":
                l =openCostume()
                ReturnCostume.returnCostume(l)

            elif selectOption == "E":
                print("*---*---*>> We appreciate your visit <<*---*---*")
                indicator = False


            else:
                print("--------!!!!!! Please provide which task you want to perfom !!!!!!!--------")
                continue

    except ValueError:
        print("Error: Please enter an integer value")

startProgram()                                       






