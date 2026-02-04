import random as r
list=list(range(10))
r.shuffle(list)
print(list)
def quick_sort(list,left,right):
    if left<right:
        mid=portition(list,left,right)
        quick_sort(list,left,mid-1)
        quick_sort(list,mid+1,right)
def portition(list,left,right):
    mid=list[right]
    while left< right:
        tag=True
        while tag and left< right:
            if list[left]>mid:
                list[left],list[right]=list[right],list[left];tag=False
                break
            left+=1
        while not tag and left<right :
            if list[right]<mid:
                list[left],list[right]=list[right],list[left];tag=True
                break
            right-=1
    return left
quick_sort(list,0,len(list)-1)
print(list)
