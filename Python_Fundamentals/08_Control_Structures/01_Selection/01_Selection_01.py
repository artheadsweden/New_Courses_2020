def main():
    name = input("What is your name? ")
    city = input("Where do you live?")
    if name.lower() == "anna" and city.lower() == "paris":
        print("Wow,", name, "is a great name! And", city, "is a great city.")
    else:
        if name.lower() == "peter":
            print("Peter is a great name")
        else:
            print("Oh, hi", name)


if __name__ == '__main__':
    main()
