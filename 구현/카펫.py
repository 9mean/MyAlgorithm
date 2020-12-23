#ac긴한데 범위잡기가 야메임..
yellow=2
brown=10
answer=[]
flag=0
for i in range(1,2500):
  for j in range(1,2500):
    if i*j==yellow and i>=j:
      if i*2+j*2+4==brown:
        answer.append(i+2)
        answer.append(j+2)
        flag=1
        break
  if flag==1:
    break
print(answer)