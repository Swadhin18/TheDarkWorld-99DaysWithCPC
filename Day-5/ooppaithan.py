class MyClass:
    def __init__(self, a, b, c, d, e, allbooks):
        self.name = a
        self.age = b
        self.gender = c
        self.birthplace = d
        self.selected_books_indexes = e
        self.allbooks = allbooks

    def the_customer_information(self): 
        # Display customer information
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Birthplace:", self.birthplace)
        
        # Display selected books based on the indexes in `selected_books_indexes`
        print("Selected Books:")
        for index in self.selected_books_indexes:
            if 0 <= index < len(self.allbooks):  # Check if index is within the valid range
                print(self.allbooks[index])
            else:
                print(f"Invalid index {index}, skipping.")
            
        print("\n")

def main():
    AllBooks = ("The Book Thief", "The Little Prince", "Ikigai", "Sputnik", "AnciC", "Python", "Gitanjali")
    n1 = MyClass("Swadhin", 23, "Male", "Chandpur", (1, 3, 4), AllBooks)
    n2 = MyClass("Mehedi",23, "Male", "Jhinaidah",(4,5,6),AllBooks)
    
    # Call the method to display the customer information
    n1.the_customer_information()
    n2.the_customer_information()

main()
