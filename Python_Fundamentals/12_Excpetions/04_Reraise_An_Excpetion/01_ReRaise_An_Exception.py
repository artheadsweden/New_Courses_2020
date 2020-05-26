class ArgumentError(ValueError):
    pass


def my_func(x, y):
    if y == 0:
        raise ValueError("Can't pass 0 to y")
    z = x / y
    return z


def main():
    try:
        result = my_func(10, 2)
    except ValueError as e:
        # We are re-raising the same exception
        raise
    else:
        print(result)
    finally:
        print("Will always run")


if __name__ == '__main__':
    main()
