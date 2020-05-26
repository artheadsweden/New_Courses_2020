def say_hi(name, times = 2, end = "!"):
    for _ in range(times):
        print("Hi", name, end)


def main():
    say_hi("John", 3)
    say_hi("Anna", end = "?")
    say_hi(times = 4, end = "#", name = "Sue")


if __name__ == '__main__':
    main()
