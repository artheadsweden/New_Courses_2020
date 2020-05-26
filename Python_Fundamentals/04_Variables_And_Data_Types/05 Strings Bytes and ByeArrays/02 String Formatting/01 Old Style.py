def main():
    # Setup stuff
    first_name = "Anna"
    last_name = "Jones"
    age = 34

    msg = 'Hi %s, your full name is %s %s and you are %d years old' % (first_name, first_name, last_name, age)
    print(msg)

    # We can also algin text
    msg = '%10s' % (first_name,)
    print(msg)
    # And we can pad
    msg = '%-10s!' % (first_name,)
    print(msg)

    # Format floating point numbers
    # In this case 6 characters padding with 0
    msg = '%06.2f' % (3.141592653589793,)
    print(msg)


if __name__ == '__main__':
    main()