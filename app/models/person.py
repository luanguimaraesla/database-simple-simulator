from app.helpers.formatting import *
from app.models.car import Car
import re

class Person:
    _people_counter = 0

    def __init__(self, name, cpf, id=None):
        self.set_name(name)
        self.set_cpf(cpf)
        self.cars = {} # id : car object
        if not id:
            self.id = str(Person._people_counter)
            Person._people_counter += 1
        else:
            self.id = id

    def set_name(self, name):
        try:
            self.name = capitalize_all_words(name) 
        except TypeError as type_err:
            # Increase error's scope
            type_err.message = "Person's name must be a string"
            raise type_err
    
    def set_cpf(self, cpf):
        # Create a valid regex to validates cpf field
        valid_cpf_regex = re.compile('([0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}' + \
                                     '[\/]?[0-9]{4}[-]?[0-9]{2})|([0-9]{3}'+ \
                                     '[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2})')
        if valid_cpf_regex.match(cpf):
            self.cpf = cpf
        else:
            error_message = "Invalid format for CPF"
            raise TypeError(error_message)

    def append_a_car(self, car):
        if isinstance(car, Car):
            self.cars[car.id] = car
        else:
            error_message = "car must be a Car object"
            raise TypeError(error_message)
    
    def attach_a_car(self, car):
        if isinstance(car, Car):
            car.owner = self
            car.owner_id = self.id
            self.append_a_car(car)
        else:
            error_message = "car must be a Car object"
            raise TypeError(error_message)
