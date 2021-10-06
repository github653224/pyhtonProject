import functools 


def authenticate(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        request = args[0]
        if check_user_logged_in(request):
            return func(*args, **kwargs)
        else:
            raise Exception("Authentication failed")
    return wrapper

@authenticate
def post_comment(request):
    pass