from Flight import Flight

#Inicializálja a belföldi járat adatait, örökölve az ősosztályból (Flight) osztálytól
class DomesticFlight(Flight):
    def __init__(self, flight_number, flight_code, destination, duration, price, departure_date,available_seats):
        super().__init__(flight_number, flight_code, destination, duration, price, departure_date,available_seats)

    #Visszaadja a járat típusát
    def flight_type(self):
        return "Belföldi Járat"