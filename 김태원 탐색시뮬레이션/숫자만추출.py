#숫자만 추출
s=input()
l=len(s)
t=""
for i in s:
  k=ord(i)
  if k>=48 and k<=57:
    t+=i
res=int(t)
print(res)
cnt=0
for i in range(1,res+1):
  if res%i==0:
    cnt+=1
print(cnt)