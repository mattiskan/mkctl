

def fail(cond=True, msg=''):
    if cond:
        raise Exception(msg)


def lists_values_to_tuples(dct):
    for k,v in dct.copy().items():
        if isinstance(v, list):
            dct[k] = tuple(v)

    
