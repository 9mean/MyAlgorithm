n=int(input())
data=list(map(str,input().split()))
print(data)
i=1
j=1

for key in data:
  if(i==0 or j==0):
    continue

  elif key=='R':
   i+=1
  elif key=='L':
    i-=1
  elif key=='U':
    j-=1
  elif key=='D':
    j+=1

print(i,j)    
