from app.helpers.formatting import *
import re

class Car:
    _cars_counter = 0

    def __init__(self, brand, model, year, license_plate):
        self.set_brand(brand)
        self.set_model(model)
        self.set_year(year)
        self.set_license_plate(license_plate)
        self.owner = None
        self.owner_id = None
        self.id = str(Car._cars_counter)
        Car._cars_counter += 1

    def set_brand(self, brand):
        try:
            self.brand = capitalize_all_words(brand)
        except TypeError as type_err:
            # Increase error's scope
            type_err.message = "Brand must be a string"
            raise type_err    

    def set_model(self, model):
        try:
            self.model = capitalize_all_words(model) 
        except TypeError as type_err:
            # Increase error's scope
            type_err.message = "Car's model must be a string"
            raise type_err

    def set_year(self, year):
        if isinstance(year, str):
            valid_year_regex = re.compile('[12][09]\d{2}')
            if valid_year_regex.match(year):
                self.year = year
            else:
                # year should match regex
                error_message = "Wrong format for the year"
                raise StandardError(error_message)
        else:
            # raise error if year is in the incorrect format
            error_message = "Year should be a string"
            raise TypeError(error_message)
    
    def set_license_plate(self, license_plate):
        if isinstance(license_plate, str):
            letters = license_plate[:3].upper()
            if license_plate[3] == '-':
                license_plate = letters + license_plate[3:]
            else:
                license_plate = letters + '-' + license_plate[3:]
                    
            valid_license_plate_regex = re.compile('[A-Z]{3}-*\d{4}')

            if valid_license_plate_regex.match(license_plate):
                self.license_plate = license_plate
            else:
                # license_plate should match regex
                error_message = "Wrong format for the license plate"
                raise StandardError(error_message)
        else:
            # raise error if license_plate is in the incorrect format
            error_message = "License plate should be a string"
            raise TypeError(error_message)

    def set_owner(self, owner):
        owner.attach_a_car(self)
