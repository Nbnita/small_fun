import random
for i in range(1):
    a=random.randint(1,10)
turns= 3
if a%2==0:
    print("Hint - Number is even")
else:
    print("Hint - Number is odd")
for j in range(turns):
    guess=int(input('Guess a number between 1-10:'))
    if a==guess:
        print("Congrats!You won")
        break
    else:
        print("Sorry!Lose")
        j+=1
