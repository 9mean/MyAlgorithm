#solve
#체육복
def solution(n, lost, reserve):

    answer=0
    for i in lost[:]:
        for j in reserve[:]:
            if i==j:
                reserve.remove(i)
                lost.remove(i)
#여벌체육복학생이 도난당하지 않은경우
    for i in lost[:]:
        for j in reserve[:]:
            if i not in lost:
                break
    #도난당한학생의 앞에 여벌학생이 존재한다면
            if i==j+1:
              lost.remove(i)
              reserve.remove(j)
              break
    #도난당한학생의 뒤에 여벌학생이 존재한다면    
            elif i==j-1:
              lost.remove(i)
              reserve.remove(j)
              break
    answer=n-len(lost)
    return answer