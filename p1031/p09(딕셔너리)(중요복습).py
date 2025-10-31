# # 1:3, 2:1, 3:1, 4:2
# a_dic[1]= 1
# a_dic[2]= 1
# a_dic[3]= 1
# a_dic[4]= 1

a_list=[1,1,1,2,3,4,4]
a_dic={}

for i in a_list:
    if i not in a_dic:
        a_dic[i]=1
    else:
        a_dic[i]=a_dic[i]+1
print(a_dic)

        
# b_dic={}
# "홍길동",100
# b_dic["홍길동"]=100  # 딕셔너리 추가
# b_dic["홍길동"]=99  # 딕셔너리 수정
# print(b_dic)