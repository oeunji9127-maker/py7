# 오늘은 이걸로만 복습하세요!!
# 최종복습

# 이름,국어,영어,수학,합계,평균

stu_datas=[]

stu_data=[]
name= input("학생이름을 입력하시오")
stu_data.append(name)
kor= int(input("국어점수를 입력하세요"))
stu_data.append(kor)
eng= int(input("영어점수를 입력하세요"))
stu_data.append(eng)
math= int(input("수학점수를 입력하세요"))
stu_data.append(math)
total= kor+eng+math
stu_data.append(total)
avg= total/3
stu_data.append(avg)
print(stu_data)
stu_datas.append(stu_data)

stu_data=[]
name= input("학생이름을 입력하시오")
stu_data.append(name)
kor= int(input("국어점수를 입력하세요"))
stu_data.append(kor)
eng= int(input("영어점수를 입력하세요"))
stu_data.append(eng)
math= int(input("수학점수를 입력하세요"))
stu_data.append(math)
total= kor+eng+math
stu_data.append(total)
avg= total/3
stu_data.append(avg)
print(stu_data)
stu_datas.append(stu_data)

stu_data=[]
name= input("학생이름을 입력하시오")
stu_data.append(name)
kor= int(input("국어점수를 입력하세요"))
stu_data.append(kor)
eng= int(input("영어점수를 입력하세요"))
stu_data.append(eng)
math= int(input("수학점수를 입력하세요"))
stu_data.append(math)
total= kor+eng+math
stu_data.append(total)
avg= total/3
stu_data.append(avg)
stu_datas.append(stu_data)
print(stu_data)

print("-"*50)
print(stu_datas)

# 가장 큰 리스트 안에 작은 리스트를 꺼내고 싶을 때
print(stu_datas[0])   # 오은지의 점수모음 출력
# 가장 큰 리스트 안에 작은 리스트 안의 항목을 꺼내고 싶을때
print(stu_datas[0][0])   # 오은지 출력 

