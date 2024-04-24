# Program Name 2 Generate PDF Report (Students bssic information) from CSV file
import csv
from fpdf import FPDF

# Open CSV file in write mode to store student records
with open("student2.csv", "w+", newline="") as fh:
    w = csv.writer(fh)
    header = ["Student ID", "Name", "Roll", "Semester", "Shift", "Department", "Date of Birth", "Phone No."]
    w.writerow(header)

    # Take input for student records
    try:
        n = int(input("How many student records to insert? "))
    except ValueError:
        print("Please enter a valid number.")
        exit()

    data = []
    for i in range(n):
        print(f"Enter Student record {i + 1}:")
        student_id = input("Student ID: ")
        name = input("Name: ")
        roll = int(input("Roll: "))
        semester = input("Semester: ")
        shift = input("Shift: ")
        dept = input("Department: ")
        dob = input("Date of Birth (dd/mm/yyyy): ")
        phone_no = input("Phone No: ")
        rec = [student_id, name, roll, semester, shift, dept, dob, phone_no]
        data.append(rec)
    w.writerows(data)

# Generate PDF report
pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 12)

col_width = pdf.w / 7

with open("student2.csv", "r") as fh:
    r = csv.reader(fh)
    th = pdf.font_size

    # Add column headers
    for header in header:
        pdf.cell(col_width, th, header, border=1)
    pdf.ln(th)

    # Add student records
    for row in r:
        for item in row:
            pdf.cell(col_width, th, str(item), border=1)
        pdf.ln(th)

pdf.output('student2.pdf')
print("PDF report generated successfully.")
