def main():
    x = 10
    print(x)

    print("Hi there")

    name = "John"
    print("Hi there", name)

    print("This is ", name, "'s bike", sep="")

    print("This is {0}'s bike".format(name))
    age = 17
    print("This is {0}'s bike. He is {1} years old. Bye {0}".format(name, age))

    print("Hi", end="")
    print("Bye")


if __name__ == '__main__':
    main()
