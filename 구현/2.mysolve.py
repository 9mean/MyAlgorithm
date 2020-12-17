#시각
#틀림
n=int(input())
cnt=0
for i in range(n+1):
  for j in range(60):
    for k in range(60):
      #일의자리,십의자리가 3인경우
      if(i%10==3 or j%10==3 or k%10==3 or i//10==3 or j//10==3 or k//10==3):
        cnt+=1

print(cnt)