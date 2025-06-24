


def primer(a, b, c = None):
    print(a, b, c)


def for_primer(*args, **kwargs):
    primer(*args, **kwargs)


for_primer(1, 2, 3)