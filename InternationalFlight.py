from Flight import Flight

class InternationalFlight(Flight):
    def __init__(self, flight_number, flight_code, destination, duration, price, departure_date,available_seats):
        super().__init__(flight_number, flight_code, destination, duration, price, departure_date,available_seats)

    def flight_type(self):
        return "Nemzetközi Járat"