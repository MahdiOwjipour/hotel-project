from person import *
from room import *
from guest import *

class Staff(Person):
    def __init__(self, id_, first_name, last_name, age, role):
        super().__init__(id_, first_name, last_name, age)
        self.role = role

    # receptionist
    def book_room(self, guest_id, room_id):
        if self.guest_id not in self.room_booking and :
            self.room_booking[guest_id] = room_id
            self.room_is_available = False
            print("guest checked in successfully!")
        else:
            print("the id aleady exists")
    def check_out_guest(self, guest_id):
        pass

    # housekeeping
    def mark_room_cleaned(self, room_id):
        pass

    def request_cleaning_supplies(self):
        pass

    # maintenance
    def report_repair_done(self, room_id):
        pass

    def order_repair_materials(self, material_list):
        pass
    
