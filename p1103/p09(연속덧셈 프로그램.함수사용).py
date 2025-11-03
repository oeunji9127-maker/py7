# def cal() 함수생성
# 1,10까지의 합이 출력되도록 구성하시오.
# cal(1,10)

# 함수정의
def cal(num1,num2):
    sum=0
    for i in range(num1,num2+1):
         sum+=i
    print(sum)
        
num1= int(input("숫자1을 입력하세요>> "))
num2= int(input("숫자2을 입력하세요>> "))
cal(num1,num2)
    
cal(2,10)
cal(5,9)
cal(11,20)


# 함수를 사용 cal(매개변수 3개)
# 두수와 +,-,*,/ 4개중에 입력받아
# 두수의 결과를 출력하시오

# def cal(num1,num2,str1):
#     if str1=="+":
#         return num1+num2
#     elif str1=="-":
#         return num1-num2
#     elif str1=="*":
#         return num1*num2
#     elif str1=="/":
#         return num1/num2
    
# num1= int(input("숫자를 입력하세요>> "))
# num2= int(input("숫자를 입력하세요>> "))
# str1= input("원하는 사칙연산 기호를 입력하세요(+,-,*,/)>> ")
# print(cal(num1,num2,str1))




# 입력한 글자를 입력한 숫자만큼 반복출력
# "안녕하세요"입력/ "3"입력
# 안녕하세요가 3번 반복해서 출력

# 함수를 사용하지 않았을때
# str1= input("글자를 입력하세요>> ")
# num= int(input("반복횟수를 입력하세요>> "))
# for i in range(num):
#     print(str1)
    
# # 함수를 사용했을때
# def s_print(str1,num):
#     for i in range(num):
#         print(str1)
# s_print(str1,num)



    
    