# 변수 = 파일을 저장하는 공간
# 타입 - 숫자(정수,실수),문자열,불(참,거짓)
# 문자열+숫자: 불가능/프로그램에 에러가 난다.


num= None
print(type(num))
# num에 아무값도 넣지 않았음을 표현
num= 100
print(type(num))

astr= 100
astr= True
astr= "안녕" #마지막값이 타입으로 지정됨
print(type(astr)) #타입이 문자열로 지정됨

result= 100
result2= result
result= result+200
result= result+200
print(result2) #값은 얼마일까요?
#result는 300, result2는 100이다.
#각각의 변수를 각각의 다른 공간이라고 생각해라.




