class TicketBooking:
    #Inicializáljuk a foglalások listáját
    #Inicializáljuk a foglalások listáját
    def __init__(self):
        self._bookings = []

    #Hozzáad egy járatot a foglalásokhoz és csökkenti a szabad helyek számát
    def add_booking(self, Flight):
        if Flight.available_seats > 0:
            self._bookings.append(Flight)
            Flight.available_seats -= 1
            return True


    #Töröl egy foglalást a listából és növeli a járaton a szabad helyek számát
    def cancel_booking(self, booking_index):
        if 0 <= booking_index < len(self._bookings):
            Flight = self._bookings[booking_index]
            Flight.available_seats += 1
            del self._bookings[booking_index]
            return True
        else:
            print("\033[31;40mÉrvénytelen foglalási szám!\033[0m")
            return False
            print("\033[31;40mÉrvénytelen foglalási szám!\033[0m")
            return False

    #A foglalások listázása
    #A foglalások listázása
    def list_bookings(self):
        if not self._bookings:
            print("\033[31;40mNincsenek foglalások!\033[0m")
            print("\033[31;40mNincsenek foglalások!\033[0m")
            return
        print("\nAktuális foglalások:")
        for i, flight in enumerate(self._bookings, start=1):
            print(f"{i}. {flight.flight_type()} - {flight.flight_number} - {flight.flight_code} -> {flight.destination}, Ár: {flight.price} Ft, Indulás: {flight.departure_date}")