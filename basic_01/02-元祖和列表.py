import timeit 
from collections import namedtuple


def func():
    for i in range(10):
        print(i)


# 使用timeit里的Timer类可以测试函数func的性能, 以下运行func函数10次返回其执行的时间
# 可以使用timeit进行批量造数据
run_time = timeit.Timer(func).timeit(10)
print(run_time)

# 这里运行10000000次
# run_time2 = timeit.timeit(func)
# print(run_time2)

# 命名元祖
student_info = namedtuple('student_info', ('name', 'age', 'gender'))
tu = student_info('panxuey', 18, 'male')
print(tu)
print(tu.name)
print(tu.age)
print(tu.gender)
# type元类
print(type(student_info))
print(type(tu))