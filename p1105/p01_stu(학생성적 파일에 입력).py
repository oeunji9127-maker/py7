stu_list = [
    {'stuno':10101,'name':'홍길동','kor':80,'eng':80,'math':80,\
        'total':240,'avg':80.00,'rank':0},
    {'stuno':10102,'name':'유관순','kor':90,'eng':90,'math':90,\
        'total':270,'avg':90.00,'rank':0},
    {'stuno':10103,'name':'이순신','kor':100,'eng':100,'math':100,\
        'total':300,'avg':100.00,'rank':0},
]

stu_str=""
for i in range(len(stu_list)):
    stu_str+= f"{stu_list[i]["stuno"]},{stu_list[i]["name"]},\
    {stu_list[i]["kor"]},{stu_list[i]["eng"]},{stu_list[i]["math"]},\
    {stu_list[i]["total"]},{stu_list[i]["avg"]},\
    {stu_list[i]["rank"]}\n"

       
with open("C:/down/aaa.txt","w",encoding="utf-8") as f:
    f.write(stu_str)
    print("입력이 완료되었습니다!")
    


