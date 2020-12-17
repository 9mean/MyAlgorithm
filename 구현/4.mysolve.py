#문자열 재정렬
input_data=list(input())
input_data.sort()
print(input_data)

sum=0
for i in input_data:
  column=int(ord(i))-int(ord('0'))
  if(column>=0 and column<=9):
    sum+=column
    input_data.remove(i)
    print(input_data)
  

sum=str(sum)
input_data.append(sum)
print(input_data)


# result=""
# for i in input_data:
#   result=result+i
# print(result)
