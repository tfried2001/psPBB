import functools

def noop(f):
    @functools.wraps(f)
    def noop_wraper():
        return f()

    # noop_wraper.__name__ = f.__name__
    # noop_wraper.__doc__ = f.__doc__
    return noop_wraper

@noop
def hello():
    '''Print a well-known message.'''
    print("Hello, world!")