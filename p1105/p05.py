stu_list = [
    {'stuno':10101,'name':'홍길동','kor':80,'eng':80,'math':80,\
        'total':240,'avg':80.00,'rank':0},
    {'stuno':10102,'name':'유관순','kor':90,'eng':90,'math':90,\
        'total':270,'avg':90.00,'rank':0},
    {'stuno':10103,'name':'이순신','kor':100,'eng':100,'math':100,\
        'total':300,'avg':100.00,'rank':0},
]

str1= "{'stuno':10101,'name':'홍길동','kor':80,'eng':80,'math':80,\
        'total':240,'avg':80.00,'rank':0}"
        
print(str1)

import ast
str_dic= ast.literal_eval(str1)