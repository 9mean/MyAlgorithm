#라이브러리를 활용한 조합
sys.stdin=open("input.txt", "r")
n, k=map(int, input().split())
a=list(map(int, input().split()))
m=int(input())
cnt=0
for x in it.combinations(a, k):
    if sum(x)%m==0:
        cnt+=1
print(cnt)