#후위식 연산
n=list(map(str,input()))
stack=[]
res=0
for i in n:
  if i.isdecimal():
    stack.append(int(i))
  else:
    if i=='+':
      stack[-2]=stack[-2]+stack[-1]
    elif i=='-':
      stack[-2]=stack[-2]-stack[-1]
    elif i=='*':
      stack[-2]=stack[-2]*stack[-1]
    else:
      stack[-2]=stack[-2]//stack[-1]
    res=stack[-2]
    stack.pop()
print(res)