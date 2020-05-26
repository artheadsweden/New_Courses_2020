def main():
    my_str = "This\tis\ta\tstring"
    for c in my_str:
        print(ascii(c))

    print('-'*20)

    for c in my_str.expandtabs():
        print(ascii(c))

    print(my_str)
    print(my_str.expandtabs())


if __name__ == '__main__':
    main()