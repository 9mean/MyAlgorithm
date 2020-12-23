from itertools import permutations

#0을조심하자(앞에 0이있는경우)
#같은문자가있다면 즉 11같은거면 같은거로센다(중복조합)
#주어진 길이만큼 돌아서 
#ac
def solution(numbers):
    answer = 0

    a=[]
    for i in range(1,len(numbers)+1):
        k=permutations(numbers,i)
        for j in k:
            b="".join(j)
            a.append(int(b))
        a=list(set(a))
    
    for i in a:
        flag=0
        if i==1 or i==0:
            continue
        for j in range(2,i):
            if i%j==0:
                flag=1
                break
        if flag==0:
            answer+=1
    return answer