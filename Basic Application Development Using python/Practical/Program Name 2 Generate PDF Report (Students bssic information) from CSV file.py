# Program Name 2 Generate PDF Report (Students bssic information) from CSV file
"""
Experiment No : 2
2. GENERATE PDF REPORT FROM CSV FILE
2.1 Setup Environment.
2.2 Store Student basic information into CSV file. (Student_id, Name, Roll, Semester, Shift, Department, Date of birth, Phone_no.)
2.3 Generate PDF report for all of the student from information CSV file. Example: ln the report table, show students basicc information.
"""

import csv
from fpdf import FPDF

fh = open("student.csv", "w+", newline="")
w = csv.writer(fh)
# Student_id, Name, Roll, Semester, Shift, Department, Date of birth, Phone_no.
header = ["Student ID", "Name", "Roll", "Semester", "Shift", "Department", "Date of birth", "Phone_no."]
w.writerow(header)
data = []
# Take item data from the user
while True:
    try:
        n = int(input("How many insert stuudent Record: ?"))
    except ValueError:
        print("student Record are Number Please again Entered!")
        continue
    else:
        break
for i in range(n):
    print("Enter Student record", i + 1, ":")
    student_id = input("Student ID: ")
    name = input("Name: ")
    while True:
        try:
            roll = int(input("Roll: "))
        except ValueError:
            print("Invalid Roll, Please Entered Again")
            continue
        else:
            break
    semester = input("Semester: ")
    shift = input("Shift: ")
    dept = input("Department: ")
    dob = input("Date of birth(dd/mm/yyyy): ")
    phone_no = input("Phone No: ")
    # Store intems data into CSV(comma-separated values) file
    rec = [student_id, name, roll, semester, shift, dept, dob, phone_no]
    data.append(rec)
w.writerows(data)
fh.close()

# Print fruits items summary data from stored CSV file
print("Student Record from stored CSV file")
print("if you went to see pdf report, please open student pdf file your current dirctory location")
fh = open("student.csv", "r")
r = csv.reader(fh)

pdf = FPDF()
pdf.add_page()
page_width = pdf.w - 2 * pdf.I_margin

pdf.set_font('Times', 'B', 12.0)
pdf.cell(page_width, 0.0, 'Students Data Report', align='C')
pdf.In(10)

pdf.set_font('Courier', '', 12)

col_width = page_width / 6

pdf.In(1)

th = pdf.font_size
for row in r:
    # Print(row)
    pdf.cell(col_width, th, str(row[0]), border=1)
    pdf.cell(col_width, th, row[1], border=1)
    pdf.cell(col_width, th, row[2], border=1)
    pdf.cell(col_width, th, row[3], border=1)
    pdf.cell(col_width, th, row[4], border=1)
    pdf.cell(col_width, th, row[5], border=1)
    # pdf.cell(col_width, th, row[6], border=1)
    # pdf.cell(col_width, th, row[7], border=1)
    pdf.ln(th)

pdf.In(10)

pdf.set_font('Times', '', 10.0)
pdf.cell(pagr_width, 0.0, '- end of report-', align='C')

pdf.output('student.pdf', '')
fh.close()
