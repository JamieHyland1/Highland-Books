import Books
from Books import Book

b = Book("1Q84", "Haruki Murakami", 15.50,17.99)
print("Weclome to Hyland Books")
print("===============================")
print("=Press 1 to see all books" +
      "\n=Press 2 to add a book" +
      "\n=Press 3 to delete a book" + 
      "\n=Press 4 update a books details" +
      "\n=Press 5 to leave the store")

choice = input("Please select a number")
while choice != 5:
        if choice == 1:
            b.display()
            choice = input()
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            print("Goodbye!")
            break
