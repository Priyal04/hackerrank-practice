from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

#Write MyBook class
class MyBook(Book):
    price = 0
    def __init__(self, title, author, price):
        super(Book, self).__init__()
        self.price = price
        super().__init__(title, author)

    def display(self):
        print("Title: "+ title)
        print("Author: "+ author)
        print("Price: "+str(price))
title=input()