class Cab:
    """
    Represents a single cab with basic attributes.
    """
    def __init__(self, cab_id, driver_name, location):
        self.cab_id = cab_id
        self.driver_name = driver_name
        self.location = location  # Simple string-based location
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "Not Available"
        return f"[Cab ID: {self.cab_id}, Driver: {self.driver_name}, Location: {self.location}, Status: {status}]"


class Booking:
    """
    Represents a booking with a unique booking ID,
    user information, pickup/drop-off details, and assigned cab.
    """
    def __init__(self, booking_id, user_name, pickup, drop_off, cab):
        self.booking_id = booking_id
        self.user_name = user_name
        self.pickup = pickup
        self.drop_off = drop_off
        self.cab = cab

    def __str__(self):
        return (f"Booking ID: {self.booking_id}, User: {self.user_name}, "
                f"Pickup: {self.pickup}, Drop-off: {self.drop_off}, "
                f"Cab: {self.cab.cab_id} ({self.cab.driver_name})")


class BookingSystem:
    """
    Main system to manage cabs and bookings.
    """
    def __init__(self):
        # Lists to store Cab and Booking objects
        self.cabs = []
        self.bookings = []
        self.booking_counter = 1  # Simple incrementing ID for bookings

    def add_cab(self, cab):
        """
        Add a new cab to the list of cabs.
        """
        self.cabs.append(cab)

    def show_available_cabs(self):
        """
        Print out the details of all currently available cabs.
        """
        available_cabs = [cab for cab in self.cabs if cab.is_available]
        if not available_cabs:
            print("\nNo cabs are currently available.\n")
        else:
            print("\nAvailable Cabs:")
            for cab in available_cabs:
                print(cab)
            print()

    def create_booking(self, user_name, pickup, drop_off):
        """
        Create a new booking for the user if an available cab is found.
        This simple implementation chooses the *first* available cab.
        """
        available_cabs = [cab for cab in self.cabs if cab.is_available]
        if not available_cabs:
            print("\nNo cabs available to book.\n")
            return

        # Here, we simply pick the first available cab
        chosen_cab = available_cabs[0]
        chosen_cab.is_available = False  # Mark the cab as not available

        booking = Booking(
            booking_id=self.booking_counter,
            user_name=user_name,
            pickup=pickup,
            drop_off=drop_off,
            cab=chosen_cab
        )

        self.bookings.append(booking)
        self.booking_counter += 1

        print("\nBooking created successfully!")
        print(booking)
        print()

    def show_all_bookings(self):
        """
        Show all existing bookings.
        """
        if not self.bookings:
            print("\nNo bookings have been made yet.\n")
        else:
            print("\nAll Bookings:")
            for booking in self.bookings:
                print(booking)
            print()

    def cancel_booking(self, booking_id):
        """
        Cancel a booking based on booking ID.
        The cab assigned to that booking is then made available again.
        """
        for booking in self.bookings:
            if booking.booking_id == booking_id:
                # Mark the associated cab as available again
                booking.cab.is_available = True
                self.bookings.remove(booking)
                print(f"\nBooking ID {booking_id} has been canceled.\n")
                return
        print(f"\nNo booking found with ID {booking_id}.\n")


def main():
    # Initialize the booking system
    system = BookingSystem()

    # For demonstration, we add a few cabs to the system
    system.add_cab(Cab(cab_id=101, driver_name="Alice", location="Downtown"))
    system.add_cab(Cab(cab_id=102, driver_name="Bob", location="Airport"))
    system.add_cab(Cab(cab_id=103, driver_name="Charlie", location="Uptown"))

    while True:
        print("=== CAB AGGREGATION/BOOKING SYSTEM ===")
        print("1. Show Available Cabs")
        print("2. Book a Cab")
        print("3. Show All Bookings")
        print("4. Cancel a Booking")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            system.show_available_cabs()

        elif choice == "2":
            user_name = input("Enter your name: ").strip()
            pickup = input("Enter pickup location: ").strip()
            drop_off = input("Enter drop-off location: ").strip()
            system.create_booking(user_name, pickup, drop_off)

        elif choice == "3":
            system.show_all_bookings()

        elif choice == "4":
            try:
                booking_id = int(input("Enter the booking ID to cancel: ").strip())
                system.cancel_booking(booking_id)
            except ValueError:
                print("\nInvalid booking ID. Please enter a numeric value.\n")

        elif choice == "5":
            print("\nExiting the system. Thank you!\n")
            break

        else:
            print("\nInvalid choice. Please select a valid option.\n")


if __name__ == "__main__":
    main()
