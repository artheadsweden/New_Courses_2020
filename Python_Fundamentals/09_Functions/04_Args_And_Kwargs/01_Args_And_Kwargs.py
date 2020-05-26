def my_func(*args):
    print("my_func with", len(args))
    for value in args:
        print(value)


def my_func_2(**kwargs):
    print("my_func_2 with", len(kwargs))
    for k, v in kwargs.items():
        print(k, "=", v)


def my_func_3(*args, **kwargs):
    print("Pos args: ", len(args))
    print("Kw args:", len(kwargs))
    print("args:")
    for value in args:
        print(value)

    print("kwargs:")
    for k, v in kwargs.items():
        print(k, "=", v)


def main():
    my_func(1, 3)
    my_func(2, 4, 6, 8)
    my_func(9)
    my_func()

    my_func_2(name = "Bob", age = 34)
    my_func_2(city = "London", country = "UK", value = 34)
    my_func_2()

    my_func_3(1, 2, 3, name = "John", city = "Rome")
    my_func_3()
    my_func_3(animal = "Dog")
    my_func_3(2, 3)


if __name__ == '__main__':
    main()
