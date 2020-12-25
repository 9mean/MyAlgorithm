#재귀는 아름다워요
answer = 0
def DFS(idx, numbers, target, value,N):
    global answer
    
    if(idx== N and target == value):
        answer += 1
        return
    if(idx == N):
        return

    DFS(idx+1,numbers,target,value+numbers[idx],N)
    DFS(idx+1,numbers,target,value-numbers[idx],N)

def solution(numbers, target):
    global answer
    N=len(numbers)
    DFS(0,numbers,target,0,N)
    return answer