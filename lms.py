# Library Management System
# Create a file named book_available.txt and mention all the books there

import datetime

class LibraryManagementSystem:

    def __init__(self, books_available, library_name):
        self.books_available = "books_available.txt"
        self.library_name = library_name
        self.books_dict = {}
        id = 1001
        with open(self.books_available) as b:
            content = b.readlines()
        for line in content:
            self.books_dict.update({str(id): {'books_title': line.replace("\n", ""), 'lender_name': '', 'len_date': '', 'status': 'Available'}})
            id += 1

    def display_books(self):
        print("---List of Books---")
        print("Books Id", "\t", "Title")
        print("--------------------")
        for key, value in self.books_dict.items():
            print(key, "\t\t", value.get("books_title"), "- [", value.get("status"), "]")

    def lend_books(self):
        books_id = input("Enter the Books Id: ")
        current_date = datetime.datetime.now().strftime("%d-%m-$Y %H:%M:%S")
        if books_id in self.books_dict.keys():
            if self.books_dict[books_id]['status'] is not 'Available':
                print(f"This book is already issued to {self.books_dict[books_id]['lender_name']} on {self.books_dict[books_id]['lend_date']}")
                return self.lend_books()
            elif self.books_dict[books_id]['status'] is 'Available':
                your_name = input("Enter your Name: ")
                self.books_dict[books_id]['lender_name'] = your_name
                self.books_dict[books_id]['lend_date'] = current_date
                self.books_dict[books_id]['status'] = 'Already Issued'
                print("Books Issued Successfully !!!!\n")
        else:
            print("Book Id not found !!!")
            return self.lend_books()

    def add_books(self):
        new_books = input("Enter the Book's Tittle: ")
        if new_books == "":
            return self.add_books()
        elif len(new_books) > 20:
            print("Books title length is too long !!! Title length limit is 20 characters")
            return self.add_books()
        else:
            with open(self.books_available, "a") as b:
                b.writelines(f"{new_books}\n")
            self.books_dict.update({str(int(max(self.books_dict)) + 1): {'books_title': new_books,
                                                                         'lender_name': '', 'status': 'Available'}})
            print(f"The books '{new_books}' has been successfully added !!!")

    def return_books(self):
        books_id = input("Enter Book Id: ")
        if books_id in self.books_dict.keys():
            if self.books_dict[books_id]['status'] is 'Available':
                print("This book is already in library. Please check the Book Id !!!")
                return self.return_books()
            elif self.books_dict[books_id]['status'] is not 'Available':
                self.books_dict[books_id]['lender_name'] = ''
                self.books_dict[books_id]['lend_date'] = ''
                self.books_dict[books_id]['status'] = 'Available'
                print("Successfully Updated !!!!\n")
            else:
                print("Book Id not found !!!")
                return self.return_books()


if __name__ == "__main__":
    try:
        lms = LibraryManagementSystem("books_available.txt", "Coding")
        press_key_list = {"D": "Display Books", "L": "Lend Books", "A": "Add Books", "R": "Return Books", "Q": "Quit"}

        key_press = False
        while key_press is not "q":
            print(f"\nWelcome to {lms.library_name}'s Library Management System\n")
            for key, value in press_key_list.items():
                print("Press", key, "To", value)
            key_press = input("Press Key: ").lower()
            if key_press == "l":
                print("\nCurrent Selection : Lend Book\n")
                lms.lend_books()
            elif key_press == "a":
                print("\nCurrent Selection : Add Book\n")
                lms.add_books()
            elif key_press == "d":
                print("\nCurrent Selection : Display Book\n")
                lms.display_books()
            elif key_press == "r":
                print("\nCurrent Selection : Return Book\n")
                lms.return_books()
            elif key_press == "q":
                break
            else:
                continue

    except Exception as e:
        print("Something is wrong. Please Select Again !!!")
