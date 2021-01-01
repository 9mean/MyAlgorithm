#회문 문자열 검사
n=int(input())
for i in range(n):
  s=input()
  s=s.upper()
  size=len(s)
  if s==s[::-1]:
    print("#%d YES"%(i+1))
  else:
    print("#%d NO"%(i+1))
