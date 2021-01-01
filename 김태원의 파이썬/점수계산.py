#점수계산
n=int(input())
a=list(map(int,input().split()))

sum=0
flag=0
for i in a:
  if i==1:
    if flag==0:
      sum+=1
      flag=1
    else:
      flag+=1
      sum+=flag
      
  if i==0 and flag!=0:
    flag=0    
print(sum)  