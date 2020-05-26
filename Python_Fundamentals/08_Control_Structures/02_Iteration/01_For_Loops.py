def main():
    my_list = ["John", "Sara", "Anna", "Peter"]
    for name in my_list:
        print("Hi", name)

    name = "John-Paul"
    for c in name:
        print(c)

    for i in range(10, -1, -1):
        print(i)

    for _ in range(10):
        print("Hi")

    my_friend = {"name": "John", "age": 26, "city": "London"}
    for k, v in my_friend.items():
        print(k, "=", v)

    for i in range(5):
        for j in range(3):
            print("i =", i, "j =", j)

    for i in range(10):
        if i == 3:
            continue
        print(i)

    print("Ok we are done")


if __name__ == '__main__':
    main()
