#뮤직비디오
n,m=map(int,input().split())
song=list(map(int,input().split()))
longest=sum(song)
s=max(song)
while s<=longest:
  mid=(s+longest)//2
  group=0
  cnt=0
  for i in song:
    if group+i>mid:
      cnt+=1
      group=i
    else:
      group+=i
  if cnt>=m:
    s=mid+1
  elif cnt<m:
    longest=mid-1
print(s)



