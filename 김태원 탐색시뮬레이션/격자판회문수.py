#격자판 회문수
a=[list(map(int,input().split())) for _ in range(7)]
#행,열의 회문수를 담는 리스트 두개만든다
#각 포인팅으로 검사
res=0
for i in range(7):
  for j in range(3):
    s,e=j,j+4
    l,r=j,j+4
    row=0
    col=0
    while(s<e):
      if a[i][s]==a[i][e]:
        row+=1
        s+=1
        e-=1
      else:
        break
    if row==2:
      res+=1
    while(l<r):
      if a[l][i]==a[r][i]:
        col+=1
        l+=1
        r-=1
      else:
        break
    if col==2:
      res+=1
print(res)