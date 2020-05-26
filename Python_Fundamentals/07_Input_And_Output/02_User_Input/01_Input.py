def main():
    name = input("What is your name? ")
    print("Hi there", name)
    age = input("How old are you? ")
    print("So you are", age, "years old")
    age = int(age) + 1
    print("In one year you will be", age, "years old.")


if __name__ == '__main__':
    main()
