# 함수: 특정명령어를 집합 - **반복을 제거, 유지보수 쉽게, 코드량을 줄임

# 함수의 형태
# def 함수명(매개변수):
#     pass

# 함수호출
# 함수명()

def calculate(a,b): # 함수정의
    # 매개변수: 값을 전달하는 변수
    print("더하기",a+b)
    print("빼기",a-b)
    print("곱하기",a*b)
    print("나누기",a/b)
    
a,b= 10,2
calculate(a,b) # 함수호출
a,b= 5,3
calculate(a,b)
a,b= 2,1
calculate(a,b)



# a,b= 10,2
# print("더하기:",a+b)
# print("빼기:",a-b)
# print("곱하기:",a*b)
# print("나누기:",a/b)

# a,b= 5,3
# print("더하기:",a+b)
# print("빼기:",a-b)
# print("곱하기:",a*b)
# print("나누기:",a/b)


