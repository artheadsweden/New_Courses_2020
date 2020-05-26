def main():
    grade = input("Enter grade: ")
    grade = float(grade)
    letter_grade = ""
    if grade >= 90.0:
        letter_grade = "A"
    elif grade >= 80.0:
        letter_grade = "B"
    elif grade >= 70.0:
        letter_grade = "C"
    elif grade >= 60.0:
        letter_grade = "D"
    elif grade >= 50.0:
        letter_grade = "E"
    else:
        letter_grade = "F"

    print("The student gets a letter grade of", letter_grade)


if __name__ == '__main__':
    main()
