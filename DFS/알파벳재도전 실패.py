#11시반시작
#12시반끝
#알파벳 1987
def dfs(x,y,cnt):
    global res
    if visit[board[x][y]]==2:
        if res<cnt-1:
            res=cnt-1
        return
    else:
        
        for i in range(4):
            bx=x+dx[i]
            by=y+dy[i]
            if 0<=bx<=r-1 and 0<=by<=c-1 and v[bx][by]==0:
                v[bx][by]=1
                visit[board[bx][by]]+=1
                dfs(bx,by,cnt+1)
                v[bx][by]=0
                visit[board[x][y]]-=1
            
r,c=map(int,input().split())
board=[]
check=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','W','Y','Z']
v=[[0]*c for _ in range(r)]
for _ in range(r):
    tmp=input()
    board.append(tmp)
dx=[0,1,0,-1]
dy=[1,0,-1,0]
res=0
visit={}
for i in check:
    visit[i]=0
visit[board[0][0]]=1

v[0][0]=1
dfs(0,0,1)
print(res)