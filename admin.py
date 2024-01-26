from person import *
from room import *
from staff import *

class Admin(Person):
    def __init__(self, id_, first_name, last_name, age):
        super().__init__(id_, first_name, last_name, age)

    def create_staff_account(self, staff_details):
        pass

    def remove_staff_member(self, staff_id):
        pass

    def update_staff_role(self, staff_id, new_role):
        pass

    def approve_maintenance_request(self, room_id, maintenance_type):
        pass

    def generate_payroll_report(self):
        pass