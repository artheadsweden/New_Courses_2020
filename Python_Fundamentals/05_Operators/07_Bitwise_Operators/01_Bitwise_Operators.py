def print_byte(value):
    print('+' + '---+' * 8)
    print('|128| 64| 32| 16| 8 | 4 | 2 | 1 |')
    print('+' + '---+' * 8)
    bits = f'{value:>08b}'
    for bit in bits:
        print(f'| {bit} ', end='')
    print('|')
    print('+' + '---+' * 8)


def main():
    # Using the bitwise operators we can manipulate individual bits of an variable
    x = 17
    # We can print an integer as a binary number like this
    print_byte(x)

    # Let's print a separator line
    print("="*20)

    # Bitwise and
    result = x & 16
    print(f"{x:>08b}")
    print("   &")
    print(f"{16:08b}")
    print("   =")
    print(f"{result:08b}")

    print("="*20)

    # Bitwise or
    result = x | 7
    print(f"{x:>08b}")
    print("   |")
    print(f"{7:08b}")
    print("   =")
    print(f"{result:08b}")

    print("="*20)

    # Bitwise xor
    result = x ^ 7
    print(f"{x:>08b}")
    print("   ^")
    print(f"{7:08b}")
    print("   =")
    print(f"{result:08b}")

    print("="*20)

    # Bitwise not (inverse all bits)
    # As Python uses two complement to indicate a negative number the output might not look the way you expect
    x = 10
    print(f"{x:>08b}")
    print(f"{~x:08b}")

    print("="*20)

    # Bitwise zero fill left shift
    x = 10
    print(f"{x:>08b}")
    print(f"{x<<2:08b}")

    print("="*20)

    # Bitwise zero fill right shift
    x = 10
    print(f"{x:>08b}")
    print(f"{x>>2:08b}")


if __name__ == '__main__':
    main()
