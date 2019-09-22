# 1.1.2
def compress_vector(x):
    d = {'inds': [], 'vals': []}
    for loc, value in enumerate(x):
        if value != 0.0:
            d['inds'].append(loc)
            d['vals'].append(value)
    return d
