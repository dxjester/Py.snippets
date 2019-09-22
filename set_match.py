# 1.1.4
def find_common_inds(d1, d2):
    assert type(d1) is dict and 'inds' in d1 and 'vals' in d1
    assert type(d2) is dict and 'inds' in d2 and 'vals' in d2
    d1_val = d1['inds']
    d2_val = d2['inds']
    matching = list(set(d1_val) & set(d2_val))
    return matching
