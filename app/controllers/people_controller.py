from app.models.person import Person

def save_person(person):
    try:
        with open('app/data/people.data', 'a') as people_data_file:
            text_to_save = "|".join([person.id,
                                     person.name,
                                     person.cpf,
                                     str(list(person.cars.keys())).replace("'","")
                                     ]) + '|\n'
            people_data_file.write(text_to_save)
            print("passou aqui")
    except IOError as io_err:
        # Display error message [TODO]
        print(str(io_err))


