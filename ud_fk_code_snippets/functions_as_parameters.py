def square_it(x):
    return x*x


# print(SquareIt(2))


def square_it_param(func, x):
    return func(x)


# print(square_it_param(square_it, 2))

print(square_it_param(lambda x: x*x*x, 3))
