#주사위게임
n=int(input())
person=[]
for i in range(n):
  tmp=list(map(int,input().split()))
  person.append(tmp)
res=[]
for i in range(n):
  sum=0
  if person[i][0]==person[i][1] and person[i][1]==person[i][2]:
    sum=10000+person[i][0]*1000
  elif person[i][0]!=person[i][1] and person[i][1]!=person[i][2] and person[i][0]!=person[i][2]:
    sum=max(person[i])
  else:
    if person[i][0]==person[i][1]:
      sum=1000+person[i][0]*100
    elif person[i][0]==person[i][2]:
      sum=1000+person[i][0]*100
    else :
      sum=1000+person[i][1]*100
  res.append(sum)
print(max(res))    