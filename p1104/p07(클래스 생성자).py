# 클래스
# 클래스내 변수,함수를 사용하려면 무조건 객체선언을 해야 사용할수 있음
# 객체선언: 참조변수= 클래스명

class Car:
    color= ""  # 전역변수
    speed= 0  # 전역변수
    
    # 생성자: 객체선언시 값을 바로 할당할수있게 해줌
    def __init__(self,color,speed):
        self.color= color  # self.변수명 시 없으면 클래스에 변수추가해줌
        self.speed= speed
        self.tire= 4  # 변수 자동생성
        
    
    # 클래스내 함수 첫매개변수로 self
    # 클래스내의 변수에 값을 재할당해서 다시 저장하고 싶을때 self를 작성
    def upSpeed(self,num):
        # 함수내 변수를 선택
        self.speed+=num
        
    def downSpeed(self,num):
        self.speed-=num


# 1. 객체선언후 값지정
        
# c1= Car()  # 객체선언 - 변수,함수를 사용
# # 사용방법: 변수 - 참조변수.변수명
# # 사용방법: 함수 - 참조변수.함수명
# print(c1.speed)
# c1.upSpeed(10)  # 클래스내 함수호출 - 참조변수.함수명()
# print(c1.speed)


# 2. 생성자를 통해 값지정 - 생성자를 사용해서 프로그램을 함
c2= Car("파랑",100)  # 생성자의 매개변수 개수를 맞춰야함
print(c2.color)
print(c2.speed)
c2.door= 5  # 클래스에 변수가 없으면 클래스에 자동으로 추가됨

# 속도 50으로 증가, 속도 30감소, 속도 100증가
# 속도를 출력하시오
# 색상 >> 파랑으로 변경하시오

# c1.upSpeed(50)
# c1.downSpeed(30)
# c1.upSpeed(100)
# print(c1.speed)
# c1.color= "파랑"
# print(c1.color)