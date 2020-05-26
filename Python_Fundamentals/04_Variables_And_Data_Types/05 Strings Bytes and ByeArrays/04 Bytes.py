# bytes is an immutable type that stores a sequence of values
# ranging from 0-255 (8-bits, or one byte)
# We can index into this sequence to get the value of a particular byte


def main():
    b = bytes(4)  # Create an empty sequence of 4 bytes
    print(b)
    b = bytes([12, 3, 5])
    print(b)
    i = 39321
    # 128| 64| 32| 16|  8|  4|  2|  1
    #   1  0   0   1   1   0   0   1
    # 128 + 16 + 8 + 1 = 153
    # 1001 1001 1001 1001 binary
    #    9    9    9    9 hex

    # big endian is used on unix systems for example
    # little endian is used on windows systems
    two_bytes = i.to_bytes(2, byteorder="big", signed=False)
    print(two_bytes)
    for i in two_bytes:
        print(i)

    i = 127
    print(f"{i:08b}")
    print(f"{~i:08b}")

    b = i.to_bytes(1, byteorder="big", signed=True)
    print(f"{b[0]:08b}")
    b = i.to_bytes(1, byteorder="big", signed=True)
    print(f"{~b[0]:08b}")
    print(f"{~b[0]& 0b11111111:08b}")
    i = -127
    b = i.to_bytes(1, byteorder="big", signed=True)
    print(f"{b[0]:08b}")
    print(b)


if __name__ == '__main__':
    main()
