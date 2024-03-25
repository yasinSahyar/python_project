#
class Publication:
    def __init__(self, name):
        self.name = name

    def print_information(self):
        print(f"Name: {self.name}")

class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        super().print_information()
        print(f"Author: {self.author}")
        print(f"Page Count: {self.page_count}")

class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        super().print_information()
        print(f"Chief Editor: {self.chief_editor}")

# Main program
if __name__ == "__main__":
    donald_duck = Magazine("Donald Duck", "Aki Hyyppä")
    compartment_no_6 = Book("Compartment No. 6", "Rosa Liksom", 192)

    donald_duck.print_information()
    print("\n")
    compartment_no_6.print_information()






"""
Implement the following class hierarchy using Python: A publication can be either a book or a magazine. Each publication has a name.
Each book also has an author and a page count, whereas each magazine has a chief editor. Also write the required initializers to both classes.
Create a print_information method to both subclasses for printing out all information of the publication in question. In the main program,
create publications Donald Duck (chief editor Aki Hyyppä) and Compartment No. 6 (author Rosa Liksom, 192 pages). Print out all information
of both publications using the methods you implemented.

"""