# Stack And Queue
books = []
books.append("Learn C")
books.append("Learn Python")
books.append("Learn Java")
books.append("Learn C++")
print(books)

books.pop()
print(books)
print("Now the book is: ",books[-2])

books.pop()
print("Now the book is: ",books[-2])

books.pop()
print("Now the book is: ",books[-1])

books.pop()
if not books:
    print("No books")

