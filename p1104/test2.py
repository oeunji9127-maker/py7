titles = ['번호','이름','국어','영어','수학','합계','평균',"등수"]
stu_list = [
    [10101,'홍길동',80,80,80,240,80.00,0],
    [10102,'유관순',90,90,90,280,90.00,0],
    [10103,'이순신',100,100,100,300,100.00,0]
]

# 등수처리
for s1 in stu_list:
    for s2 in stu_list:
        if s1[5]<s2[5]:
            count+=1
s1[7]=count

print("-"*70)
print(*titles,sep="\t")
for stu in stu_list:
    print(*stu,sep="\t")
print("-"*70)

# 끝




    
    