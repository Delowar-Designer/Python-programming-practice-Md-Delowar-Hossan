def calculate_average(grades):
    return sum(grades) / len(grades)

def analyze_grade(average):
    if 90 <= average <= 100:
        return "A"
    elif 80 <= average < 90:
        return "B"
    elif 70 <= average < 80:
        return "C"
    elif 60 <= average < 70:
        return "D"
    else:
        return "F"

def gta_grade_analysis():
    # Get input for the number of students and subjects
    num_students = int(input("Enter the number of students: "))
    num_subjects = int(input("Enter the number of subjects: "))

    # Initialize a dictionary to store grades
    grade_data = {}

    # Input grades for each student and subject
    for student in range(1, num_students + 1):
        student_name = input(f"\nEnter name for Student {student}: ")
        grades = []

        for subject in range(1, num_subjects + 1):
            grade = float(input(f"Enter the grade for Subject {subject} (0-100) for {student_name}: "))

            # Validate input
            if not (0 <= grade <= 100):
                print("Error: Invalid grade. Please enter a number between 0 and 100.")
                return

            grades.append(grade)

        grade_data[student_name] = grades

    # Analyze and display grades
    print("\nGrade Analysis:")
    for student, grades in grade_data.items():
        average_grade = calculate_average(grades)
        letter_grade = analyze_grade(average_grade)
        print(f"\nStudent: {student}")
        print(f"Average Grade: {average_grade:.2f}")
        print(f"Letter Grade: {letter_grade}")

if __name__ == "__main__":
    gta_grade_analysis()
