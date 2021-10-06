import functools


def validation_check(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        pass

@validation_check
def neural_network_training(param1, param2):
    pass