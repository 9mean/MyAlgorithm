#단어수학 1339
#2시40분시작
#문자는 상관이없어 결국엔 숫자를 어떻게 배치할거냐 이거잖아
#길이가 긴애의 앞에를 오름차순으로 먹인다
#문자열길이순대로 배열을 하고
# ACKGF
# 00FGF
# 000TA
n=int(input())
word=[]
v={}
for _ in range(n):
    tmp=input()
    word.append(tmp)
word.sort(key=len,reverse=True)
keyLen=len(word[0])

#첫번째 원소의 길이만큼 인덱싱돈다
for i in range(n):
    tmp=len(word[i])
    for j in range(keyLen-tmp):
        word[i]='0'+word[i]
#첫번째 원소의 길이만큼 인덱싱돈다
cnt=9
for i in range(keyLen):
    #각단어의 인덱스번호 비교
    for j in range(n):
        #딕셔너리에 존재하지않는다면 추가
        #각단어 인덱스에 값저장
        if word[j][i]!='0' and word[j][i] not in v:
            v[word[j][i]]=cnt
            cnt-=1
for i in range(keyLen):
    #각단어의 인덱스번호 변환
    for j in range(n):
        if word[j][i].isalpha():
            word[j]=word[j].replace(word[j][i],str(v[word[j][i]]))
            
        
res=0            
for i in range(n):
    res+=int(word[i])
print(res)