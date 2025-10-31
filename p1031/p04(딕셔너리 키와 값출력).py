# "num":1,"name":"홍길동","kor":100 딕셔너리 추가해서
# 키: 값으로 모두 출력하시오

# stu_dic={}
# stu_dic["num"]= 1
# stu_dic["name"]="홍길동"
# stu_dic["kor"]= 100

# for k,v in stu_dic.items():
#     print("{}:{}".format(k,v))

# for k in stu_dic.keys():
#     print("{}:{}".format(k,stu_dic[k]))
    
# for v in stu_dic.values():
#     print("값: {}".format(v))
    
stu_list= [
{"no":1,"name":"홍길동","kor":100},
{"no":2,"name":"유관순","kor":90},
{"no":3,"name":"홍길동","kor":80},
]
## 3번째에 있는 홍길도 kor를 50점으로 변경하시오
print(stu_list[2])
stu_list[2]["kor"]=50

stus= {"num":3, "name":"홍길동", "kor":100}
# kor를 50점으로 변경하세요
stus["kor"]=50

a_list= [3,"이순신",90]
# 90을 50점으로 변경하세요
a_list[2]=50
print(a_list)


    
    
    