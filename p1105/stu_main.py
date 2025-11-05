# 파일읽어오기


stu_list=[]
with open("C:/down/aaa.txt","r",encoding="utf-8") as f:
    while True:
        txt=f.readline()
        if txt=="":break
        t_list= txt.strip().split(",")
        # 문자열 >> 딕셔너리 타입으로 변경해주는 함수
        import ast
        t_dic= ast.literal_eval(txt)
        
        
        # 딕셔너리 형태변경
        t_dic= {"stuno":int(t_list[0]),"name":t_list[1],"kor":int(t_list[2]),\
        "eng":int(t_list[3]),"math":int(t_list[4]),"total":int(t_list[5]),\
        "avg":float(t_list[6]),"rank":t_list[7]}
        stu_list.append(t_dic)
print(stu_list)

# 파일 >> 리스트[딕셔너리타입] >> 파일
stu_str=""
for i in range(len(stu_list)):
    stu_str+= f"{stu_list[i]["stuno"]},{stu_list[i]["name"]},\
    {stu_list[i]["kor"]},{stu_list[i]["eng"]},{stu_list[i]["math"]},\
    {stu_list[i]["total"]},{stu_list[i]["avg"]},{stu_list[i]["rank"]}\n"

with open("C:/down/aaa.txt","w",encoding="utf-8") as f:
    f.write(stu_str)
    print("입력이 완료되었습니다!")
    
    
        