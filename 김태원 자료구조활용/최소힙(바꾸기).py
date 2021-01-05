#아나그램
a=input()
b=input()

p=dict()
q=dict()
for i in a:
  p[i]=0
for i in a:
  p[i]+=1
for i in b:
  q[i]=0
for i in b:
  q[i]+=1
flag=0
for key,val in p.items():
  if q[key]!=val:
    print("NO")
    flag=1
    break
if flag==0:
  print("YES")

