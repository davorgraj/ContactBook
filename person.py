# -*- coding: utf-8 -*-
class Person(object):

    def __init__(self, f_name, l_name, email, phone, age):
        self.first_name = f_name
        self.last_name = l_name
        self.email = email
        self.phone_number = phone
        self.age = age

    def GetFullName(self):
        return self.first_name + " " + self.last_name

def ListAllPerson(seznam):
    for index, oseba in enumerate(seznam):
        print "ID: " + str(index)
        print "Name: " + oseba.GetFullName()
        print "Email: " + oseba.email
        print "Phone number: " + oseba.phone_number
        print "Age: " + str(oseba.age)
        print ""

def AddNewContact(seznam):
    first_name = raw_input("Vnesite ime: ")
    last_name = raw_input("Vnesite priimek: ")
    email = raw_input("Vnesite email naslov: ")
    phone_number = raw_input("Vnesite telefonsko številko: ")
    age = raw_input("Vnesite starost: ")

    nova_oseba = Person(f_name=first_name, l_name=last_name, email=email, phone=phone_number, age=age)
    seznam.append(nova_oseba)

    print ""
    print "Osebo " + nova_oseba.GetFullName() + " ste uspešno dodali na vaš seznam."
    print ""

def EditContact(seznam):
    print "Kontakti na voljo:"

    for index, person in enumerate(seznam):
        print "ID: " + str(index) + " - " + person.GetFullName()
    print ""

    contact_id = int(raw_input("Izberite ID kontakta katerega želite urediti:"))
    if contact_id <= len(seznam)-1:
        izbrani_kontakt = seznam[contact_id]

        nov_email = raw_input("Vnesite novi email za izbrano osebo %s:" % izbrani_kontakt.GetFullName())
        izbrani_kontakt.email = nov_email
    else:
        print "seznam ne obstaja!"
        EditContact(seznam)


def DeleteContact(seznam):
    print "Kontakti na voljo:"

    for index, oseba in enumerate(seznam):
        print "ID: " + str(index) + " - " + oseba.GetFullName()
    print ""

    id = raw_input("Izberite ID kontakta katerega želite izbrisati:")
    izbrani_kontakt = seznam[int(id)]

    seznam.remove(izbrani_kontakt)

