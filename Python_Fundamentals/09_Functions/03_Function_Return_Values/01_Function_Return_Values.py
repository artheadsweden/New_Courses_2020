def add(a, b):
    return a + b


def greeting(name, times):
    greeting_str = ""
    for _ in range(times):
        greeting_str += "Hi " + name + "\n"
    return greeting_str


def return_values(a, b):
    return a*2, b*3, a * b


def main():
    x = add(2, 3)
    print(x)

    greet = greeting("John", 3)
    print(greet, end="")

    greet2 = greeting("Sara", 5)
    print(greet2, end="")

    a, b, c = return_values(2, 3)
    print("a =", a, "b =", b, "c =", c)
    d = return_values(4, 5)
    print(d)


if __name__ == '__main__':
    main()
