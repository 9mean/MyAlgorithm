#사과나무(다이아몬드)
n=int(input())
farm=[list(map(int,input().split())) for _ in range(n)]
mid=n//2
k=0
b=[]
for i in range(n):
  if mid>=i:
    b=farm[i][mid-i:mid+i+1]
    k+=sum(b)
  else:
    b=farm[i][i-mid:n-i+mid]
    k+=sum(b)

print(k)