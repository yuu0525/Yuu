import random as r
list=list(range(10))
r.shuffle(list)
print(list)
def quick_sort(list,left,right):
    if left<right:
        mid=partition(list,left,right)
        quick_sort(list,left,mid-1)
        quick_sort(list,mid+1,right)
def partition(list,left,right):
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
def quick_sort_V2(list,left,right):
    if left<right:
        mid=partition_V2(list,left,right)
        quick_sort_V2(list,left,mid-1)
        quick_sort_V2(list,mid+1,right)
def partition_V2(list,left,right):
    mid=list[right]
    while left<right:
        while left<right and list[left]<mid:
            left+=1
        list[right]=list[left]
        while left<right and list[right]>mid:
            right-=1
        list[left]=list[right]
    list[right]=mid
    return left
quick_sort_V2(list,0,len(list)-1)
print(list)
