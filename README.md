# Yuu
download
[hanio.py](https://github.com/user-attachments/files/25042616/hanio.py)
def h(n,a,b,c):
    if n >0:
        h(n-1,a,c,b)
        print('第%s个盘子从%s到%s'%(n,a,b))
        h(n-1,c,b ,a)
h(3,'A','B','C')
