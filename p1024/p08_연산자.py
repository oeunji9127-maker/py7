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

# num1= int(input("정수1를 입력하시오."))
# num2= int(input("정수2를 입력하시오"))

# plus= num1+num2
# min= num1-num2
# X= num1*num2
# N1= num1/num2
# N2= num1//num2
# N3= num1%num2

# print("%d + %d = %d" % (num1,num2,plus))
# print("%d - %d = %d" % (num1,num2,min))
# print("%d * %d = %d" % (num1,num2,X))
# print("%d / %d = %.2f" % (num1,num2,N1))
# print("나눗셈 결과의 몫 = %d" % (N2))
# print("나눗셈 결과의 나머지 = %d" % (N3))

# 몫과 나머지를 이용해보기
# 780원을 동전으로 교환하려고 해요.
# 500원 동전 몇개, 100원 동전 몇개, 50원 동전 몇개, 10원 동전 몇개로 교환해야 할까요?
# 500원(1) 100(2) 50(1) 10(3)

have_money= int(input("본인이 가지고 있는 돈의 금액을 입력하세요."))
coin_500= have_money//500
min_500=have_money%500

coin_100= min_500//100
min_100= min_500%100

coin_50= min_100//50
min_50= min_100%50

coin_10= min_50//10
min_10= min_50%10

print("500원 동전: %d개, 100원 동전: %d개, 50원 동전: %d 10원 동전:%d" % \
(coin_500,coin_100,coin_50,coin_10))

##주의! %뒤에 %에 들어갈 변수를 적을 때 꼭 괄호()써주고 안에 넣을 것!!





 






