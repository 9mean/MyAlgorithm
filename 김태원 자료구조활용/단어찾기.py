#단어찾기

n=int(input())
a={}
for i in range(n):
  tmp=input()
  a[tmp]=1
for i in range(n-1):
  tmp=input()
  a[tmp]=0
for key,val in a.items():
  if val==1:
    print(key)
    break

