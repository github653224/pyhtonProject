"""
函数内部嵌套函数并把内部函数返回，即函数闭包
内部函数接受参数为 函数
"""

def my_decorator(func):
    def wrapper():
        print("wrapper of decorator")
        func()
    return wrapper

def greet():
    print("hello world")



if __name__ == "__main__":
    greet_hello = my_decorator(greet)
    greet_hello()



