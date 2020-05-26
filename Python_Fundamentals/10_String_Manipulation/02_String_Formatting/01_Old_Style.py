def main():
    age = 34
    name = 'Alice'

    message = 'Hello %s. You are %d years old.' % (name, age)
    print(message)

    # It is also possible to use the variable names when formatting
    # We will then need to provide a dict with the variables
    message = 'Hello %(name)s. You are %(age)d years old.' % {'name': name, 'age': age}
    print(message)


if __name__ == '__main__':
    main()
