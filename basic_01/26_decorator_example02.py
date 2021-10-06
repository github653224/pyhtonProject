import time
import functools 


def _log_execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        print(f'{func.__name__} took {(end - start)*1000} ms')
        return res
    return wrapper

@_log_execution_time
def calculate_similarity(times):
    tmp_list = list()
    for i in range(10000):
        tmp_list.append(i)


if __name__ == "__main__":
    calculate_similarity(5)