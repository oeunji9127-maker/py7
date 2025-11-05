class Student:
    
    def __init__(self,stunum,name,kor,eng,math):
        self.stunum= stunum
        self.name= name
        self.kor= kor
        self.eng= eng
        self.math= math
        self.total= kor+eng+math
        self.avg= self.total/3
        self.rank= 0
    
    # 객체,참조변수를 출력하면 값이 아닌 주소값이 출력됩니다.
    # 주소값이 아닌 값을 출력하고 싶기 때문에 __str__함수를 실행해 값을 출력합니다
    # 참조명.함수명으로 적어 출력하는 방식이 번거로우니
    # __str__함수를 만들면, 클래스를 적으면 주소값이 아닌 값이 바로 출력되게끔 만든것   
    
    def __str__(self):
        return(f"{self.stunum}\t{self.name}\t{self.kor}\t\
            {self.eng}\t{self.math}\t{self.total}\t{self.avg:.2f}\t\
            {self.rank}\t")
        
        
        
    def stu_total(self):
        self.total= self.kor + self.eng + self.math
        
    def stu_avg(self):
        self.avg= self.total/3

class Students:
    stu_list=[]
    titles= ["번호","이름","국어","영어","수학","합계","평균"]
    
    def print(self):0.
        print("-"*50)
        print(" "*10,"[ 학생성적프로그램 ]")
        print("-"*50)
        print(*self.titles,sep="\t")
        print("-"*50)
        for stus in self.stu_list:
            print(stus)
        print()
    
    def add(self,student):
        self.stu_list.append(student)
        




        

# stus= Student()

# stus.add(Student(10101,"홍길동",100,100,100))
# stus.add(Student(10102,"유관순",100,90,90))
# stus.add(Student(10103,"이순신",100,80,80))

# print(Student(10101,"홍길동",100,100,100))
# print(Student(10102,"유관순",100,90,90))
# print(Student(10103,"홍길동",100,80,80))

   
