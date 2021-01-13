#알리바바와 40인의도둑(탑다운)
def dfs(x,y):
    if x==0 or y==0 or d[x][y]!=0:
        return d[x][y]
    else:
        d[x][y]=min(dfs(x-1,y),dfs(x,y-1))+bridge[x][y]
        return d[x][y]
n=int(input())
bridge=[list(map(int, input().split())) for _ in range(n)]
d=[[0]*n for _ in range(n)]
d[0][0]=bridge[0][0]
for i in range(1,n):
    d[0][i]=d[0][i-1]+bridge[0][i]
    d[i][0]=d[i-1][0]+bridge[i][0]
print(dfs(n-1,n-1))