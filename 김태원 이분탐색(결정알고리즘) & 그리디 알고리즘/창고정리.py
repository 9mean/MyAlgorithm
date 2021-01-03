#창고정리

n=int(input())
a=list(map(int,input().split()))
m=int(input())
i=0

while i!=m:
  i+=1
  left=a.index(max(a))
  right=a.index(min(a))
  a[left]-=1
  a[right]+=1
a.sort(reverse=True)

print(a[0]-a[n-1])

  