#후위표기식 만들기
n=list(map(str,input()))
cnt=0
stack=[]
avl=['+','-']
mul=['*','/']
res=""
for i in n:
  if ord(i)>=48 and ord(i)<=57:
    res+=i
  else:
    if i in avl:
      while stack:
        if stack[-1]=='(':
          break
        res+=stack.pop()
      stack.append(i)
    elif i in mul:
      while stack:
        if stack[-1]=='(' or stack[-1] in avl:
          break
        res+=stack.pop()
      stack.append(i)
    elif i=='(':
      stack.append(i)
    else:
      while stack:
        if stack[-1]=='(':
          stack.pop()
          break
        res+=stack.pop()
while stack:
  res+=stack.pop()
print(res)

