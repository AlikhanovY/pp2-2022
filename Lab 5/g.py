def snaketocamel(a):
    import re
    return ''.join(x.capitalize() or '_' for x in a.split('_'))
a=input()
print(snaketocamel(a))