stus= [1,"홍길동",100,90,80]
# 국어,영어,수학점수를 입력받아, return을 적용

def sum(kor,eng,math):
    return kor+eng+math

def avg(kor,eng,math):
    return (kor+eng+math)/3

stus.append(sum(stus[2],stus[3],stus[4]))
print(stus)
stus.append(avg(stus[2],stus[3],stus[4]))
print(stus)


# stus= [1,"홍길동",100,90,80]
# 함수를 제대로 구성해서 stus 리스트를 아래와 같이 변경하시오    
# stus= [1,"홍길동",100,90,80,270,90.00] 



# 매개변수 개수는 호출하는 변수의 개수와 동일해야함
# 매개변수 타입도 호출하는 변수타입과 일치해야함

# 가변 매개변수
# def add(a,b,*c): # 변수 앞에 *를 붙이면 가변매개변수가 된다
#     sum= a+b
#     for i in c: # c가 여러개 가능
#         sum=sum+i
#     return sum
# print(add(1,2,3,4,5,6,7,8,9))


# def print_str(a,b,*c):
#     print(a)
#     print(b)
#     for i in c:
#         print(i)
        
# print_str("안녕","사과","홍길동","점수",100)
# 가변매개변수는 들어와도 되고, 들어오지 않아도 된다
