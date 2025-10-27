# str1= "안녕하세요"
# if "하" in str1:
#     print("'하'라는 글자가 존재합니다.")
# else: print("'하'라는 글자가 존재하지 않습니다")


# str2= "안녕하세요. 반갑습니다. 저는 홍길동입니다."
# # 1개의 글자를 입력받아 str1변수에 존재하는지 확인하시오.
# word= input("글자를 입력하시오")
# if word in str2: print("입력하신 글자가 문장에 포함되어있습니다")
# else: print("입력하신 글자가 문장에 포함되어있지 않습니다.")

# stu_data=[]
# stu_data.append(1)
# stu_data.append("홍길동")
# stu_data.append(100)
# stu_data.append(100)
# print(stu_data)


stu_datas=[]

name= input("이름을 입력하세요")
kor= int(input("국어점수를 입력"))
eng= int(input("영어점수를 입력"))
math= int(input("수학점수를 입력"))
total= kor+eng+math
avg= total/3
stu_data1= [name,kor,eng,math,total,avg]
print(stu_data1)
stu_datas.append(stu_data1)

name2= input("이름을 입력하세요")
kor2= int(input("국어점수를 입력"))
eng2= int(input("영어점수를 입력"))
math2= int(input("수학점수를 입력"))
total2= kor2+eng2+math2
avg2= total2/3
stu_data2= [name2,kor2,eng2,math2,total2,avg2]
print(stu_data2)

stu_datas.append(stu_data2)
print(stu_datas)



