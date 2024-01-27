from person import *
from room import *
from guest import *
from admin import *
from hotel import *

class Staff(Person):
    def __init__(self, id_, first_name, last_name, age, role):
        super().__init__(id_, first_name, last_name, age)
        self.role = role
        self.room_guest_dict = {} # to ascribe a room id to a guest id

    # receptionist
    def book_guest(self, room, guest_id, room_id):
        if guest_id not in self.room_guest_dict and room.room_is_available == True:
            self.room_guest_dict[guest_id] = room_id
            room.room_is_available = False
            print("guest checked in successfully!")
        else:
            print("the id aleady exists")

    def check_out_guest(self, room, guest_id):
        if guest_id in self.room_guest_dict:
            self.room_guest_dict.pop(guest_id)
            room.room_is_available = False
        else:
            print("guest id does not exist!")

    # housekeeping
    def mark_room_cleaned(self, room, room_id):
        pass

    def request_cleaning_supplies(self):
        pass

    # maintenance
    def report_repair_done(self, room_id):
        pass

    def order_repair_materials(self, material_list):
        pass
    
