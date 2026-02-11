import random

li_sort=[ 0 for _ in range(101)]
li=list(random.randint(1,100) for i in range(101))
for i in li:
    li_sort[i]+=1
for i in range(1,100):
    for j in range(li_sort[i]):
        print(i,end=" ")