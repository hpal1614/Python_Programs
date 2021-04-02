str='geeks'
tmp=str+str
n=len(tmp)
for i in range(1,n+1):
    substring=tmp[i: i+n]
    if (str==substring):
         print(i)
print(n)
