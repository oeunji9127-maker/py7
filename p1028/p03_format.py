# 1.

# year= 2025
# month= 10
# day= 28

# print("{}년 {}월 {}일".format(year,month,day))
# print(f"{year}년 {month}월 {day}일")


# 2.

# 3개의 값을 입력받아 숫자를 모두 합친 금액을 출력하시오.
# 1000원 이상 입력하세요
# 총금액: 1,000,000

# m1= int(input("금액1을 입력하세요 (1,000원이상 입력 바람)"))
# m2= int(input("금액2을 입력하세요 (1,000원이상 입력 바람)"))
# m3= int(input("금액3을 입력하세요 (1,000원이상 입력 바람)"))
# total= m1+m2+m3
# print(f"금액1: {m1}, 금액2: {m2}, 금액3: {m3}")  # ->> f()함수사용
# print("금액1: {}, 금액2: {}, 금액3: {}".format(m1,m2,m3))  # ->> format()함수사용
# print("입력하신 금액을 모두 합친 총금액은 다음과 같습니다 {:,d}".format(total))


# 이름, 국어, 영어, 수학점수를 입력받아
# 홍길동, 국어, 영어, 수학, 합계, 평균을 출력하시오

# name= input("이름을 입력하시오")
# kor= int(input("국어점수를 입력하시오"))
# eng= int(input("영어점수를 입력하시오"))
# math= int(input("수학점수를 입력하시오"))
# total= kor + eng + math
# avg= (kor + eng + math)/3

# print("이름:{}, 국어:{}, 영어:{}, 수학:{}, 합계:{}, 평균:{:.2f}".format(name,kor,eng,\
#     math,total,avg))
# print(f"이름:{name}, 국어:{kor}, 영어:{eng}, 수학:{math}, 합계:{total}, 평균:{avg:.2f}")

stu=[]

name= input("이름을 입력하시오>>")
stu.append(name)

kor= int(input("국어점수를 입력하세요>>"))
stu.append(kor)

eng= int(input("영어점수를 입력하세요>>"))
stu.append(eng)

math= int(input("수학점수를 입력하세요>>"))
stu.append(math)

total= kor + eng +math
stu.append(total)

avg= (kor + eng +math)/3
stu.append(avg)

print("이름:{}\n국어:{}, 영어:{}, 수학:{}, 합계:{}, 평균:{:.2f}".format(*stu))


