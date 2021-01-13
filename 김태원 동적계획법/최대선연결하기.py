#최대선연결하기
n=int(input())
line=list(map(int,input().split()))
#d배열은 인덱스마다 왼쪽에서 오른쪽으로 최대이을수있는 갯수
d=[0]*(n+1)
#1에서 시작할땐 당연히 최대길이 1
d[1]=1
res=0
#1은 했으니 2부터 n까지 구하자
for i in range(2,n+1):
    #각 정수에서 오른쪽의 인덱스를 구한다
    iidx=line.index(i)
    for j in range(i-1,1,-1):
        #왼쪽에서 i-1부터 1까지 인덱스를 비교하면서
        #최대값을 d[i]에 저장
        if iidx > line.index(j) and d[i]<d[j]:
            d[i]=d[j]
    #이전값의 +1을한다        
    d[i]=d[i]+1
    #반복문 돌때마다 최댓값 저장하기
    if res < d[i]:
        res=d[i]
    
print(res)