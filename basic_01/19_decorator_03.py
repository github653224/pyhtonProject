"""
带有一个参数的装饰器
"""
def my_decorator(func):
    def wrapper(arg):
        print("wrapper of decorator")
        func(arg)
    return wrapper


def greet(arg):
    print(f"hello {arg}")


if __name__ == "__main__":
    decorator = my_decorator(greet)
    decorator("panxueyan")


