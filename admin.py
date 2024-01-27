from person import *
from room import *
from staff import *
from hotel import *

class Admin(Person):
    def __init__(self, id_, first_name, last_name, age):
        super().__init__(id_, first_name, last_name, age)
        self.staff_dict = {} # staff members

    def create_staff_account(self, new_staff):
        staff_id_ = input("new staff id: ")
        staff_first_name = input("new staff first name: ")
        staff_last_name = input("new staff last name: ")
        staff_age = input("new staff age: ")
        staff_role = input("new staff role: ")
        if new_staff.id_ not in self.staff_dict:
            self.staff_dict[new_staff.staff_id_] = new_staff
        else:
            print("id already existed!")

    def remove_staff_member(self, staff_id):
        for i in self.staff_dict:
            if i == staff_id:
                self.staff_dict.pop(i)
            else:
                print("id does not exist!")

    def update_staff_role(self, staff_id, new_role):
        if staff_id in self.staff_dict:
            self.staff_dict[self.id_][self.role] = new_role or self.role
        else:
            print("id does not exist!")

    def approve_maintenance_request(self, room_id, maintenance_type):
        pass

    def generate_payroll_report(self):
        pass

    def display_role(self):
        return f"{self.first_name} {self.last_name} is Admin"