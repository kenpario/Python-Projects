class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"{self.title} by {self.author}, {self.num_pages} pages"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    
    def __gt__(self, other):
        return self.num_pages > other.num_pages

    def __add__(self, other):
        return self.num_pages + other.num_pages
    
    def __contains__(self, keyword):
        return keyword.lower() in self.title.lower() or keyword.lower() in self.author.lower()
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            raise KeyError(f"Invalid key: {key}. Valid keys are 'title', 'author', 'num_pages'.")

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
# book2 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 281)
book3 = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 309)
print(book1)
print(book2)
print(book3)
print(book1 == book2)
print(book2 < book3)
print(book3 > book2)
print(book1 + book2)
print("Gatsby" in book1)
print("Lee" in book3)
print(book1["title"])
print(book2["author"])
print(book3["num_pages"])