import re


def main():
    phone = "ERD555-434-776!!"
    num = re.sub(r'\D', "", phone)
    print(num)

    text = "lkjdsla0704534532sdfkj0704 34 23 19sdlkjfs0123456789"
    pattern = re.compile(r'07\d{8}')
    mobile_number = re.findall(pattern, text)
    print(mobile_number)
    pattern = re.compile(r'07\d{2}\D*\d{2}\D*\d{2}\D*\d{2}')
    mobile_numbers = re.findall(pattern, text)
    print(mobile_numbers)


if __name__ == '__main__':
    main()
