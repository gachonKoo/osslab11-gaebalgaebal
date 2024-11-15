# tester.py

import geo.utils as utils

# 빗변 길이 계산 (a=3, b=4)
a, b = 3, 4
c = utils.pythagoras(a, b)
print('c =', c)

# 반지름 r=10인 원의 넓이 계산
r = 10
area = utils.circle(r)
print('area =', area)
