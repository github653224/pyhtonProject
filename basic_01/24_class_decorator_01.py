class Count:
    def __init__(self, func) -> None:
        self.func = func
        self.num_calls = 0
    
    def __call__(self, *args, **kwds):
        self.num_calls += 1
        print(f'num of calls is: {self.num_calls}')
        return self.func(*args, **kwds)

@Count
def example():
    print("hello world")


if __name__ == "__main__":
    example()
    example()