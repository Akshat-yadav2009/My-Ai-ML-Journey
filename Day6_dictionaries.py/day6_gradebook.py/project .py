students = []
SUBJECTS = ["Math","Science","English","History"]

while True:
    print("\n1.Add new student")
    print("2.Add/update score for student")
    print("3.View single student report")
    print("4.View all students")
    print("5.Class statistics per subject")
    print("6.Top 3 students overall")
    print("7.Find students by grade")
    print("8.Delete student")
    print("9.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name: ")
        sid = int(input("Enter id: "))

        new_student = {
            "name": name,
            "id": sid,
            "scores": {},
            "overall_grade": ""
        }

        students.append(new_student)
        print("Student added!")

    elif choice == 2:
        sid = int(input("Enter student id: "))
        found = False

        for s in students:
            if s["id"] == sid:
                found = True

                subject = input("Enter subject: ")
                score = int(input("Enter score: "))
                s["scores"][subject] = score

                print("Updated!")

        if not found:
            print("Student not found!")

    elif choice == 3:
        sid = int(input("Enter your id: "))
        found = False

        for s in students:
            if s["id"] == sid:
                found = True

                print("="*40)
                print("Student Report:", s["name"])
                print("ID:", s["id"])
                print("="*40)

                for subject, score in s["scores"].items():
                    if score >= 90:
                        sg = "A"
                    elif score >= 80:
                        sg = "B"
                    elif score >= 70:
                        sg = "C"
                    elif score >= 60:
                        sg = "D"
                    else:
                        sg = "F"

                    print(f"{subject:<10}: {score} ({sg})")

                if len(s["scores"]) > 0:
                    avg = sum(s["scores"].values()) / len(s["scores"])
                else:
                    avg = 0

                if avg >= 90:
                    grade = "A"
                elif avg >= 80:
                    grade = "B"
                elif avg >= 70:
                    grade = "C"
                elif avg >= 60:
                    grade = "D"
                else:
                    grade = "F"

                print("-"*40)
                print("Average:", round(avg, 2))
                print("Grade:", grade)
                print("="*40)

        if not found:
            print("Student not found")

    elif choice == 4:
        if len(students) == 0:
            print("No student found")
        else:
            for s in students:
                print(f"Name: {s['name']} | ID: {s['id']}")
                print("Scores:", s["scores"])
                print("-------------------")

    elif choice == 5:
        for subject in SUBJECTS:
            scores = []

            for s in students:
                if subject in s["scores"]:
                    scores.append(s["scores"][subject])

            if len(scores) > 0:
                avg = sum(scores) / len(scores)
                print(subject)
                print("Average:", avg)
                print("Highest:", max(scores))
                print("Lowest:", min(scores))
                print("-------------------")
            else:
                print(subject, ": No data")

    elif choice == 6:
        if len(students) == 0:
            print("No students")
        else:
            def get_avg(s):
                if len(s["scores"]) == 0:
                    return 0
                return sum(s["scores"].values()) / len(s["scores"])

            top = sorted(students, key=get_avg, reverse=True)[:3]

            print("Top Students:")
            for s in top:
                print(s["name"], "Avg:", round(get_avg(s), 2))

    elif choice == 7:
        for s in students:
            if len(s["scores"]) == 0:
                continue

            avg = sum(s["scores"].values()) / len(s["scores"])

            if avg >= 90:
                grade = "A"
            elif avg >= 80:
                grade = "B"
            elif avg >= 70:
                grade = "C"
            elif avg >= 60:
                grade = "D"
            else:
                grade = "F"

            print(s["name"], "Grade:", grade)

    elif choice == 8:
        sid = int(input("Enter id to delete: "))
        found = False

        for s in students:
            if s["id"] == sid:
                students.remove(s)
                print("Deleted!")
                found = True
                break

        if not found:
            print("Student not found")

    elif choice == 9:
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
    

