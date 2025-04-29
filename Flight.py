from abc import ABC, abstractmethod

class Flight(ABC):
    #Inicializálja a járat alapvető adatait.
    def __init__(self, flight_number, flight_code, destination, duration, price, departure_date, available_seats):
        self._flight_number = flight_number
        self._flight_code =flight_code
        self._destination = destination
        self._duration =duration
        self._price = price
        self._departure_date = departure_date
        self._available_seats = available_seats
        
        
    #Visszaadja a járat számát
    @property
    def flight_number(self):
        return self._flight_number
    
    #Visszaadja a járat kódját
    @property
    def flight_code(self):
        return self._flight_code

    #Visszaadja a járat célállomását
    @property
    def destination(self):
        return self._destination
    
    #Visszaadja a járat menetidejét
    @property
    def duration(self):
        return self._duration

    #Visszaadja a járat árát
    @property
    def price(self):
        return self._price

    #Visszaadja a járat indulási dátumát
    @property
    def departure_date(self):
        return self._departure_date

    #Visszaadja a járaton elérhető helyek számát
    @property
    def available_seats(self):
        return self._available_seats

    #Beállítja a szabad helyek számát
    @available_seats.setter
    def available_seats(self, value):
        if value >= 0:
            self._available_seats = value
            
    
    #Absztrakt metódus a járat típusának lekérdezésére (pl. belföldi, nemzetközi)
    @abstractmethod
    def flight_type(self):
        pass