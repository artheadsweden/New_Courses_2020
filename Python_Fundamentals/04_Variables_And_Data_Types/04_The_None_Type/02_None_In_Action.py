def add_to_list(name, people=[]):
    people.append(name)
    return people


def add_to_list_imporoved(name, people=None):
    if not people:
        people = []
    people.append(name)
    return people


def main():
    # As we are not passing any list we might expect to see
    # only one name in the list after each call
    # But when inspecting the result we see that this is not the case
    names1 = add_to_list("Alice")
    print(names1)
    names2 = add_to_list("Bob")
    print(names2)

    # This happens because people is a mutable type (a list)
    # and that it is initialized to an empty list on execution
    # not when it is called
    # Here the None-type can help us

    names1 = add_to_list_imporoved("Alice")
    print(names1)
    names2 = add_to_list_imporoved("Bob")
    print(names2)

if __name__ == '__main__':
    main()
