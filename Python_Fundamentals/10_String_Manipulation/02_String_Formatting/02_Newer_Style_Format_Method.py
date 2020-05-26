def main():
    age = 34
    name = 'Alice'

    message = 'Hello {}. You are {} years old.'.format(name, age)
    print(message)

    # We can also name the interpolated values
    message = 'Hello {name}. You are {age} years old.'.format(name=name, age=age)
    print(message)

    # If a value is repeated we can use index numbers
    message = 'Hello {0}. You are {1} years old. Bye {0}.'.format(name, age)
    print(message)


if __name__ == '__main__':
    main()
