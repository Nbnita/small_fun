import matplotlib.pyplot as plt
import random

n=2
e=list()
for i in range(10):
    x=random.randint(1,11)
    e.append(x)
final=list()
log=list()
for i in e:
    c=1-int(i)
    a=n*int(i)*c
    b=a+10
    log.append(a)
    final.append(b)
plt.plot(final,'b')
plt.plot(log,'r')
plt.title('Logistic')
plt.show()
