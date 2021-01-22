#뱀3190
#7시30분
from collections import deque
def dfs(tx,ty):
    global cnt
    global dir
    flag=True
    while flag:
        cnt+=1
        #방향바꿀시간이 왔다면
        if bam and cnt==bam[0][0]+1:
            time,direction=bam.popleft()
            if direction=='D':
                dir+=1
            elif direction=='L':
                dir-=1
            #현재 상이었다면 우로
            if dir>3:
                dir=0
            #현재 우였다면 상으로
            elif dir<0:
                dir=3
        x,y=dq.pop()
        dq.append((x,y))
        take=0
        for i in range(4):
            tx=x+dx[i]
            ty=y+dy[i]
            if 0<=tx<=n-1 and 0<=ty<=n-1:
                if i==dir:
                    flag=True
                    #몸통과 부딪히면 false로 다시 셋팅
                    if (tx,ty) in dq:
                        flag=False
                        break
                    if m[tx][ty]!=2:
                        dq.popleft()
                    m[tx][ty]=0                
                    dq.append((tx,ty))
                    break
            #범위밖이면 일단 false로 박아두고
            else:
                flag=False
        
    return        
n=int(input())
k=int(input())
m=[[0]*n for _ in range(n)]
dir=0
#우하좌상순임
dx=[0,1,0,-1]
dy=[1,0,-1,0]
for _ in range(k):
    x,y=map(int,input().split())
    m[x-1][y-1]=2
L=int(input())
dq=deque()
bam=deque()
for i in range(L):
    x,c=map(str,input().split())
    bam.append((int(x),c))
cnt=0
dq.append((0,0))
dfs(0,0)
print(cnt)
#덱큐로 머리부분을 뒤에 append하고 사과가 있으면 꼬리그대로
# 없으면 꼬리부분 pop하는게 맞아
# 그리고 만약 머리가 몸통과 맞거나 범위밖이면 종료시키자 