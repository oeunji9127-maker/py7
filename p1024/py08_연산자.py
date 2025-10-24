# 연산자
# +: 더하기, =: 빼기, *:곱하기, /:나누기
# //:몫, %:나머지, **:제곱

# print(10+20)
# print(10-20)
# print(10*20)
# print(10/20)

# print(10/3)   #3.33333
# print(10//3)  #3
# print(10%3)   #1 나머지
# print(10**3)  #10*10*10=1000

# 퀴즈: 두수를 입력받아 위의 연산을 출력하시오.

num1= int(input("정수1를 입력하시오."))
num2= int(input("정수2를 입력하시오"))

plus= num1+num2
min= num1-num2
X= num1*num2
N1= num1/num2
N2= num1//num2
N3= num1%num2

print("%d + %d = %d" % (num1,num2,plus))
print("%d - %d = %d" % (num1,num2,min))
print("%d * %d = %d" % (num1,num2,X))
print("%d / %d = %.2f" % (num1,num2,N1))
print("나눗셈 결과의 몫 = %d" % (N2))
print("나눗셈 결과의 나머지 = %d" % (N3))






