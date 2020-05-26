def main():
    # There is only one integer type in Python . int
    x = 10  # Remember that Python is dynamically typed and x becomes an int when we assign to it

    # Integers in Python does not have any upper limit
    x = 999999999999999999999999999999
    y = 999999999999999999999999999999
    # To create a huge number we can multiply x and y and raise the result to the power of 10,000
    z = x * y ** 10000
    # If we want to know how many digits a number has we can convert the int to a string and get the length of it
    num_digits = len(str(z))
    print("The result is a number with", num_digits, "digits")


if __name__ == '__main__':
    main()