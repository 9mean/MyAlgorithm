#왕실의 나이트
where=list(input())
dx=[0,-1,0,1]
dy=[-1,0,1,0]

#x찾기
wx=['a','b','c','d','e','f','g','h']
x=0
for i in wx:
  x+=1
  if where[0]==i:
    break

y=int(where[1])


cnt=0
for j in range(4):
    #상하2칸인경우
    if(j%2==0):
      nx=x+dx[j]
      ny=y+2*dy[j]
    #좌우2칸인경우
    else:
      nx=x+2*dx[j]
      ny=y+dy[j]
      
    if(nx>8 or ny>8 or nx<1 or ny<1):
        continue
    cnt+=1
    print(nx,ny)

print(cnt)
