#두 배열의 원소교체
n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.sort()
b.sort(reverse=True)
for i in range(k):
  if a[i]>=b[i]:
    break
  else:
    a[i]=b[i]
print(sum(a))