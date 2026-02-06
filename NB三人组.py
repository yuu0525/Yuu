import random
li=list(range(10));random.shuffle(li)
##1.快速排序  //速度一般情况下最快 三者时间复杂的皆为O（nlogn）
def quick_sort(li, left, right):
    if left < right:
        mid=partition(li,left,right)
        quick_sort(li, left, mid - 1)
        quick_sort(li, mid + 1, right)
def partition(list, left, right):
    tmp = list[left];mid=left+right
    while left<right:
        while list[right]>tmp and left<right:
            right-=1
        list[left]=list[right]
        while list[left]<tmp and left<right:##注意不要漏关键条件，left<right
            left+=1                         ##否则会不停止
        list[right]=list[left]
    list[right]=tmp
    return left
#quick_sort(li,0,len(li)-1)
#print(li)

##2.堆排序  //利用堆的特性进行排序，可用于解决topk问题
def heap_sort(li,low,high):
    n=len(li)
    for i in range((n-2)//2,-1,-1):  ##不要忘记是-2//2！！代表最末尾叶子的根
        sift(li,i,n-1)
    for i in range(n-1,-1,-1):
        li[i],li[0]=li[0],li[i]
        sift(li,0,i-1)  ##此处不要搞混传参的数为0与i-1
def sift(li,low,high):
    i=low ; j=i*2+1 ; tmp=li[i]
    while j<=high:
        if  j<high and li[j]<li[j+1]:  ##   注意要先判定右孩子存在！！
            j=j+1
        if li[j]>tmp:      ###这里是和tmp作比较！！！不是li【i】!!!
            li[i]=li[j]
            i=j;j=i*2+1   ##不要忘记交换完i和j向下移动！
        else:
            break
    li[i]=tmp
#heap_sort(li,0,len(li)-1)
#print(li)

##3.归并排序    //内存占用相对较大（会生成新列表）
def merge_sort(li,low,high):
    if low < high:  ##当元素大于两个就进行“分裂”
        mid=(low+high)//2
        merge_sort(li,low,mid)
        merge_sort(li,mid+1,high)
        merge(li,low,mid,high)      ##先分裂彻底再进行“拼接”
def merge(li,low,mid,high):  ##将列表按mid的位次分割后拼接
    i=low; j=mid+1;litmp=[]   ##注意拼接时的指针是分别从开头和中间开始！！
    while i<=mid and j<=high:
        while i<=mid and li[i]<=li[j]:
            litmp.append(li[i]);i=i+1
        while j<=high and li[i]>=li[j]:
            litmp.append(li[j]); j+=1
    while i<=mid:
        litmp.append(li[i]); i+=1
    while j<=high:
        litmp.append(li[j]); j+=1
    li[low:high+1]=litmp
merge_sort(li,0,len(li)-1)
print(li)






