# Great and Poem assessment program with number input of a student in one subject
def poem_assessment():
    # Get input from the user
    student_name = input("Enter student's name: ")
    poem_grade = float(input("Enter the student's grade for the poem (0-100): "))

    # Validate input
    if not (0 <= poem_grade <= 100):
        print("Error: Invalid grade. Please enter a number between 0 and 100.")
        return

    # Assess the student's performance
    if 90 <= poem_grade <= 100:
        assessment = "Excellent"
    elif 80 <= poem_grade < 90:
        assessment = "Very Good"
    elif 70 <= poem_grade < 80:
        assessment = "Good"
    elif 60 <= poem_grade < 70:
        assessment = "Satisfactory"
    else:
        assessment = "Needs Improvement"

    # Display the assessment
    print(f"\nStudent Name: {student_name}")
    print(f"Poem Grade: {poem_grade}")
    print(f"Assessment: {assessment}")

if __name__ == "__main__":
    poem_assessment()
