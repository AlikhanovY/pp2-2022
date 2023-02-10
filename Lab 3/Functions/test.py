def histogram(v):
    dot = '*'
    for val in v:
        if val != 0:
            dot = dot * val
        else:
            dot = ''
        print(dot)
        dot = '*'