from Flight import Flight

class DomesticFlight(Flight):
    def __init__(self, flight_number, flight_code, destination, duration, price, departure_date):
        super().__init__(flight_number, flight_code, destination, duration, price, departure_date)


    def flight_type(self):
        return "Belföldi Járat"