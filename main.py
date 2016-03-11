#from app.models.car import Car
#from app.models.person import Person
#from app.controllers.people_controller import *
#from app.controllers.cars_controller import *
from app.controllers.application_controller import *

def main():
#    aPerson = Person("luan guimaraes", "05199692194")
#    aCar = Car("Ford", "thunder bird", "1986", "LIS7654")
#    aPerson.attach_a_car(aCar)
#    print("aqui")
#    save_person(aPerson)
#    save_car(aCar)
    load_database()
    menu()


if __name__ == '__main__':
    main()
