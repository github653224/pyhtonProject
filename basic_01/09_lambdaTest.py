import re 
from functools import reduce


# map纯函数使用场景：  对列表中的所有元素进行平方操作
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared = map(lambda x: x**2, l)
print(list(squared))

# filter纯函数使用场景：  返回列表中所有偶数
oushu = filter(lambda x: x%2==0, l)
print(list(oushu))

test_str1 = "I am boy, . I love code !, .. I dd "
test_str1 = re.sub(r'[^\w]', ' ', test_str1)
print(test_str1)
test_str1 = test_str1.split(' ')
print(test_str1)
result1 = filter(None, test_str1)
print(list(result1))

# reduce 纯函数使用场景：它通常用来对—个集合做一些累积操作。
"""
function同样是一个函数对象，规定它有两个参数，表示对 
iterab|e中的每个元素以及上次调用后的结果，运用 function进行计算，所以最后返回的是一个单独的数值
"""

l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 计算列表元素的乘积
result2 = reduce(lambda x,y: x*y, l2)
print(result2)

# 计算列表元素的相加
result3 = reduce(lambda x,y: x+y, l2)
print(result3)

