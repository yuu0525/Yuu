li=list(range(16));import random;random.shuffle(li);print(li)
def merge_sort(li,low,high):
    if low<high:
        mid=(low+high)//2
        merge_sort(li,low,mid)
        merge_sort(li,mid+1,high)
        g(li,low,mid,high)
def g(li,low,mid,high):
    i=low;j=mid+1;new_li=[]
    while i<mid+1 and j<=high:
        if li[i]<li[j]:
            new_li.append(li[i])
            i=i+1
        else:
            new_li.append(li[j])
            j=j+1
    while i<=mid:
        new_li.append(li[i])
        i=i+1
    while j<=high:
        new_li.append(li[j])
        j=j+1
    li[low:high+1]=new_li
merge_sort(li,0,len(li)-1)
#li_test=[1,3,7,9,2,4,6,7];g(li_test,0,3,len(li_test)-1)
#print(li_test)
print(li)

