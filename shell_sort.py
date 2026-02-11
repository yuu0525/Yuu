li=list(range(1,10));import random
random.shuffle(li)
print(li)
def insert_sort(li,gap):
    for i in range(gap,len(li)):
        tmp=li[i];j=i-gap
        while j>=0 and tmp<li[j]:
            li[j+gap]=li[j]
            j-=gap
        li[j+gap]=tmp
def shell_sort(li,gap):
    while gap>0:
        insert_sort(li,gap)
        gap=gap//2
#shell_sort(li,gap=len(li)//2)
#print(li)
def shell_sort_V0(li):
    gap=len(li)//2
    while gap>0:
        for i in range(gap,len(li)):
            j=i-gap;tmp=li[i]
            while j >=0 and li[j]>tmp:
                li[j+gap]=li[j]
                j-=gap
            li[j+gap]=tmp
        gap=gap//2
#shell_sort_V0(li)
#print(li)
def insort_sort_V0(li):
    for i in range(1,len(li)):
        j=i-1;tmp=li[i]
        while j>=0 and li[j]<tmp:
            li[j+1]=li[j]
            j-=1
        li[j+1]=tmp
insort_sort_V0(li)
print(li)


