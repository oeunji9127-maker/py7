# 매우중요!!

# lambda() 함수: 함수를 한줄로 간단히 만든 것
# lambda() 함수 : lambda(매개변수:수식)
# map()함수: 여러개를 함수적용시킬때 사용/리스트= map(함수,리스트)
# 하지만 복잡한 수식은 기본함수정의를 통해 만들어야한다

# 방법1. print(10+20)


# 방법2. 
# def add(a,b):
#     return a+b
# print(add(10,20))


# 방법 3.
# 함수축약 lambda()
# def선언하는 것과 같음
# lambda 매개변수 : 함수수식

# result: 함수명(값,값)
# add= lambda a,b: a+b
# print(add(10,20))


# map()함수
# map(함수,리스트)
# m_list= list(map(cal,my_list))

# 결과값리스트= map(함수,리스트)
# 결과값리스트: map타입의 객체 형태이므로 >> list타입으로 변경해야함
# map(함수,리스트)
# m_list= list(map(cal,my_list))


# my_list=[1,2,3,4,5]
# my_list= ["1","2","3","4","5"]
# my_list=["0"]*10
# m_list= list(map(lambda a:int(a),my_list))
# print(m_list)


# def cal (a):
#     return a%2
# map(cal,my_list)



# 기본함수 사용
# 함수선언,함수정의
# def add(a,b):
#     return a+b
# print(add(10,20))

# 함수축약 lambda()
# def선언하는 것과 같음
# lambda 매개변수 : 함수수식

# result: 함수명(값,값)
# add= lambda a,b: a+b
# print(add(10,20))


# 파이썬만의 특징: 함수 안에 함수가 들어올 수 도 있다
# 내부함수: 함수 내에 함수

