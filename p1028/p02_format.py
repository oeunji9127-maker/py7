# year= 2025
# month= 10
# day= 28
# 2025년 10월 20일
# print("%d년 %d월 %d일" % (year,month,day))


# format() 함수
# 변수를 파일형태로 저장하는 함수
# 포멧함수 정말 많이 사용하는 함수이다. 잘 알고 있어야 한다

# "{}".format()
# date1= "{}년 {}월 {}일".format(year,month,day)
# print(date1)

# b= 12.3456789
# print("{:.2f}".format(b))
 
 
# list타입 format함수사용 

bank= [1,"홍길동",100000]
# 1번 홍길동 100,000원

# format함수를 사용해서 출력하시오
cus1= "{}번 {} {:,}원".format(*bank)
print(cus1)

name= "유관순"
rank= 3
result= 98.123456
# 이름: 유관순, 단계: 3, 성공률: 98.12
print("이름:{}, 단계:{}, 성공률:{:.2f}".format(name,rank,result))
# f함수
print(f"이름:{name}, 단계:{rank}, 성공률:{result:.2f}")




 







