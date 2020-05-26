def main():
    # We can test if a sequence is present in another object
    name = "Alice"
    print("li" in name)

    # It works on lists too
    values = [1, 2, 3, 4]
    print(3 in values)

    # and dict for example
    names_and_values = {"Alice": 1, "Bob": 2}
    print("Bob" in names_and_values)


if __name__ == '__main__':
    main()
