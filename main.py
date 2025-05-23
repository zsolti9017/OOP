from Airline import Airline
from TicketBooking import TicketBooking
from DomesticFlight import DomesticFlight
from InternationalFlight import InternationalFlight

class MainMenu:
    #Létrehozzuk a légitársaságunkat
    def __init__(self):
        self._airline = Airline("OOP Airlines")
        self._ticket_booking = TicketBooking()
        self._init_data()

    #járatok és alap foglalások feltöltése
    def _init_data(self):
        self._airline.add_flight(DomesticFlight("W6-1234", "BUD-DEB", "Debrecen", 0.6, 15000,"2025-06-12",10))
        self._airline.add_flight(DomesticFlight("W6-1235", "BUD-PEC", "Pécs", 0.5, 10000,"2025-06-14",11))
        self._airline.add_flight(DomesticFlight("W6-1236", "BUD-SZE", "Szeged", 0.7, 12000,"2025-06-10",3))
        self._airline.add_flight(InternationalFlight("BA-789", "BUD-LHR", "London", 2.2, 50000,"2025-06-10",2))
        self._airline.add_flight(InternationalFlight("AA-456", "BUD-JFK", "New York", 10, 180000,"2025-06-01",2))
        self._airline.add_flight(InternationalFlight("SQ-321", "BUD-BEI", "Peking", 12.1, 210000,"2025-06-04",2))
        self._ticket_booking.add_booking(self._airline.flights[0])
        self._ticket_booking.add_booking(self._airline.flights[1])
        self._ticket_booking.add_booking(self._airline.flights[4])
        self._ticket_booking.add_booking(self._airline.flights[0])
        self._ticket_booking.add_booking(self._airline.flights[4])
        self._ticket_booking.add_booking(self._airline.flights[1])

    #Kiszerveztem a menü alól a jegyfoglalás és törlést, így átláthatóbb a menürész kódja
    def handle_booking(self):
         while True: 
            self._airline.list_flights() # Járatok listázása minden foglalás előtt, hogy látható legyen miből lehet válogatni
            valasztas = input("\nAdd meg a foglalni kívánt járat sorszámát (0 a kilépéshez): ")
            if valasztas == "0":
                print("\n\033[31;40mVisszatérés a főmenübe.\033[0m\n")
                break
            try:
                flight_index = int(valasztas) - 1
                if 0 <= flight_index < len(self._airline.flights):
                    selected_flight = self._airline.flights[flight_index]
                    if selected_flight.available_seats > 0:  # Ellenőrizzük, van-e még hely
                        while True:
                            travel_date_str = input(f"Add meg a kívánt utazási dátumot ({selected_flight.departure_date}): ")
                            if travel_date_str == selected_flight.departure_date:
                                self._ticket_booking.add_booking(selected_flight)
                                print("Sikeres foglalás!\n")
                                break
                            else:
                                print(f"Ezen a napon ({travel_date_str}) nem indul ez a járat. Kérlek, add meg a helyes dátumot ({selected_flight.departure_date}).")
                    else:
                        print("\n\033[31;40mNincs elérhető hely a járatra.\033[0m\n")
                else:
                    print("\n\033[31;40mÉrvénytelen választás! Kérlek, adj meg egy érvényes sorszámot vagy 0 a kilépéshez.\033[0m\n")
            except ValueError:
                print("\n\033[31;40mHibás bevitel! Kérlek, csak számot adj meg.\033[0m\n")


    def handle_cancellation(self):
        while True:
            self._ticket_booking.list_bookings()
            try:
                i = int(input("\nAdd meg a lemondani kívánt foglalás sorszámát (0 a kilépéshez): "))

                if i == 0:
                    print("\n\033[31;40mVisszatérés a főmenübe.\033[0m\n")
                    break
                elif 0 < i <= len(self._ticket_booking._bookings):
                    if self._ticket_booking.cancel_booking(i - 1):
                        print("Sikeres lemondás!")
                else:
                    print("\n\033[31;40mÉrvénytelen sorszám!\033[0m\n")

            except ValueError:
                print("\n\033[31;40mHibás bevitel! Kérlek adj meg egy számot.\033[0m\n")


    #főmenü elemei és azok meghívása            
    def menu(self):
        while True:
            print(f"\n✈ ✈ ✈  {self._airline._name} Foglalási rendszer ✈ ✈ ✈\n")
            print("1. Járatok listázása")
            print("2. Jegy foglalása")
            print("3. Foglalás lemondása")
            print("4. Foglalások listázása")
            print("\033[31;40m5. Kilépés\033[0m\n")


            while True:
                choice = input("\nVálassz egy lehetőséget: ")
                if choice in ["1", "2", "3", "4", "5"]:
                    break
                else:
                    print("\n\033[31;40mÉrvénytelen választás! Kérlek, válassz egyet az 1-5 közötti lehetőségek közül.\033[0m\n")

            if choice == "1":
                self._airline.list_flights()
                input("\nNyomj Enter-t a folytatáshoz...")
            
            elif choice == "2":
                   self.handle_booking()

            elif choice == "3":
                 self.handle_cancellation()

            elif choice == "4":
                self._ticket_booking.list_bookings()
                input("\nNyomj Enter-t a folytatáshoz...")

            elif choice == "5":
                print(f"\nKöszönjük, hogy az {self._airline._name}-t választotta!")
                break


#Létrehozza a főmenü objektumot és elindítja a menüt.
if __name__ == "__main__":
    menu = MainMenu()
    menu.menu()