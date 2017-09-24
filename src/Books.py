# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

class Book:
    'base class for books'
    book_id = 0
    name = ''
    author = ''
    costPrice = 0.0
    sellPrice = 0.0
    
    def __init__(self,n,a,cP,sP):
        self.book_id =+ 1
        self.name = n
        self.author = a
        self.costPrice = cP
        self.sellPrice = sP
    
    def display(self):
        print("Name: " + self.name + "\n" +
              "Author: " + self.author)
       
          
