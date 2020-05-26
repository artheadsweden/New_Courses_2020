def main():
    my_str = "is this what it is"
    next_index = 0

    for i in range(len(my_str)):
        index = my_str.find("is", next_index)
        next_index = index + 1
        if index == -1:
            print(f"Found 'is' {i} times")
            break
        print(f"Found 'is' at index {index}")


if __name__ == '__main__':
    main()