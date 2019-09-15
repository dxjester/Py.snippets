# a program designed to convert a string with a base parameter to a number

def eval_strint(s, base=2):
    assert type(s) is str
    assert 2 <= base <= 36
    cast = int(s, base) # convert to interger
    return cast
