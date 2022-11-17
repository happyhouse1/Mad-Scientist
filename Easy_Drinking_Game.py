import random

ran1 = random.randint(1,6)
ran2 = random.randint(1,6)

print("Alea Jacta Est")
print("Dices are rolling ...")
print(ran1, "and", ran2)

if (ran1==ran2):
    print("Drink !")
else:
    print("Pass")