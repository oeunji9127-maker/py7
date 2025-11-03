# return: 함수를 호출한 곳으로 값을 전달할 때 사용
def cal(a,b): # 매개변수는 꼭 타입을 일치시켜야함
    return (a+b) # 함수끝을 만나면 함수가 종료됨
    # return # return을 만나면 함수가 종료됨

num1= cal(10,5)
num2= cal(2,7)
num3= cal(3,5)

# 3개의 계산 더하기 빼기를 구하시오
print(num1+num2+num3)
print(num1-num2-num3)

# print(cal(2,1)) # return값을 받아 3을 출력