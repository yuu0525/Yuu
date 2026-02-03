l=8
ls=[i for i in range(l)]
print(ls)
goal=int(input())
def fun_search(ls,goal):
    left=0;right=len(ls)-1;i=(left+right)//2
    while left<= right:
        if goal==ls[i]:
            return i
        elif goal>=ls[i]:
            left=i+1
        else:
            right=i-1
        i=(left+right)//2
    else :
        return mzd

