#씨름선수
n=int(input())
a=[]
for i in range(n):
    tmp=list(map(int,input().split()))
    a.append(tmp)
a.sort()
cnt=1
w=a[0][1]
for i in range(n-1):
    k=0
    for j in range(i+1,n):
        if a[i][1]<a[j][1]:
            break
        k+=1
    if k==n-i-1:
        cnt+=1
print(cnt)