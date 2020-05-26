def main():
    with open("data.txt", "r") as f:
        text = f.read(6)
        print(text)
        print(f.tell())
        text = f.read(2)
        print(text)
        print(f.tell())

        f.seek(25, 0)
        text = f.read(4)
        print(text)


if __name__ == '__main__':
    main()
