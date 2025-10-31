a_dic= {"no":1,"name":"홍길동","kor":100}
# 국어점수를 입력하세요
# print(a_dic["kor"])
# print(a_dic["kor1"])      # 없는 키값 입력시 에러


# 딕셔너리의 .get()함수
print(a_dic.get("kor1"))  # 없는 키값 입력시 None타입으로 출력됨


# 딕셔너리의 keys()
print(a_dic.keys())
a_list= list(a_dic.keys())
print(a_list[1])  # name출력

# 딕셔너리 values()
print(a_dic.values())
b_list=list(a_dic.values())
print(b_list)

# 딕셔너리 items(): 키와 값을 동시에 가져옴
# 키와 값을 리스트에 담아 리스트안에 리스트를 만든다 (2차원리스트)
print(a_dic.items())
c_list= list(a_dic.items())
print(c_list)


a_dic= {"no":1,"name":"홍길동","kor":100}
if "kor" in a_dic:
    print("키가 존재합니다")
else: print("키가 존재하지 않습니다") 


# stu_list={name:'홍길동',kor=100,eng=100,math=100}
# 딕셔너리변수= {키1:값1, 키2:값2, 키:값3......}

# 딕셔너리 생성
# list1= [1,2,3]
# dic1= {1:'1',2:'b',3:'c'}
# dic2= {"no":1, "name":"홍길동", "class":3}
# print(dic1)
# print(dic2)

# 리스트 추가: append,insert,extend
# 딕셔러리 추가: 없는 키와 값을 입력하면 됨

stu= {'학번':1, '이름':'홍길동', '학과':'컴퓨터공학과'}
stu['연락처']= '010-8698-9127'  # 딕셔너리 추가

# 딕셔너리 수정
stu['이름']= '홍길자'
print(stu)
# 키는 수정할 수 없다, 값만 수정가능

# 딕셔너리 삭제
del stu['이름']
print(stu)

