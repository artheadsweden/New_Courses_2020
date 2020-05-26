def main():
    # Capitilize

    # Center

    # Casefold

    my_str = "Meßergebnis"
    new_str1 = my_str.lower()
    new_str2 = my_str.casefold()

    print(new_str1, new_str2)

    # Count

    # Endswith

    # Expandtabs
    my_str = "This\tis\ta\tstring"
    for c in my_str:
        print(ascii(c))

    print('-'*20)

    for c in my_str.expandtabs():
        print(ascii(c))

    print(my_str)
    print(my_str.expandtabs())

    # Encode
    # unicode string
    string = 'pythôn!'

    # print string
    print('The string is:', string)

    # default encoding to utf-8
    string_utf = string.encode()

    # print result
    print(string_utf)


    # Translate

    intab = "aeiou"
    outtab = "@3104"
    trantab = string.maketrans(intab, outtab)
    for k,v in trantab.items():
        print(k, "=", chr(k), v, "=", chr(v))

if __name__ == '__main__':
    main()