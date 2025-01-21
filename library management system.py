class Library:
    def __init__(self, list, name):
        self.booklist = list
        self.name = name
        self.lenDict = {}

    def display_books(self):
        print(f"We have following books in our library : {self.name}")
        for book in self.booklist:
            print(book)

    def lend_book(self, user, book):
        if book not in self.lenDict.keys():
          self.lenDict.update({book:user})
          print("Lender-Book database has been updated. You can take the book now.")
        else:
            print(f"Book is already being used by : {self.lenDict[book]}")
    def add_book(self, book):
        self.booklist.append(book)      
        print("Book has been added to the book list")
    def return_book(self, book):
        self.lenDict.pop(book)

books = Library(["Python", "Rich dad poor dad", "Harry Potter", "Java Programming", "Rayed's Library"],"library")

while True:
    print(f"Welcome to the {books.name}")
    print("Choose any one option")
    print("1. Display a book")
    print("2. Lend a book")
    print("3. Add a book")
    print("4. Return a book")
    user_choice = int(input("Enter the number of your choice : "))
    if user_choice == 1:
        books.display_books()
    elif user_choice == 2:
        book = input("Enter the name of the book you want to lend : : ")
        user = input("Enter your name : ")
        books.lend_book(user,book)
    elif user_choice == 3:
        book = input("Enter the name of the book you want to add :")
        books.add_book(book)
    elif user_choice == 4:
        book = input("Enter the name of the book you want to return : ")
        books.return_book(book)
    else:
        print("Not a valid option")

    print("press q to quit and c to continue")
    user_choice2 = input("Enter your choice to continue or quit : ")
    while (user_choice2 != user_choice2 != "q"):
        if user_choice2 == "q":
            exit()
        elif user_choice2 == "c":
          continue    