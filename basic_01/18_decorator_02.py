import logging 


logging.basicConfig()

def my_decorator(func):
    def wrapper():
        logging.log(1, "日志打印开始")
        print("wrapper of decorator")
        func()
    return wrapper


@my_decorator
def greet():
    print("hello world")


if __name__ == "__main__":
    greet()


