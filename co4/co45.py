class Publisher:
    def __init__(self,name):
        self.name=name
class Book(Publisher):
    def __init__(self,name,title,author):
        super().__init__(name)
        self.title=title
        self.author=author
    def display(self):
        print("name:",self.name)    
        print("title:",self.title)    
        print("author:",self.author)
        
class Python(Book):
    def __init__(self,name,title,author,price,pages):
        super().__init__(name,title,author)
        self.price=price
        self.pages=pages
    def display(self):
        super().display()
        print("price:",self.price)    
        print("pages:",self.pages)    
Book1=Python(name="vk",title="jokil",author="lua",price="1000",pages="100")
Book1.display() 
        
                
                