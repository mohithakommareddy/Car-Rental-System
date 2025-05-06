import datetime

class CarRentalSystem:
    def __init__(self):
        self.car_brands = ["HYUNDAI", "SUZUKI", "HONDA", "TOYOTA", "FORD", "TATA", "MERCEDES", "AUDI", "ISUZU"]
        self.car_models = ["Veloster", "Celerio", "Civic", "Avalon", "Explorer", "Safari", "E-Class", "Q3", "D-MAX"]
        self.car_seats = [4, 4, 4, 8, 4, 4, 4, 8, 8]
        self.car_rent_per_day = [250] * 9
        self.car_rent_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.rented_cars = []

    def display_cars(self):
        print("\n################################################")
        print("#    CAR BRAND   #  MODEL  # RENT PER DAY(Php) #")
        print("################################################")
        for i in range(len(self.car_brands)):
            print(f"# {self.car_brands[i]:<12} # {self.car_models[i]:<8} # {self.car_rent_per_day[i]:<15} #")
        print("################################################\n")

    def calculate_days(self, start_date, return_date):
        days = (return_date - start_date).days
        return days if days > 0 else 0

    def car_rent(self):
        self.display_cars()

        # Validate car name input
        while True:
            car_rented = input("ENTER THE BRAND OF CAR YOU WANT TO RENT: ").strip().upper()
            if car_rented in self.car_brands:
                break
            else:
                print("Invalid car brand. Please enter a valid car name from the list.")

        # Validate start date
        while True:
            try:
                start_date = input("ENTER DATE ON WHICH YOU WILL TAKE THE CAR (dd mm yyyy): ")
                start_date = datetime.datetime.strptime(start_date, "%d %m %Y")
                break
            except ValueError:
                print("Invalid date format. Please enter date in dd mm yyyy format.")

        # Validate return date
        while True:
            try:
                return_date = input("ENTER THE DATE ON WHICH YOU WILL RETURN THE CAR (dd mm yyyy): ")
                return_date = datetime.datetime.strptime(return_date, "%d %m %Y")
                if return_date > start_date:
                    break
                else:
                    print("Return date must be after the start date.")
            except ValueError:
                print("Invalid date format. Please enter date in dd mm yyyy format.")

        # Check if car is available
        for car in self.rented_cars:
            if car['car_rented'] == car_rented:
                if not (return_date <= car['start_date'] or start_date >= car['return_date']):
                    print("Car not available. Try another car.")
                    return

        # Get user details
        customer_name = input("ENTER YOUR NAME: ")
        customer_id = input("ENTER YOUR ID NUMBER: ")

        # Calculate rent
        days = self.calculate_days(start_date, return_date)
        rent = days * self.car_rent_per_day[self.car_brands.index(car_rented)]

        # Save rental details
        self.rented_cars.append({
            'customer_name': customer_name,
            'customer_id': customer_id,
            'car_rented': car_rented,
            'start_date': start_date,
            'return_date': return_date,
            'days': days,
            'rent': rent
        })

        # Show rental details
        print("\n--- RENTAL DETAILS ---")
        print(f"NAME: {customer_name}")
        print(f"ID: {customer_id}")
        print(f"CAR RENTED: {car_rented}")
        print(f"NUMBER OF DAYS: {days}")
        print(f"RENT: Php {rent}")
        print("----------------------\n")

    def car_return(self):
        customer_id = input("Please enter your ID number: ")

        for car in self.rented_cars:
            if car['customer_id'] == customer_id:
                print(f"\nHELLO {car['customer_name']}")
                
                # Confirm return details
                while True:
                    try:
                        start_date = input("ENTER THE DATE YOU TOOK THE CAR (dd mm yyyy): ")
                        start_date = datetime.datetime.strptime(start_date, "%d %m %Y")

                        return_date = input("ENTER THE RETURN DATE (dd mm yyyy): ")
                        return_date = datetime.datetime.strptime(return_date, "%d %m %Y")
                        
                        if return_date > start_date:
                            break
                        else:
                            print("Return date must be after the start date.")
                    except ValueError:
                        print("Invalid date format. Please enter date in dd mm yyyy format.")

                # Calculate total days and penalty (if any)
                actual_days = self.calculate_days(start_date, return_date)
                if actual_days > car['days']:
                    penalty = (actual_days - car['days']) * 50
                    car['rent'] += penalty
                    print(f"Penalty for late return: Php {penalty}")

                print(f"\nFINAL AMOUNT: Php {car['rent']}\n")

                # Remove from rented cars
                self.rented_cars.remove(car)
                return
        
        print("Customer not found.\n")

    def run(self):
        while True:
            print("\n1. Rent a Car")
            print("2. Return a Car")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.car_rent()
            elif choice == '2':
                self.car_return()
            elif choice == '3':
                print("Thank you for using our service! Goodbye.")
                break
            else:
                print("Invalid choice. Try again.")

# Run the program
if __name__ == "__main__":
    system = CarRentalSystem()
    system.run()
