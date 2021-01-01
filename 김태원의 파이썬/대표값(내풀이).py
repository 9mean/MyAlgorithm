n=int(input())
score=list(map(int,input().split()))
sum=0
for i in score:
  sum+=i
avg=round(sum/n)
adj=123456789
idx=0
for i in range(n):
  if adj>abs(score[i]-avg):
    adj=abs(score[i]-avg)
    idx=i
  if adj==abs(score[i]-avg):
    if score[i]>score[idx]:
      idx=i
print(avg,idx+1)
