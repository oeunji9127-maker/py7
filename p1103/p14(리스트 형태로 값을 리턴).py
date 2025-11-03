# 파이썬 여러개 리턴가능
# 리턴형태: 튜플타입
# 리스트형태로 값을 리턴하면, 여러개의 값을 리턴할 수 있음


# 매우중요!! 리스트를 사용해서 여러개 리턴, 리턴값은 1개
def func():
    a_list=[10,20,30]
    return a_list

a_list=func()
print(a_list)


def cal():
    return 10,20,30 # 파이썬의 특징: 여러개 리턴가능
a,b,c= cal()
print(a,b,c)
