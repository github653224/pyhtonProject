"""
定义一个参数表示装饰器内部函数执行的次数
"""
import functools


def repeat(num):
    def my_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwwords):
            for i in range(num):
                print("wrapper of decorator")
                func(*args, **kwwords)
        return wrapper
    return my_decorator


@repeat(1)
def greet(*args, **kwwords):
    print(f"hello {args}")
    arg1, arg2 = args
    print(arg1)
    print(arg2)
    print(kwwords)


if __name__ == "__main__":
    greet("panxueyan", "xiaoniu", name="xiaomei", age=18)
    print(greet.__name__)


