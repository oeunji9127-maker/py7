# {키:값}
stu_dic= {"num":1, "name":"홍길동", "kor":100}

# dic 추가
stu_dic["eng"]= 100

# dic 수정
stu_dic["kor"]= 90

# dic 삭제
# del stu_dic["name"]

# key 출력
print(stu_dic.keys())
print(list(stu_dic.keys()))
for k in stu_dic.keys():
    print(k)
    # stu_dic= {"num":1, "name":"홍길동", "kor":100}
    # sut_dic의 키만 출력
    # 출력

for k in stu_dic.keys():
    print("{}:{}".format(k,stu_dic[k]))

# values 출력
print(stu_dic.values())
print(list(stu_dic.values()))
for i,v in enumerate(stu_dic.values()):
    print("{},{}".format(i,v))
    
# items() 출력: key와 value 모두 출력
print(stu_dic.items())
print(list(stu_dic.items()))
for k,v in stu_dic.items():
    print("{}:{}".format(k,v))
    
# 딕셔너리 출력
print(stu_dic["num"])
print(stu_dic["name"])
print(stu_dic["kor"])
# print(stu_dic["math"])  # 없는 키 출력시 에러발생
print(stu_dic.get("math"))  # none으로 출력됨
# get()함수는 함수이므로 "괄호"안에 키를 입력해야 한다 

names= {"홍길동":100, "유관순":80, "이순신":90, "김구":99, "강감찬":95, }

import operator
# reverse=True: 역순정렬,  reverse=False: 순차정렬
# itemgetter(0):키,  itemgetter(1):값 
names2= sorted(names.items(),key=operator.itemgetter(0),reverse=True)

# 리스트 정렬
a_list= [1,2,3,4]
# sort(): 해당리스트 자체를 정렬
# sorted(): 다른변수에 정렬된 값 저장가능, 원본보존
b_list=sorted(a_list)
print(b_list)

# 리스트 최대값, 최솟값
print(max(a_list))
print(min(a_list))

