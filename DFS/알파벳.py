#1시10분시작
r,c=list(map(int,input().split()))
cnt=0
board=[]
check=[]

for i in range(r):
  board.append(list(input()))


def dfs(x,y):
  global cnt
  #범위벗어나면 탐색종료
  if( x<0 or x>r-1 or y<0 or y>c-1):
    return False
  #check배열에 탐색하는 보드에 해당하는 알파벳이 없다면 길탐색
  #탐색했다면 다신 검사안하기
  if board[x][y]!=0:
    if board[x][y] not in check:
      check.append(board[x][y])
      
      board[x][y]=0
      cnt+=1
      dfs(x+1,y)
      dfs(x-1,y)
      dfs(x,y+1)
      dfs(x,y-1)
      
      return cnt
    #check배열에 존재한다면 탐색그만
    else :
      board[x][y]=0
      return False
  #방문했다면 탐색그만
  else:
    return False


print(dfs(0,0))
# 10 10
# ASWERHGCFH
# QWERHDLKDG
# ZKFOWOHKRK
# SALTPWOKSS
# BMDLKLKDKF
# ALSKEMFLFQ
# GMHMBPTIYU
# DMNKJZKQLF
# HKFKGLKEOL
# OTOJKNKRMW
