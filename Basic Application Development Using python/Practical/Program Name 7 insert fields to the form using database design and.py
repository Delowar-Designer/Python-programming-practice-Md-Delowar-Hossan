import tkinter as tk
import sqlite3

# Database connection (replace with your database details)
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

# Function to insert data into database
def insert_data():
    name = name_field.get()
    course = course_field.get()
    # ... (get data from other fields)

    # Create an SQL INSERT statement with placeholders
    sql = "INSERT INTO your_table (name, course, ...) VALUES (?, ?, ...)"
    cursor.execute(sql, (name, course, ...))  # Replace ... with actual data

    # Save changes to the database
    conn.commit()

    # Clear entry fields and other actions (optional)

# ... (rest of your GUI code)

# Create a Submit Button and link it to the insert_data function
submit_button = tk.Button(root, text="Submit", command=insert_data)
submit_button.grid(...)

# ... (rest of your GUI code)

# Close the database connection
conn.close()

root.mainloop()
