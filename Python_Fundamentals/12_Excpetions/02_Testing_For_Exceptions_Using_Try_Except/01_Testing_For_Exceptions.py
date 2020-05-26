def main():
    try:
        pass
        # This is the try block
    except RuntimeError as e:
        pass
        # Here we can catch an RuntimeError exception
        # e is the exception object
    except ValueError as e:
        pass
        # Here we can catch an ValueError exception
        # e is the exception object


if __name__ == '__main__':
    main()
