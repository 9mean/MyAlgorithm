#가장높은탑쌓기
n=int(input())
block=[list(map(int,input().split())) for _ in range(n)]
block.sort(reverse=True)
#각 인덱스마다 블록을 놓았을때 최대개수
d=[0]*(n)
d[0]=block[0][1]
res=0
for i in range(1,n):
    for j in range(i-1,-1,-1):
        if block[i][2]<block[j][2] and d[i]<d[j]:
            d[i]=d[j]
    d[i]+=block[i][1]
    if res<d[i]:
        res=d[i]
print(res)