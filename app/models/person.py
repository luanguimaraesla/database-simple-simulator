from app.helpers.formatting import *
import re

class Person:
    def __init__(self, name, cpf):
        self.set_name(name)
        self.set_cpf(cpf)

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
    
        
 