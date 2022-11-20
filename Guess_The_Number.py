import random 


ran_num = None
guess = None 

print("Welcome to my personal 'Guess The Number' Game.")


ran_num = random.randint(1,10) #change values as you wich 
print ("A random number has randomly been generated ...")


for i in range(1): #change the value as you wich 
    print("Guess the number ! Enter a value")
    guess = int(input())

    if (ran_num == guess):
        print("Congratz ! You've found the right one !")
        break
    else:
        print ("Wrong one ... Try again !")
    


