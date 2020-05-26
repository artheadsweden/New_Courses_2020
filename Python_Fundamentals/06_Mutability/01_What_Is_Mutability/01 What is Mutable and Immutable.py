def main():
    # Something that is immutable cannot change once it has gotten a value
    # An integer for example is an immutable type in Python
    # We can see this
    x = 10
    y = 10
    print(id(x))
    print(id(y))
    x = 11
    print(id(x))

    x = [1, 2, 3]
    y = x.copy()
    print(id(x))
    print(id(y))


if __name__ == '__main__':
    main()
