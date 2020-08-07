import random
outcomes= ["Random","Shillong","Friends","Rasmalai"]
for i in range(1):
    a=random.choice(outcomes)
x=list(a)
y=len(x)
z=list()
failed=0
n=3
print("The word has {} letter".format(y))
print("The first and last letters are {} and {}".format(x[0],x[-1]))
z.append(x[0])
z.append(x[-1])
for j in range(y-2):
    guess=input("Guess letters now:")
    if guess in x:
        z.append(guess)
        j+=1
        c=set(x)
        b=set(z)
        if c==b:
            print(a)
            break
    else:
        failed+=1
        print("Wrong!You have {} times left.".format(n-failed))
        if failed==n:
            print("Lose")
            break
