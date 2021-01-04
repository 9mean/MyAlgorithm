#쇠막대기
n=list(map(str,input()))
cnt=0
stack=[]
for i in n:
  if i==')':
    if cur=='(':
      stack.pop()
      cnt+=len(stack)
    else:
      stack.pop()
      cnt+=1
  if i=='(':
    stack.append(i)
  cur=i
print(cnt)


