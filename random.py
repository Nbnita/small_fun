import matplotlib.pyplot as plt
import random
x=list()
y=list()
for i in range(10):
        X=random.randint(1,20)
        x.append(X)
for j in range(10):
        Y=random.randint(1,20)
        y.append(Y)

#s=size,c=color,marker=o(round)
#plt.scatter(X,Y, s=60, c='red', marker='^')
plt.plot(x,y,"r")
#plt.plot(y,"b")

#limits
plt.xlim(1,20)
plt.ylim(1,20)

#add title
plt.title('Relationship between coffee sold and temperature')

#add x and y labels
plt.xlabel('Cups of coffee sold')
plt.ylabel('temperature')

#show plot
plt.show()
