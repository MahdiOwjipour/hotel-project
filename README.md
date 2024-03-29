﻿# Hotel Management System

This project is a Hotel Management System implemented in Python, utilizing Object-Oriented Programming (OOP). The system manages various aspects of a hotel, such as staff, guests, and room bookings.

## Table of Contents

- [Classes](#classes)
  - [Person](#person)
  - [Admin](#admin)
  - [Staff](#staff)
  - [Receptionist](#receptionist)
  - [Housekeeping](#housekeeping)
  - [Maintenance](#maintenance)
  - [Guest](#guest)
  - [Rooms](#rooms)
  - [Hotel](#hotel)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Classes

### Person

- Attributes:

  - unique_id
  - name
  - contact_info

- Methods:
  - `__init__(self, unique_id, name, contact_info)`: Initialize common attributes.
  - `update_contact_details(self, new_contact_info)`: Update contact details.
  - `__str__(self)`: Return a string representation of the person.

### Admin

- Inherits from `Person`.

- Additional Methods:
  - `create_staff_account(self, staff_details, hotel)`: Add a new staff member to the hotel.
  - `remove_staff_member(self, staff_id)`: Remove an existing staff member.
  - `update_staff_role(self, staff_id, new_role)`: Change the role of a staff member.
  - `approve_maintenance_request(self, room_id, maintenance_type)`: Approve maintenance requests.

### Staff

- Inherits from `Person`.

- Additional Methods:
  - `generate_payroll_report(self)`: Create a report for staff salaries.

### Receptionist

- Inherits from `Staff`.

- Additional Methods:
  - `book_guest(self, guest_id, room_id)`: Book a room for a guest.
  - `check_out_guest(self, guest_id)`: Process guest check-out.

### Housekeeping

- Inherits from `Staff`.

- Additional Methods:
  - `mark_room_cleaned(self, room_id)`: Mark a room as cleaned.
  - `request_cleaning_supplies(self)`: Request cleaning supplies.

### Maintenance

- Inherits from `Staff`.

- Additional Methods:
  - `report_repair_done(self, room_id)`: Report completion of room repair.
  - `order_repair_materials(self, material_list)`: Order repair materials.

### Guest

- Inherits from `Person`.

- Additional Methods:
  - `request_room_booking(self, room_type, dates)`: Request room booking.
  - `amend_booking(self, booking_id, new_dates)`: Amend booking dates.
  - `cancel_booking(self, booking_id)`: Cancel a booking.
  - `give_feedback(self, feedback_text)`: Provide feedback.

### Rooms

- Methods:
  - `set_room_status(self, new_status)`: Change the status of the room.
  - `schedule_room_maintenance(self, maintenance_type)`: Schedule room maintenance.
  - `__str__(self)`: Return details of the room, including type and status.

### Hotel

- Methods:
  - `__init__(self)`: Initialize the hotel with an empty list of staffs.
  - `add_staff(self, staff)`: Add a staff member to the hotel.
  - `list_available_rooms(self, room_type)`: Show all available rooms of a specified type.
  - `get_guest_details(self, guest_id)`: Retrieve details of a specific guest.
  - `summarize_daily_operations(self)`: Provide a summary of daily operations.

## Usage

To use the Hotel Management System, you can instantiate the classes and call the methods based on your requirements. Below is a basic example:

```python
from hotel import Hotel
from admin import Admin

# Initialize Hotel
hotel = Hotel()

# Create Admin
admin = Admin(1, "Admin Name", "admin_contact")

# Create Staff Account
admin.create_staff_account((101, "Staff Name", "staff_contact"), hotel)

# Perform other operations as needed
# ...

# Summarize Daily Operations
hotel.summarize_daily_operations()

```
