#회의실 배정(그리디)
n=int(input())
m=[]
for i in range(n):
  tmp=list(map(int,input().split()))
  l,r=tmp[0],tmp[1]
  tmp[0],tmp[1]=r,l
  m.append(tmp)
m.sort()


e,s=m[0][0],m[0][1]

cnt=1
i=0
while i<n-1:
  i+=1
  if m[i][1]>=e:
    cnt+=1
    e=m[i][0]
print(cnt)