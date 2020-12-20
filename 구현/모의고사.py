onelist=[1,2,3,4,5]
twolist=[2,1,2,3,2,4,2,5]
thrlist=[3,3,1,1,2,2,4,4,5,5]
answers=[1,2,3,4,5]
one=0
two=0
thr=0
onecnt=0
twocnt=0
thrcnt=0
for i in range(5):
  if i%5==0:
    one=0
  if i%8==0:
    two=0
  if i%10==0:
    thr=0
  if onelist[one]==answers[i]:
    onecnt+=1
  if twolist[two]==answers[i]:
    twocnt+=1
  if thrlist[thr]==answers[i]:
    thrcnt+=1
  one+=1
  two+=1
  thr+=1
k=onecnt
a=[]
one=1
two=2
thr=3
if k<twocnt:
  k=twocnt
  if k<thrcnt:
    a.append(thr)
  elif k==thrcnt:
    a.append(two)
    a.append(thr)
  else:
    a.append(two) 
elif k==twocnt:
  if k<thrcnt:
    a.append(thr)
  elif k==thrcnt:
    a.append(one)
    a.append(two)
    a.append(thr)
  else:
    a.append(one)
    a.append(two)
else:
  if k<thrcnt:
    a.append(thr)
  elif k==thrcnt:
    a.append(one)
    a.append(two)
  else:
    a.append(one)
print(a)