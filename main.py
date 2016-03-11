from app.models.car import Car
from app.models.person import Person

if __name__ == '__main__':
    aPerson = Person("luan guimaraes", "05199692194")
    aCar = Car("Ford", "thunder bird", "1986", "LIS7654")
    aPerson.attach_a_car(aCar)
