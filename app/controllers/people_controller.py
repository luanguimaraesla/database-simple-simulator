from app.models.person import Person
from app.controllers.cars_controller import *

def create_person(name, cpf, cars):
    person = Person(name, cpf)
    for car in cars:
        person.attach_a_car(car)
    return person

def save_next_person_id_reference():
    try:
        with open('app/data/people_next_id.data', 'w') as people_data_file:
            text_to_save = str(Person._people_counter)
            people_data_file.write(text_to_save)
    except IOError as io_err:
        # Display error message [TODO]
        print(str(io_err))

def save_person(person):
    try:
        with open('app/data/people.data', 'a') as people_data_file:
            cars_ids = list(person.cars.keys())
            text_to_save = "|".join([person.id,
                                     person.name,
                                     person.cpf,
                                     str(cars_ids).replace("'","")
                                     ]) + '|\n'
            people_data_file.write(text_to_save)
            
            for car_id in cars_ids:
                save_car(person.cars[car_id])

    except IOError as io_err:
        # Display error message [TODO]
        print(str(io_err))

def find_person_by_id(person_id):
    try:
        with open('app/data/people.data') as people_data_file:
            content = people_data_file.readlines()[1:]
            person_info = None
            for person_dump in content:
                person_info = person_dump.strip().split('|')
                if person_id == person_info[0]:
                    break
                else:
                    pass #continue
            else:
                # No matches
                return None
            
            person = Person(person_info[1], person_info[2], person_info[0])
            
            cars_ids = person_info[3].strip('[]').split(',')

            for car_id in cars_ids:
                car = find_car_by_id(car_id.strip())
                if car:
                    person.attach_a_car(car)
                else:
                    # Display error message [TODO]
                    print("error")

            return person
    except IOError as io_err:
        # Display error message [TODO]
        print(str(io_err))
