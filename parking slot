#parking slot
class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current_count = 0
        self.parking_slots = []
    def park_vehicle(self):
        if self.current_count < self.capacity:
            car_number = input("Enter vehicle number to park: ")
            self.parking_slots.append(car_number)
            self.current_count += 1
            print(f"Vehicle {car_number} parked successfully.")
        else:
            print("Parking lot is full. Cannot park vehicle.")
    def exit_vehicle(self):
        car_number = input("Enter vehicle number to exit: ")
        if car_number in self.parking_slots:
            self.parking_slots.remove(car_number)
            self.current_count -= 1
            print(f"Vehicle {car_number} exited successfully.")
        else:
            print(f"Vehicle {car_number} not found in parking lot.")
    def display_status(self):
        print(f"Current number of vehicles parked: {self.current_count}/{self.capacity}")
        print("Vehicles parked: ", self.parking_slots)
parking_lot = ParkingLot(20)
while True:
    print("\nMenu:")
    print("1. Park a vehicle")
    print("2. Exit a vehicle")
    print("3. Display parking status")
    print("4. Exit the program")
    choice = input("Enter your choice (1/2/3/4): ")
    if choice == '1':
        parking_lot.park_vehicle()
    elif choice == '2':
        parking_lot.exit_vehicle()
    elif choice == '3':
        parking_lot.display_status()
    elif choice == '4':
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")