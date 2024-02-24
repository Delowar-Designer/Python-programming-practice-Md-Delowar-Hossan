# Python Project 1 Marge The PDF Project
''''from PyPDF2 import PdfMerger
AllPDF = ["Developer Delowar Designer.pdf", "Programer Delowar Designer.pdf"]

OurMerger = PdfMerger()

for NewPDF in AllPDF:
    OurMerger.append(NewPDF)

OurMerger.write("Programer and Developer Delowar Designer.pdf")
OurMerger.close()
'''

from PyPDF2 import PdfMerger

# List of PDF files to merge
AllPDF = ["Developer Delowar Designer.pdf", "Programer Delowar Designer.pdf"]

# Initialize PDF merger object
OurMerger = PdfMerger()

# Loop through each PDF and append it to the merger
for NewPDF in AllPDF:
    OurMerger.append(NewPDF)

# Write the merged PDF to a new file
with open("Programer and Developer Delowar Designer2.pdf", "wb") as merged_file:
    OurMerger.write(merged_file)

# Close the merger object
OurMerger.close()