## num,num2 2개를 입력받아 숫자타입으로 변경후,
# 사칙연산 결과를 출력하시오.
###int(num)

###이것만은 기억하자!
#변수를 지정하지 않고, input만 적으면 입력만 된다. 변수에 입력한 값을 저장해야한다.
#입력한 값을 바로 출력하고 싶을 때: print(input())
###print(input())

num= input("숫자를 입력하세요")
num2= input("숫자를 입력하세요")
print("덧셈값: ",int(num)+int(num2))
print("뺄셈값: ",int(num)-int(num2))
print("곱셈값: ",int(num)*int(num2))
print("나누기값: ",int(num)/int(num2))

###이것만은 기억하자!!
#input()함수는 문자열이므로 "사칙연산"을 하고 싶다면 자료의 타입을 바꿔줘야한다.

