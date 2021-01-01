from itertools import combinations
n,k=map(int,input().split())
card=list(map(int,input().split()))
#print(card)
ans=[]
idx=0
for i in combinations(card,3):
  sum=0
  sum=i[0]+i[1]+i[2]
  ans.append(sum)
ans.sort(reverse=True)
cnt=1
while True:
  if cnt==k:
    print(ans[idx])
    break
  if ans[idx]!=ans[idx+1]:
    cnt+=1
  idx+=1