def main():
    # Can hold the values True and False
    done = True
    equal = False
    print(done)
    print(equal)

    name = ""  # Empty string, None, 0 and False will all be evaluated into False
    # Everything else will be True
    if name:
        print("True")
    else:
        print("False")


    x = 0

    if x:
        print("x is not 0")
    else:
        print("x is 0")

    nothing = None

    if nothing:
        print("Nothing is something")
    else:
        print("Nothing is not anything")


if __name__ == '__main__':
    main()