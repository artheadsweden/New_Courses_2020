def main():
    # Setup stuff
    first_name = "Anna"
    last_name = "Jones"
    age = 34

    msg = 'Hi {0}, your full name is {0} {1} and you are {2} years old'.format(first_name, last_name, age)
    print(msg)

    # We can also algin text
    msg = '{:>10}'.format(first_name,)
    print(msg)
    # And we can pad
    msg = '{:10}!'.format(first_name,)
    print(msg)

    # Format floating point numbers
    # In this case 6 characters padding with 0
    msg = '{:06.2f}'.format(3.141592653589793,)
    print(msg)


    # You can also do things you can't do with the old style like
    # Center text
    msg = '>{:^16}<'.format(first_name)
    print(msg)


if __name__ == '__main__':
    main()