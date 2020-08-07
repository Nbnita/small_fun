import random
def my_random():
    return random.randint(1,7)
print(my_random())
ask=input("Do you want to roll again?(yes/no)-")
if ask=="yes":
    times=int(input("How many times?"))
    for j in range(times):
        print(my_random())
else:
    print("okay!Have a good day.")import random
