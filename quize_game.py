print("welcome to my computer quize ! ")
playing = input("Do you want to play?  ")
print (playing)

if playing.lower() != "yes":
    quit()

print("okay! let's play :)")
score=0

  
answer = input("what is the largest state in india by area?  ")
if answer =="rajasthan":
    print('Correct!')
    score +=1
else: 
    print('Incorrect!')


answer = input("What is the currency of india?  ")
if answer =="rupees":
    print('Correct!')
    score+=1
else: 
    print('Incorrect!')


answer = input("full form of CPU ?  ")
if answer =="central processing unit":
    print('Correct!')
    score+=1
else: 
    print('Incorrect!')

print("You got " +  str(score)  +  " questions correct!" )
print("You got " +  str((score/3)*100) + "%. " )