# 모듈: 함수의 그룹
# 다른 파일의 모듈을 사용하려면, import 사용해야 가능
# import를 하면 모듈이름.함수명으로 호출해야 함

# 공식: import (모듈)
# import Func # Func 모듈을 사용하겠다는 뜻  # Func.py의 모든함수를 가져옴
# import random # random 모듈을 사용하겠다는 뜻

# import 모듈이름.함수명으로 사용
# Func.func1()
# random.sample()

# from 파일명 import 함수를 정의하면 파일명을 생략가능
# 모듈명 생략가능
# from (모듈명) import (함수,클래스)
# 덧셈,뺄셈,곱셈,나눗셈을 한 그룹에 묶어두면 (함수그룹)
# 유사한 함수들을 한그룹으로 묶어 분류해둔 것 (모듈: 여러함수가 들어있다)

# from 파일명.모듈명 import 변수,함수,클래스,*
# from 파일명 import 모듈명



# 모듈이름이 너무 길때 줄여 사용가능: as 별칭
# import random as r
# print(r.sample(1,46),6)



# 알아두면 좋은 모듈: 현재시간/날짜
# import datetime
# now= datetime.datetime.now()
# print(now)
# print(now.year) # year,month,day,hour,minute,second


# import time
# time.sleep(5)  # 5초동안 대기


# import math
# # dir: 모듈안에 모든 함수를 보여주는 명령어
# print(dir(math))  # math 모듈안에 모든 함수를 보여줌
# print(dir(r))  # random 모듈안에 있는 모든 함수를 보여줌

# from Func import func1

# 예제
# 수학공식
# from math import sin,cos,tan,floor,ceil

# floor 소수점버림, ceil 소수점올림
# print(floor(1.95))
# print(ceil(1.2))
# print(round(1.59))  # round 내장함수


