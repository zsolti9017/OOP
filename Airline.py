from Flight import Flight
class Airline:
    def __init__(self, name):
        self._name = name
        self._flights = []

    def add_flight(self, Flight):
        self._flights.append(Flight)

    def list_flights(self):
        
        for i, Flight in enumerate(self._flights, start=1):
            print(f"{i}. {Flight.flight_type()} - {Flight.flight_number} - {Flight.flight_code} -> {Flight.destination}, Ár: {Flight.price} Ft, Indulás: {Flight.departure_date}, Repülési idő: {Flight.duration} óra , Elérhető jegyek száma: {Flight.available_seats}")

    @property
    def flights(self):
        return self._flights