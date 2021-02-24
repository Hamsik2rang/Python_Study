numbers = [19, 23, 24, 66]

# variable argument
def print_args(*args):
    for arg in args:
        print(arg)


def print_list(arg_list):
    for arg in arg_list:
        print(arg)


print_args(10, *[1, 4, 2, 3, 5])