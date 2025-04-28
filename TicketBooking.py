class TicketBooking:
    def __init__(self):
        self._bookings = []

    def add_booking(self, Flight):
        self._bookings.append(Flight)
        Flight.available_seats -= 1      

    def cancel_booking(self, i):
        if 0 <= i < len(self._bookings):
            Flight = self._bookings[i]
            Flight.available_seats += 1
            del self._bookings[i]
            
            
        else:
            print("Érvénytelen választás!")

    def list_bookings(self):
        if not self._bookings:
            print("Nincsenek foglalások!")
            return
        print("\nAktuális foglalások:")
        for i, Flight in enumerate(self._bookings, start=1):
            print(f"{i}. {Flight.flight_type()} - {Flight.flight_number} - {Flight.flight_code} -> {Flight.destination}, Ár: {Flight.price} Ft, Indulás: {Flight.departure_date}")