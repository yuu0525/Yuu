li_pre=list(range(100))
import random;random.shuffle(li_pre);li=li_pre[:10]
print(li)
k=int(input('k为：'))
def heap_topk(li,k):
    for i in range((len(li)-2)//2,-1,-1):
        sift(li,i,len(li)-1)
    for i in range(k):
        li[0],li[len(li)-i-1]=li[len(li)-i-1],li[0]
        sift(li,0,len(li)-2-i)
    print(list(reversed(li[len(li)-k:len(li)])))
def sift(li,left,right):
    i=left;j=i*2+1;tmp=li[i]
    while j<right+1:
        if j<right and li[j]<li[j+1]:
            j=j+1
        if li[j]>tmp:   ######和tmp比较！！！！！
            li[i]=li[j]
            i=j;j=i*2+1
        else:
            break
    li[i]=tmp
heap_topk(li,k)




