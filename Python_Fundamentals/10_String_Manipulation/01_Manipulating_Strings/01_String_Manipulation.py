def main():
    # Creating
    word = "Hello World"

    # Accessing
    letter = word[0]
    print(letter)

    # Length
    print(len(word))

    # Counting
    s = "This is a string     with some space in it"
    print(s.count(" "))

    # Finding
    print(word.find("World"))

    # Slicing
    print(word[0])      # Prints the first character
    print(word[0:1])    # Prints the first character
    print(word[0:3])    # Prints the first three characters
    print(word[2:3])    # Prints the third character
    print(word[:3])     # Prints the first three characters
    print(word[-3:])    # Prints the last three characters
    print(word[3:])     # Prints all but the three first characters

    # Splitting
    s = "Pete;34;55 Main Street;US"
    fields = s.split(";")
    print(fields)

    # Startswith/Endswith
    print(word.startswith("H"))
    print(word.endswith("d"))
    print(word.endswith("l"))

    # Repeating
    line = "_" * 80
    print(line)

    # Casing
    print(word.upper())
    print(word.lower())
    word2 = "hellO wOrld"
    print(word2.title())
    print(word2.capitalize())
    print(word2.swapcase())

    # join
    result = "-".join(word)
    print(result)
    result = " ".join(word)
    print(result)
    result = word.join("--")
    print(result)

    # Concatinating
    result = word + "!"
    print(result)
    result = "Hi" + str(5)
    print(result)
    result = " ".join(["Hello", "World"])
    print(result)

    # Strip
    word2 = "     Hello World    "
    print("!" + word2 + "!")
    print("!" + word2.rstrip() + "!")
    print("!" + word2.lstrip() + "!")
    print("!" + word2.strip() + "!")

    # Testing content
    numword = "1356"
    print(numword.isdecimal())
    # age = ""
    # while not age.isdecimal():
    #    age = input("Enter your age: ")

    # age = int(age)
    print(word.isalpha())
    print(numword.isalnum())
    print(word.isalnum())
    print(word.istitle())
    print(word.islower())

    print("lo" in word)


if __name__ == '__main__':
    main()
