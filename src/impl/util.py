

def fail(cond=True, msg=''):
    if cond:
        raise Exception(msg)


def lists_values_to_tuples(dct):
    for k,v in dct.copy().items():
        if isinstance(v, list):
            dct[k] = tuple(v)

            
class classproperty(object):
    def __init__(self, function):
        self.function = function

    def __get__(self, obj, owner):
        return classmethod(self.function).__get__(None, owner)()

