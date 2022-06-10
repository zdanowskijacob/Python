from gradesFun import mean, median, variance, printGrades, deviation


def main():
    subjects = set()
    grades = []
    if len(subjects) == 0:
        print("No subjects added yet")
    else:
        print(subjects)

    print("If You want to stop adding subjects press enter")
    while True:
        subject = input("Enter subject to list: ")
        if len(subject):
            if subject in subjects:
                print("subject already in list")
            else:
                subjects.add(subject)
        else:
            print(subjects)
            break

    subject = input("To witch subject do You want to add grade? ")
    if subject not in subjects:
        print("No such a subject.")
    else:
        while True:
            try:
                grade = int(input("Enter grade: "))
                if (grade > 0 and grade < 7):
                    grades.append(float(grade))
                elif grade == 0:
                    break
                else:
                   print("incorrect grade!")
            except ValueError:
                print("incorrect data!")

    printGrades(grades, subject)
    m = mean(grades)
    medi = median(grades)
    dev = deviation(grades, m)

    print("\nMean: {0:5.2f}".format(m))
    print("Median: {0:5.2f}\nDeviation: {1:5.2f}".format(medi, dev))


main()
