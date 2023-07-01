"""
Декоратор - в питоне - функциональный декоратор
"""


import time


def time_it(func):
    def wrapper():
        start = time.time()
        res = func()
        end = time.time()
        print(f"{func.__name__} took {int((end-start)*1000)} ms" )
        return res
    return wrapper


@time_it # функциональный декоратор
def some_op():
    print("start")
    time.sleep(1)
    print("done")
    return 1


if __name__ == "__main__":
    some_op()
    #time_it(some_op)()
