# utilize the join function
def strcat_list(L):
    assert type(L) is list
    "".join(L)
    return "".join(L[::-1]) 
