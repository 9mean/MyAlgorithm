#재귀함수이용한 이진수출력
def Binary(x):
  if x!=0:
    Binary(x//2)
    a.append(x%2)

n=int(input())
a=[]
Binary(n)
for i in a:
  print(i,end="")