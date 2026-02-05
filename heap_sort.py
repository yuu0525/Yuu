import random
list=list(range(10));random.shuffle(list);print(list)
def heap_sort_V0(list,left,right):
    if left<right:
        heappush_V0(list,left,right)
        heap_sort_V0(list,left,right-1)
def heappush_V0(list,left,right):
    tag=True#控制器：决定何时结束向下调整
    while left<=right//2 :
        while left<right//2 and list[left]<max(list[left*2+1],list[left*2+2]):
            if list[left*2+1]<list[left*2+2]:
                list[left],list[left*2+2]=list[left*2+2],list[left]
            else:
                list[left],list[left*2+1]=list[left*2+1],list[left]
            tag=False  #执行了向下调整,marked
        left+=1
        if (not tag) and left==right//2:  #遍历完后，一次都没有执行向下调整，是大根堆
            left=0;tag=True
    list[0],list[right]=list[right],list[0];
#heap_sort_V0(list,0,len(list)-1)
def heap_sort_V1(list,low,high):
    for i in range((len(list)-1)//2,-1,-1):
        sift_V1(list,i,high)
    #1.先做一个大根堆
    for i in range(len(list)-1,-1,-1):
        list[0],list[i]=list[i],list[0]
        sift_V1(list,0,i-1)
    #2.逐一取出最大数并向下调取
def sift_V1(list,low,high):
    tmp=list[low];j=low*2+1
    while j<=high:
        if j<high and list[j]<list[j+1]:
            j=j+1
        if tmp<list[j]:
            list[low]=list[j]
            low=j;j=low*2+1
        else:
            break
    list[low]=tmp

heap_sort_V1(list,0,len(list)-1)
print(list)
