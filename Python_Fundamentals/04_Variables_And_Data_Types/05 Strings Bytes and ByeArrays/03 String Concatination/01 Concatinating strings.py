def main():
    str1 = "String1"
    str2 = "String2"
    str3 = "String3"

    # We can concatinate using the + operator

    new_message = str1 + str2 + str3
    print(new_message)

    # We can insert 'constant' strings into the sequence
    new_message = str1 + " " + str2 + " " + str3
    print(new_message)

    # An other, and often faster, way to concatinate strings is to use the join function
    new_message = "".join([str1, str2, str3])
    print(new_message)

    # The empty string before join dictates what will be inserted between each string, in previous case nothing.
    # This can be used to, for example, insert a space between each string
    new_message = " ".join([str1, str2, str3])
    print(new_message)

if __name__ == '__main__':
    main()