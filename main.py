# -*- coding: utf-8 -*-
from person import Person, ListAllPerson, AddNewContact, EditContact, DeleteContact


def main():
    oseba1 = Person("Davor", "Graj", "davorgraj@gmail.com", "031650253", 23)
    oseba2 = Person("David", "Grah", "davidgrah@gmail.com", "031650555", 28)
    oseba3 = Person("Samo", "Test", "test@gmail.com", "031643555", 30)

    seznam = [oseba1, oseba2, oseba3]

    while True:
        print "Izberite opcijo:"
        print "a) Poglejte vse kontakte"
        print "b) Dodajte novi kontakt"
        print "c) Uredite kontakt"
        print "d) Izbrišite kontakt"
        print "e) Izhod iz programa."
        print ""

        izbor = raw_input("Izberite opcijo (a, b, c, d ): ")
        print ""

        if izbor.lower() == "a":
            ListAllPerson(seznam)
        elif izbor.lower() == "b":
            AddNewContact(seznam)
        elif izbor.lower() == "c":
            EditContact(seznam)
        elif izbor.lower() == "d":
            DeleteContact(seznam)
        elif izbor.lower() == "e":
            print "Hvala za vaš obisk!"
            break
        else:
            print "Niste izprali pravilne opcije. Poskusite ponovno"

if __name__ == "__main__":
    main()
