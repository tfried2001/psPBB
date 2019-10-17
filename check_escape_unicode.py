def check_unicode_conv(func):
    def convert_unicode(*args, **kwargs):
        return ascii(func(*args, **kwargs))
    return convert_unicode

@check_unicode_conv
def print_unicode():
    return 'ætna'
