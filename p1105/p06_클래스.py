class cal:
    __hour= 12  # 접근제한  # 데이터에 제한을 줄 수 있다
    minute= 30
    second= 20
    
    def setHour(self,hour):
        self.__hour= hour
    def getHour(self):
        return self.__hour
    
time= cal()
print(time.minute)
# print(time.__hour)  # 클래스내 변수에 직접 접근제한, 변수출력을 바로 할 수 없다!!
print(time.setHour(50))  # setHour()함수를 통해서 변수값을 재설정 할수있음
print(time.getHour) # getHour()함수를 통해서 클래스내 변수를 출력할수있음



class Car:
    # 클래스명 첫글자는 무조건 대문자로 작성한다
    
    # 생성자
    def __init__(self,color,speed):
        self.color= color
        self.speed= speed
    
    def upSpeed(self,speed):
        self.speed+=speed  # 지역변수
        return self.speed

# 클래스를 사용하려면(변수를 호출하거나 값을 이용하려면), 무조건 객체선언해야함

# 객체선언방법
# 참조변수= 클래스명()

c= Car("white",10)
# 값읽기 - 참조변수명.변수명
print(c.color)
print(c.speed)


# 값수정
# 참조변수.변수명= 값입력
c.color= "red"
print(c.color)


c2= Car("red",90)  # c1과 c2는 전혀 다른객체
print(c2.upSpeed(100))


