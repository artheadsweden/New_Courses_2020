class Coordinate(dict):
    def __missing__(self, key):
        return 'NaN'


def main():

    print('({x}, {y})'.format_map(Coordinate(x='6')))
    print('({x}, {y})'.format_map(Coordinate(y='5')))
    print('({x}, {y})'.format_map(Coordinate(x='6', y='5')))


if __name__ == '__main__':
    main()