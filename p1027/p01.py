# 지난시간 내용을 복습해봅시다!

# a= input("숫자를 입력하세요.")
# print("입력된 숫자:", int(a)+10)

# 두수를 입력받아 합을 출력하시오.
# num= int(input("숫자를 입력하시오."))
# num2= int(input("숫자를 입력하시오."))
# print(num+num2) # >>문자열을 숫자타입으로 변경시켜줘야 한다

# 산술연산자
# 비교연산자 # 크다, 작다, 크거나 같다, 작거나 같다.
# and, or, not
# if else

# print()의 다양한 출력형태
# 두수를 입력받아, 합을 출력하시오.
# 10+5 = 15

# num1= int(input("정수1을 입력하시오."))
# num2= int(input("정수2를 입력하시오."))

# 앞쪽 문자열에 % 뒤의 변수값을 할당하는 방식
# 숫자: 정수-%d: 자리수 지정가능, 빈공백을 0으로 채울 수 있다.
# 실수-%f: 자리수 지정가능, 소수점 표현제한이 가능하다.
# 문자열: %s
# print("%d + %d = %d" % (num1,num2,num1+num2))
# 타입이 다른 데이터를 쌍따옴표 ""안에 넣어주겠다는 뜻
# 문자열 안에 데이터 타입이 다른 정수형 데이터 (%d)를 넣어주겠다


# 잘 알아두기!!
# print(100)
# print("%d" % 100)
# print("%5d" % 100)   #5자리 공간확보
# print("%05d" % 100)  #5자리 공간확보 및 빈공백 0으로 채우기
# print("%f" % (10/3))
# print("%.2f" % (10/3)) # 소수점2자리까지 제한
# print("%10.2f" % (10/3)) #10자리 공간확보 및 소수점2자리까지 제한
# print("%010.2f" % (10/3)) #빈공백 0으로 채우고 10자리 공간확보

# 숫자3개를 입력받아, 2025년 10월 27일 형태로 출력하시오
# % print를 사용할 것

# year= int(input("숫자 년도를 입력하시오"))
# month= int(input("숫자 월을 입력하시오"))
# day= int(input("숫자 일을 입력하시오"))
# print("%d년 %d월 %d일 입니다" % (year,month,day))

# # 소수점 2자리까지 출력하시오.
# a= 758.123456789
# print("%.2f" % a)

# # 10자리 공간을 만들고 빈공백은 0으로 채워 소수점 첫째자리까지 출력하시오
# b= 25.05
# print("%010.1f" % b)

# # 정수,실수,문자열로 출력하시오
# c= 150.15
# print(int(c))  # 소수점 삭제
# print(float(c))
# print(str(c))

# # 문자열을 20번 반복하여 출려하시오.
# d= "*"
# print(d*20)  # 문자열 반복연산자 # 문자열 연결연산자는 " + "

# 숫자 2개를 입력받아 사칙연산결과를 출력하시오.
# num1= int(input("정수1을 입력하시오"))
# num2= int(input("정수2를 입력하시오"))
# print("사칙연산결과는 다음과 같습니다.")
# print(" %d + %d = %d" % (num1,num2,num1+num2))
# print(" %d - %d = %d" % (num1,num2,num1-num2))
# print(" %d * %d = %d" % (num1,num2,num1*num2))
# print(" %d / %d = %d" % (num1,num2,num1/num2))


# 국어,영어,수학점수를 입력받아 합계,평균을 출력하시오.


# \t: 탭-사이띄움
# \n: 줄바꿈

print("학생성적프로그램")
print("-"*50)
print("이름\t국어\t수학\t영어\t합계\t평균")
print("-"*50)

name= input("이름을 입력하시오")
kor= int(input("국어점수를 입력하시오"))
eng= int(input("영어점수를 입력하시오"))
math= int(input("수학점수를 입력하시오"))
total= kor+eng+math
avg= (kor+eng+math)/3

name2= input("이름을 입력하시오")
kor2= int(input("국어점수를 입력하시오"))
eng2= int(input("영어점수를 입력하시오"))
math2= int(input("수학점수를 입력하시오"))
total2= kor2+eng2+math2
avg2= (kor2+eng2+math2)/3

print("-"*50)
print("입력하신 세과목의 합계와 평균은 다음과 같습니다")
print("-"*50)
print("이름\t국어\t수학\t영어\t합계\t평균")
print("%s\t%d\t%d\t%d\t%d\t%.2f" % (name,kor,eng,math,total,avg))
print("%s\t%d\t%d\t%d\t%d\t%.2f" % (name2,kor2,eng2,math2,total2,avg2))
print("-"*50)

















