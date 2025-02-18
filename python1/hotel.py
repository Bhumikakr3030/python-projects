class BookingManager:
    def __init__(self):
        self.bookings = []

    def book_room(self, room_number, customer_name):
        self.bookings.append({"room_number": room_number, "customer_name": customer_name})
        print(f"Room {room_number} booked by {customer_name}.")

    def view_all_bookings(self):
        if not self.bookings:
            print("No bookings available.")
        else:
            for booking in self.bookings:
                print(f"Room Number: {booking['room_number']}, Customer: {booking['customer_name']}")

class RoomManager:
    def __init__(self):
        self.rooms = []

    def add_room(self, room_number, room_type):
        if any(room['room_number'] == room_number for room in self.rooms):
            print(f"Room {room_number} already exists.")
        else:
            self.rooms.append({"room_number": room_number, "room_type": room_type})
            print(f"Room {room_number} added successfully.")

    def view_all_rooms(self):
        if not self.rooms:
            print("No rooms available.")
        else:
            for room in self.rooms:
                print(f"Room Number: {room['room_number']}, Type: {room['room_type']}")

    def is_room_available(self, room_number):
        return any(room['room_number'] == room_number for room in self.rooms)

def main():
    room_manager = RoomManager()
    booking_manager = BookingManager()

    while True:
        print("\nHotel Management System")
        print("1. Add Room")
        print("2. Book Room")
        print("3. View All Rooms")
        print("4. View All Bookings")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            room_number = input("Enter room number: ")
            room_type = input("Enter room type: ")
            room_manager.add_room(room_number, room_type)
        elif choice == '2':
            room_number = input("Enter room number: ")
            if room_manager.is_room_available(room_number):
                customer_name = input("Enter customer name: ")
                booking_manager.book_room(room_number, customer_name)
            else:
                print(f"Room {room_number} does not exist.")
        elif choice == '3':
            room_manager.view_all_rooms()
        elif choice == '4':
            booking_manager.view_all_bookings()
        elif choice == '5':
            confirm = input("Are you sure you want to exit? (y/n): ")
            if confirm.lower() == 'y':
                break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()