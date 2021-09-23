"""
带有不定长参数和不定类型参数的装饰器
"""
def my_decorator(func):
    def wrapper(*args, **kwwords):
        print("wrapper of decorator")
        func(*args, **kwwords)
    return wrapper


@my_decorator
def greet(*args, **kwwords):
    print(f"hello {args}")
    arg1, arg2 = args
    print(arg1)
    print(arg2)
    print(kwwords)


if __name__ == "__main__":
    greet("panxueyan", "xiaoniu", name="xiaomei", age=18)


