# Byte array is a mutable version of the bytes data structure


def main():
    # We can create a bytearray by using a sequence of integers
    ba = bytearray([1,2,3,4])
    print(ba)

    # bytearray is a mutable type so we can modify it
    ba.append(5)
    print(ba)

    # We can also initialize a bytearray with a hex string
    ba = bytearray.fromhex("ff 12")
    print(ba)


if __name__ == '__main__':
    main()