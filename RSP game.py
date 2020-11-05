import random
print("**********************Play Game Here******************* \n")
print("----Please Enter Between These Number Of Your Choice-----")
print("                   For  Rock- 1 \n")
print("                   For  Scissor- 2 \n")
print("                   For  Paper- 3 \n")
def choice(n):
    computer_choice = ['Rock', 'Scissor', 'Paper']

    a = random.choice(computer_choice)
    if(a=="Rock"and n==1):
        print("Computer Choice-",a,"\n")

        print("~~~~~~~~~~ TIE ~~~~~~~~~")
    elif(a=="Rock" and n==2):
        print("Computer Choice-",a,"\n")

        print("!!!!!!!Better Luck Next time!!!!!!!")
    elif((a=="Rock") and n==3):
        print("Computer Choice-",a,"\n")

        print("******Congrulations You win******")
    elif(a=="Scissor" and n==1):
        print("Computer Choice",a)

        print("******Congrulations You win******")
    elif(a=="Scissor" and n==2):
        print("Computer Choice-",a,"\n")

        print("~~~~~~~~~~ TIE ~~~~~~~~~")
    elif(a=="Scissor" and n==3):
        print("Computer Choice-",a,"\n")

        print("!!!!!!!Better Luck Next time!!!!!!!")
    elif(a=="Paper" and n==1):
        print("Computer Choice-",a,"\n")

        print("!!!!!!!Better Luck Next time!!!!!!!")
    elif(a=="Paper" and n==2):
        print("Computer Choice- ",a,"\n")

        print("******Congrulations You win******")
    elif(a=="Paper" and n==3):
        print("Computer Choice- ",a,"\n")

        print("~~~~~~~~~~ TIE ~~~~~~~~~")
a=int(input("Enter Your Choice:"))
if(a == 1):
    print("Your Choice - Rock")
    choice(a)
elif(a == 2):
    print("Your Choice - Scissor")
    choice(a)
elif(a == 3):
    print("Your  Choice -  Paper")
    choice(a)
else:
    print("You has choose wrong input")
