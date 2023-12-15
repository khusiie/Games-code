name = input("Type your name: ") 
print("welcome" ,name ,"to this adventure!")

answer =input(
    "you are on a dirt road, it has come to an end you can go left or right. which way would you like to go?").lower()

if answer == 'left':
    answer = input("you come to a river , you can walk to walk around and it or swim accross? Type walk to  walk around and swim to swim across:  ")
     
    if answer =="swim":
        print("you swim across and were eaten by the alligator.")
    elif answer == "walk":
        print("you walked for many miles,run out of water and you  lost the game.")

    else:
        print("Not a valid option. you lose.")

elif answer == 'right':
    answer =input("you come to a bridge, it looks wobbly do you want to cross it or head back(cross/back)?  ")


    if answer =="back":
        print("you go back and lose.")
    elif answer == "cross":
        answer = input("you cross the bridge and meet a stranger. Do you talk to them (yes/no)?")
        
        if answer =="yes":
           print("you talk to the stranger and they give you gold. You WIN!")
       
        elif answer =="no":
           print("you ignore the stranger and they are offended and you lose.")
        
        else:
           print("Not a valid option. you lose")
else:
    print("Not a valid option. you lose.")      


print("Thankyou for trying",  name )

