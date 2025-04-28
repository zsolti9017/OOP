from abc import ABC, abstractmethod

class Flight(ABC):
    def __init__(self, flight_number, flight_code, destination, duration, price, departure_date, available_seats):
        self._flight_number = flight_number
        self._flight_code =flight_code
        self._destination = destination
        self._duration =duration
        self._price = price
        self._departure_date = departure_date
        self._available_seats = available_seats
        
        

    @property
    def flight_number(self):
        return self._flight_number
    
    @property
    def flight_code(self):
        return self._flight_code

    @property
    def destination(self):
        return self._destination
    
    @property
    def duration(self):
        return self._duration

    @property
    def price(self):
        return self._price

    @property
    def departure_date(self):
        return self._departure_date

    @property
    def available_seats(self):
        return self._available_seats

    @available_seats.setter
    def available_seats(self, value):
        if value >= 0:
            self._available_seats = value
        else:
            print("Hiba: Az elérhető helyek száma nem lehet negatív.")
            
    @abstractmethod
    def flight_type(self):
        pass