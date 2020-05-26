import sys
def main():
    # Since Python 3.0 all strings are stored in Unicode
    # Default Python will use UTF-8
    message = "This is a Unicode string. See here: 你好."
    print(message)

    # Also identifiers can be in Unicode
    你好 = 'Hello'
    print(你好)

    msg1 = 'AB'
    msg2 = 'ÅÄ'
    msg3 = '你好'

    print(sys.getsizeof(msg1))
    print(sys.getsizeof(msg2))
    print(sys.getsizeof(msg3))

    # We can use character names to represent Unicode characters
    message = "\N{GREEK SMALL LETTER PI}"
    print(message)
    # Or we can use a 16-bit hex value
    message = '\u03C0'
    print(message)
    # Or a 32-bit hex value
    message = '\U000003C0'
    print(message)

    # We can even have emoji's
    message = '\U0001F920'
    print(message)


if __name__ == '__main__':
    main()