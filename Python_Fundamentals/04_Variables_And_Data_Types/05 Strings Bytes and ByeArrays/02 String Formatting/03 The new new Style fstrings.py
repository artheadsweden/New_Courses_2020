def main():
    # Setup stuff
    first_name = "Anna"
    last_name = "Jones"
    age = 34

    msg = f'Hi {first_name}, your full name is {first_name} {last_name} and you are {age} years old'
    print(msg)

    # We can have expressions inside f-strings
    msg = f"I shouted {first_name.upper()} because in 2 years time {first_name}'s age will be {age+2}"
    print(msg)

    # We can also algin text
    msg = f'{first_name:>10}'
    print(msg)
    # And we can pad
    msg = f'{first_name:10}!'
    print(msg)

    # Format floating point numbers
    # In this case 6 characters padding with 0
    msg = f'{3.141592653589793:06.2f}'
    print(msg)


    # You can also do things you can't do with the old style like
    # Center text
    msg = f'>{first_name:^16}<'
    print(msg)


if __name__ == '__main__':
    main()