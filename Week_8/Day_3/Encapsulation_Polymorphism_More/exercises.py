# ===================== Exercise 1 =============================


class A():
    def do_this(self):
        print("doing this in A")


class B(A):
    pass


class C():
    def do_this(self):
        print("doing this in C")


class D(B, C):
    pass

d_instance = D()
d_instance.do_this()
# Output will be "doing this in A", because first parent of D is B class.

# ===================== Exercise 2 =============================


class Book():
    def __init__(self, title, author, publication_date, price):
        self.title = title
        self.author = author
        self.publication = publication_date
        self.price = price

    def present(self):
        print(f'Title: {self.title}')


class Fiction(Book):
    def __init__(self, title, author, publication_date, price, is_awesome):
        super().__init__(title, author, publication_date, price)
        self.genre = 'Fiction'
        self.is_awesome = is_awesome
        if self.is_awesome:
            self.bored = False
            print('Woow this is an awesome book')
        else:
            self.bored = True
            print('I am very bored')


if __name__ == '__main__':
    foundation = Fiction('Asimov', 'Foundation', '1966', '5£', True)
    foundation.present() # Output: 'Foundation'
    print(foundation.price) # Output: '5£'
    print(foundation.bored) # Output: False'
    boring_book = Fiction('boring_guy', 'boring_title', 'boring_date', '9000£', False)
    print(boring_book.bored) # Output: True'