#스도쿠 검사
def check(x):
  for i in range(9):
    p=[0]*10
    q=[0]*10
    for j in range(9):
      p[x[i][j]]=1
      q[x[j][i]]=1
    if sum(p)!=9 or sum(q)!=9:
      return False
  for i in range(3):
    for j in range(3):
      a=[0]*10
      for k in range(3):
        for t in range(3):
          a[x[i*3+k][j*3+t]]=1
      if sum(a)!=9:
        return False
  return True

a=[list(map(int,input().split())) for _ in range(9)]
if check(a):
  print('YES')
else:
  print('NO')