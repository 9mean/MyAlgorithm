#회문 문자열 검사
n=int(input())
for i in range(1,n+1):
  flag=0
  k=input()
  k=k.upper()
  left=0
  right=len(k)-1
  while left<right:
    if k[left]!=k[right]:
      print("#%d NO"%i)
      flag=1
      break
    left+=1
    right-=1
  if flag==0:
    print("#%d YES"%i)  
