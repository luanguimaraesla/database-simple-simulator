from app.controllers.cars_controller import *
from app.controllers.people_controller import *

people = []
IS_DATABASE_LOADED = False

def drop_database():
    
    with open('app/data/people_next_id.data', 'w') as people_data_file:
        people_data_file.write('0')
    with open('app/data/cars_next_id.data', 'w') as cars_data_file:
        cars_data_file.write('0')
    with open('app/data/people.data', 'w') as people_data_file:
        people_data_file.write('id | name | cpf | cars_id |\n')
    with open('app/data/cars.data', 'w') as cars_data_file:
        cars_data_file.write('id | brand | model | year | license plate| owner id |\n')

def load_database():
    try:
        with open('app/data/people_next_id.data') as people_data_file:
            Person._people_counter = int(people_data_file.readlines()[0].strip())
        
        with open('app/data/cars_next_id.data') as cars_data_file:
            Car._cars_counter = int(cars_data_file.readlines()[0].strip())
        
        with open('app/data/people.data') as people_data_file:
            content = people_data_file.readlines()[1:]
            person_info = None
            ids = []
            global people
            for person_dump in content:
                person_info = person_dump.strip().split('|')
                
                people += [find_person_by_id(person_info[0])]

            global IS_DATABASE_LOADED
            IS_DATABASE_LOADED = True
    except IOError as io_err:
        # Display error message [TODO]
        print(str(io_err))
   
def print_people():
    for person in people:
        print("===================================================================")
        print('\n' + person.id + "| Name: " + person.name + " | CPF: " + person.cpf)
        print("\nCars:\n")
        for id, car in list(person.cars.items()):
            print(id + "| Brand: " + car.brand + " | Model: " + car.model +
                  " | Year: " + car.year + " | License Plate: " +
                  car.license_plate + "\n")
        print('\n')
        print("===================================================================")
        print('\n')

def list_people():
    global IS_DATABASE_LOADED
    if not IS_DATABASE_LOADED:
        load_database()

    print_people()
    

def print_menus_options():
    menu_text = "0. Drop DB\n1. Add person\n2. List people\n3. Exit\n Select: "
    op = int(input(menu_text))
    return op

def menu():
    while(True):
        selected_option = print_menus_options()
        if selected_option == 0:
            drop_database()
            print("Success\n")

        elif selected_option == 1:
            name = input("Name: ")
            cpf = input("CPF: ")
            cars = []
            repeat = True
            while(repeat):
                car_brand = input("Car's brand: ")
                car_model = input("Car's model: ")
                car_year = input("Car's year: ")
                car_lp = input("Car's License Plate: ")
                cars += [create_car(car_brand, car_model, car_year, car_lp)]
                op = input("\nWant to add another car to " + name + "?(y/n) ")
                if op == 'y' or op == 'Y':
                    repeat = True
                else:
                    repeat = False

            person = create_person(name, cpf, cars)
            save_person(person)
            global people
            people += [person]

        elif selected_option == 2:
            list_people()

        else:
            save_next_person_id_reference()
            save_next_car_id_reference()
            exit()

