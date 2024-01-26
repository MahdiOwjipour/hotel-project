class room:
    def __init__(self, room_id, room_is_available, room_type):
        self.room_id = room_id
        self.room_is_available = room_is_available
        self.room_type = room_type

    def display_room_status(self):
        return self.room_is_available

    def set_room_status(self, new_status):
        pass

    def schedule_room_maintenance(self, maintenance_type):
        pass

    def __str__(self):
        return f"room id: {self.room_id}, "