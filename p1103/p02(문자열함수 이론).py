# 문자열 함수

# 영문 대문자 소문자 변경함수
# **upper(): 대문자로 변경
# **lower(): 소문자로 변경
# **title(): 첫글자를 대문자로 변경
# swapcase():대문자를 소문자로, 소문자는 대문자로

# 함수를 사용할 때만! 일시적으로 대문자로 변경됨
# 데이터가 대문자로 변환되는 것은 아니다

# a= "abc"
# print(a.upper()) 이 형태로 사용된다. 기억!

# a= "abc"
# a.upper()
# print(a)
# # 이렇게 사용할 수 없다는 뜻! 데이터가 변환되는 것이 아니다!



# 문자열 찾기
# **count(): 해당하는 문자개수
# **find(): 해당문자 위치검색/해당문자 없을때 -1을 리턴
# **index(): 해당문자 위치검색/해당문자 없을때 에러
# startswith(): 해당문자로 시작되는지 확인/True,False로 출력 
# **endswith(): 해당문자로 끝나는지 확인/True,False로 출력



# 공백제거: stip
# **strip(스트립): 앞뒤 공백제거, 문자사이 공백은 제거되지않음
# **replace(" ",""): 공백을 제거하는 용도로 쓰임
# rstip: 오른쪽 공백제거
# lstrip: 왼쪽 공백제거



# replace: 문자열 변경
# replace: (변경하려는 문자, 변경 후의 문자)
# replace: ("홍길동","홍길자"):  홍길동을 홍길자로 변경하려고한다


# **isdigit(): 숫자인지 확인
# isalpha(): 문자(영문자,한글)인지 확인
# isalnum(): 문자(영문자,한글), 숫자인지 확인
# islower(): 소문자 확인
# isupper(): 대문자 확인


# split(): 문자열 분리: 타입은 리스트로 분리해줌
# 리스트 타입>> 문자열을 분리해서 리스트안에 넣어준다

# join(): 문자열 결합
# ss= "%"
# print(ss.join("파이썬"))

# map(): 리스트를 입력받아 처리하는 함수
# map(function 함수부분,리스트 데이터)



# 국어점수를 입력하세요

# while True:
    
#     kor= input("국어점수를 입력하세요>> ")
#     if kor.isdigit(): # 이즈디짓, 숫자인지 확인하는 작업
#         print(int(kor))
#         break
#     else: print("숫자가 아닙니다. 다시 입력하세요")
# print("입력된 국어점수 값:{}".format(kor))



# def multi(x):
#     return x**2

# a= [1,2,3]
# b= list(map(multi,a))
# print(b)

# a= ["100","90","80"]
# b= list(  map(int,a)  )  # map타입 객체로 저장됨, 따라서 리스트 타입으로 변경해야함


# a= ["100","90","80"]
# b= []
# for i in a:
#     print(b.append(int(i)))
# print(a)
# print(b)    
    
# a= "홍길동,100,100,100,300"
# titles= ["번호","이름","국어","영어","수학","합계","평균"]
# a_list= a.split(",")
# print(*titles,sep="\t")
# print("-"*50)
# print(*a_list,sep="\t")
# ,(쉼표)를 기준으로 문자열을 분리하고 싶다

b= "홍길동 유관순 이순신 김구"
b_list= b.split(" ")
print(b_list)


# # print(sep:변수사이사이 모두적용, end:마지막에 한번적용)
# print(*titles,sep="/",end="**")
# print(*titles,sep="\t")  # sep 사이 간격출력


# a= "홍길동은 키가 180, 몸무게가70, 홍길동은 사는 곳이 서울입니다."
# a.replace("홍길동","홍길자")
    
# # input1= input("이름을 입력하세요>> ").stip()  # 공백제거
# # if "홍길동"==input1:
# #     print("맞습니다",input1)
# # else:
# #     print("틀립니다",input1)

# # c= "abc.exe"
# # print(c.endswith("exe")) >>True

# # a= "1111112233566898"
# # print(a.count("1"))  # 1이 6개 존재

# # find(): 해당문자 위치검색, 해당문자 없을때 -1을 리턴
# # 해당문자가 없다고 에러가 나지 않기 때문에 index보다 find를 더 많이 사용함

# b= "프로그램 중 파이썬 사용자가 제일 많습니다.(파이썬 프로그래밍)"
# print(b.find("파이썬"))  # 7  # 왼쪽에서 파이썬 위치검색, 없을 때 -1을 리턴
# print(b.rfind("파이썬"))  # 25  # 오른쪽에서 파이썬 위치검색
# print(b.index("파이썬"))  # 파이썬 위치검색, 없을 때 에러
