import os

# 파일복사 - 문자읽기:r, 문자쓰기:w / 파일읽기: rb, 파일쓰기: wb
f1= open("C:/down/nct.jpg","rb") # rb: 파일읽기
f2= open("C:/aaa/nct.jpg","wb") # rb: 파일읽기

while True:
    nctfile= f1.read(1) # 파일읽기
    if not nctfile: break
    f2.write(nctfile)
    
f1.close()
f2.close()
print("복사완료!!")



# whit open 파일입출력
with open("C:/down/aaa.txt","r",encoding="utf-8") as f:
    while True:
        txt= f.readline()
        if txt=="":break
        print(txt.strip())
# whit open을 쓰게 되면,
# f.close()가 자동으로 입력됨


# f= open("C:/down/aaa.txt","r",encoding="utf-8")
# while True:
#     txt= f.readline()
#     if txt=="": break
#     print(txt.stip())
# f.close()


# --------------------------------------------------
# a: 추가모드
f= open("C:/down/ccc.txt","a")
for i in range(5):
    f.write(f"안녕하세요. {i}\n")
    
f.close()
print("완료!")


# -------------------------------------------------
# w: 쓰기모드: 안에 있는 모든 것을 지우고 쓰기, 새로쓰기
# a: 추가모드: 안에 있는 것을 그대로 두고 마지막에 추가해서 쓰기
# f= open("C:/down/ccc.txt","w") # 파일이 없으면 w:모드 파일이 생성
# f= open("C:/down/ccc.txt","a") # 파일이 있으면 추가모드를 사용해라
# stu_data=""
# for i in range(3):
#     txt= input("글자를 입력하세요>> \n")
#     stu_data+=txt+"\n"

# f.write(stu_data)
# f.close()
# print("완료!")

# -------------------------------------------------
# 1. 통로(stream): 파일열기
# r:읽기모드, w:쓰기모드, a:추가모드
# f= open("C:/down/aaa.txt","r",encoding="utf8")

# read(한바이트씩 읽어오기), readline(한줄씩 읽어오기), readlines(전체 읽어오기)

# 1. readline(): #1줄씩 가져오기
# while True:
#   txt= f.readline()
#   if txt=="":break
#   print(txt,end="") # print완료후 줄바꿈을 해줌

# 2. readlines() # 1줄씩 리스트에 담아서 가져옴
# txt_list= f.readlines() # 1줄씩 리스트에 담아줌
# for txt in txt_list:
#     print(txt,end="")



