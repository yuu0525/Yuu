list=list(range(10))
import random as r
r.shuffle(list);print(list)
def insert_sort_simple(list):   #时间复杂度O(n²)
    for i in range(1,len(list)):
        while i > 0 and list[i-1] > list[i]:
            list[i],list[i-1]=list[i-1],list[i]
            i-=1
    return list
print(insert_sort_simple(list))
print(insert_sort(list))

