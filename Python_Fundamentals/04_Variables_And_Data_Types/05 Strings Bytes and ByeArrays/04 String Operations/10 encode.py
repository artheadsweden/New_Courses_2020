def main():
    # unicode string
    string = 'pythôn!'

    # print string
    print('The string is:', string)

    # default encoding to utf-8
    string_utf = string.encode()

    # print result
    print(string_utf)



if __name__ == '__main__':
    main()