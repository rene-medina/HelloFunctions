def func(p1, p2, *args, k, **kwargs):
    print("Parameters must be defined and used in the following sequence:")
    print()
    print("For example a call to func(1, 2, 3, 4, 5, k=6, ke1=7, key2=8), where")
    print("func(p1, p2, *args, k, **kwargs)  returns:")
    print()
    print("1.- Positional-or-Keyword arguments p1: {0}, p2: {1}".format(p1, p2))
    print("2.- Variable-Positional arguments   *args: {0}".format(args))
    print("3.- Keyword arguments               k: {0}".format(k))
    print("4.- Variable-Keyword arguments:     **args: {0}".format(kwargs))


func(1, 2, 3, 4, 5, k=6, ke1=7, key2=8)
