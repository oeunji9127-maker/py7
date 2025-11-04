class Student:
    # 생성자 - 객체선언시 바로 실행되는 함수
    def __init__(self,stunum,name,kor,eng,math):
        # 클래스에서 사용하는 전역변수 = 함수내에서 사용하는 지역변수
        self.stunum= stunum
        self.name= name
        self.kor= kor
        self.eng= eng
        self.math= math
        self.total= kor+eng+math
        self.avg= self.total/3
        self.rank= 0
    
    # 합계
    def sum(self):
        self.total= self.kor+self.eng+self.math
    
        
s= Student(10101,"홍길동",100,100,100) # 클래스선언, 객체선언
print("국어: ",s.kor) # 국어점수 100
print("합계: ",s.total) # 합계 300
s.kor=90 # 국어점수 90으로 변경
s.sum() # 함수호출후 수식처리
print(s.total) # 합계 290= 90+100+100

