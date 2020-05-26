def main():
    # The is operators checks if two variables are the same object
    x = 10
    y = 10
    print(x is y)
    # Note that it is not the same as the equal to operator ==
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    print(list1 == list2)
    print(list1 is list2)


if __name__ == '__main__':
    main()
