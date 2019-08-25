# remove a value 'x' from a list of values
def remove_all(L, x):
    assert type(L) is list and x is not None
    copy = L.copy()
    while x in copy:
        copy.remove(x)
    return(copy)
