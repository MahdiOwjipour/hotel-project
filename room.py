from person import *
from staff import *
from guest import *
from room import *
from admin import *

class room:
    def __init__(self, room_id, room_is_available, room_type, room_is_cleaned):
        self.room_id = room_id
        self.room_is_available = room_is_available
        self.room_type = room_type
        self.room_guest_dict = room_is_cleaned

    def display_room_status(self):
        return self.room_is_available

    def set_room_status(self, new_status):
        pass

    def schedule_room_maintenance(self, maintenance_type):
        pass

    def __str__(self):
        return f"room id: {self.room_id}, "