from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, id_, first_name, last_name, age):
        self.id_ = id_
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def update_contact_details(self, new_first_name, new_last_name, new_age):
        self.first_name = new_first_name or self.first_name
        self.last_name = new_last_name or self.last_name
        try:
            self.age = int(new_age or self.age)
        except ValueError:
            print("age must be valid integer!")

    def __str__(self):
        return f"first name: {self.first_name}, last name: {self.last_name}, age: {self.age}"
    
    @abstractmethod
    def display_role(self):
        pass
        
if __name__ == "__main__":
    p1 = Person(123, "a", "b", 20)
    print(p1)

# Error handling:
# name error id_

