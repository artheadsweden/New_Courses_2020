def main():
    try:
        pass
        # This is the try block
    except Exception:
        pass
        # Here we can catch an Exception
    else:
        pass
        # In Python we have an else clause
        # We will end up here if no exception occurs in the try block
    finally:
        pass
        # The finally block is guaranteed to always execute
        # even if we have an unhandled exception
        # This is where we can do clean up, such as closing files
        # and connections


if __name__ == '__main__':
    main()
